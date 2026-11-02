#!/usr/bin/env python3
"""
FPI Maker — CLI and library for generating Federated Payer Identifiers (FPIs).

This module is the ONE and ONLY home of FPI uuid generation logic in this
repository.  All other tools (including the Medicare Advantage seed) must
import from here rather than reimplementing hashing or normalization.

Each payer identifier namespace derives a deterministic UUID5 by chaining
from NAMESPACE_DNS:

    system_uuid = uuid5(NAMESPACE_DNS, "<SYSTEM_ID>.fhir")
    fpi         = uuid5(system_uuid,   "<payer_id_value>")

The list of payer identifier systems is loaded at runtime from the Federated
Payer Identifier repository's ``main`` branch:

    https://github.com/ftrotter-gov/FederatedPayerIdentifier/tree/main/reference_data

This repository does not vendor its own copy of that reference data, so the
tool always reflects the current approved list.  Set the
``FPI_REFERENCE_DATA_DIR`` environment variable to a local directory holding
``current_payer_identification_systems.json`` to run offline or against a
pinned revision.

State-level identifier systems (e.g. STATE_DOI_ID, STATE_MCO_ID) are only
unique within a single state.  Values in those systems MUST be prefixed with
the two-letter USPS state code and a hyphen (e.g. ``TX-68775``) before an FPI
is generated, in order to prevent collisions between states.

LEGAL_NAME_HASH normalization
-----------------------------
The LEGAL_NAME_HASH system hashes a payer's legal name.  Before hashing, the
name is ALWAYS normalized here in this module (never by callers):

    lowercase the name, then remove every character that is not a-z or 0-9

so ``"AETNA HEALTH, INC."`` is transformed to ``"aetnahealthinc"`` before the
UUID5 is computed.  ``generate_fpi`` applies this normalization automatically
whenever ``system_id == "LEGAL_NAME_HASH"``, so passing the raw legal name and
passing the pre-normalized name produce the same FPI.

Usage as a library
------------------
    from tools.FPI_maker_cli import generate_fpi, load_payer_systems

    fpi = generate_fpi(system_id="NAIC_ID", payer_id_value="78700")
    print(fpi)

Usage as a CLI
--------------
    python tools/FPI_maker_cli.py
"""

import json
import os
import re
import urllib.error
import urllib.request
import uuid

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Root anchor — same as uuid.NAMESPACE_DNS, named explicitly for clarity.
_ROOT_NAMESPACE = uuid.NAMESPACE_DNS

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.abspath(os.path.join(_SCRIPT_DIR, ".."))

# ---------------------------------------------------------------------------
# Reference data location
# ---------------------------------------------------------------------------
# The payer identifier reference data is NOT vendored into this repository.
# It is owned by the Federated Payer Identifier (FPI) repository and is read
# at runtime from the `main` branch of that public repository, so that this
# repo can never drift from the authoritative list.
#
#     https://github.com/ftrotter-gov/FederatedPayerIdentifier/tree/main/reference_data
#
# Set the FPI_REFERENCE_DATA_DIR environment variable to a local directory
# containing current_payer_identification_systems.json to work offline or to
# pin a specific revision.
REFERENCE_DATA_BASE_URL = (
    "https://raw.githubusercontent.com/"
    "ftrotter-gov/FederatedPayerIdentifier/main/reference_data"
)
PAYER_SYSTEMS_URL = f"{REFERENCE_DATA_BASE_URL}/current_payer_identification_systems.json"
ENDPOINT_TYPES_URL = f"{REFERENCE_DATA_BASE_URL}/endpoint_types.json"

# Optional local override directory (used for offline/pinned operation).
REFERENCE_DATA_DIR_ENV_VAR = "FPI_REFERENCE_DATA_DIR"

# Seconds to wait for the reference data HTTP request.
REFERENCE_DATA_TIMEOUT_SECONDS = 30

# Process-wide cache so that a run touching hundreds of payer files performs a
# single network fetch rather than one request per file.
_PAYER_SYSTEMS_CACHE: list[dict] | None = None

# Identifier systems whose values are only unique within a single state.
# Values in these systems MUST be prefixed with the two-letter USPS state
# code and a hyphen (e.g. "TX-68775") to prevent collisions between states.
STATE_LEVEL_SYSTEM_IDS = {"STATE_DOI_ID", "STATE_MCO_ID"}

# System IDs that may never be used as an FPI source namespace.
# (You cannot derive an FPI from another FPI.)
FPI_SOURCE_EXCLUDED_SYSTEM_IDS = {"FPI"}

# The system whose values are payer legal names that must be normalized
# (lowercased, all non a-z0-9 characters removed) before hashing.
LEGAL_NAME_HASH_SYSTEM_ID = "LEGAL_NAME_HASH"

# Pattern that state-level identifier values must match: "XX-<value>".
_STATE_PREFIX_PATTERN = re.compile(r"^[A-Z]{2}-.+$")


# ---------------------------------------------------------------------------
# Library API
# ---------------------------------------------------------------------------

def _local_reference_data_path(*, filename: str) -> str | None:
    """Return a local override path for *filename*, or None if not configured.

    Honours the FPI_REFERENCE_DATA_DIR environment variable so that this
    repository can run offline or against a pinned copy of the reference data.
    """
    override_dir = os.environ.get(REFERENCE_DATA_DIR_ENV_VAR)
    if not override_dir:
        return None
    return os.path.join(override_dir, filename)


def _read_reference_json(*, url: str, filename: str) -> dict | list:
    """Read a reference data document, preferring a local override.

    Resolution order:
      1. ``FPI_REFERENCE_DATA_DIR/<filename>`` when that variable is set.
      2. *url* on the FPI repository's ``main`` branch.
    """
    local_path = _local_reference_data_path(filename=filename)
    if local_path:
        if not os.path.exists(local_path):
            raise FileNotFoundError(
                f"FPI_maker_cli.py Error: {REFERENCE_DATA_DIR_ENV_VAR} is set, but "
                f"'{local_path}' does not exist."
            )
        with open(local_path, encoding="utf-8") as local_file:
            return json.load(local_file)

    try:
        with urllib.request.urlopen(url, timeout=REFERENCE_DATA_TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"FPI_maker_cli.py Error: could not download the payer reference data "
            f"from '{url}' ({exc}).\n"
            f"This repository reads reference data from the Federated Payer "
            f"Identifier repository's main branch and does not vendor its own "
            f"copy.  Check network access, or set {REFERENCE_DATA_DIR_ENV_VAR} to a "
            f"local directory containing '{os.path.basename(url)}'."
        ) from exc


def load_payer_systems(*, json_path: str | None = None, use_cache: bool = True) -> list[dict]:
    """
    Load the payer identifier systems list at runtime from the reference data.

    The reference data is owned by the Federated Payer Identifier repository
    and is read from its ``main`` branch:

        https://github.com/ftrotter-gov/FederatedPayerIdentifier/tree/main/reference_data

    This repository deliberately does not keep its own copy, so the approved
    list of payer identifier systems can never go stale here.

    Parameters
    ----------
    json_path : str | None
        Optional explicit path to a local
        current_payer_identification_systems.json.  When supplied, the file is
        read instead of the remote document and the cache is bypassed.
    use_cache : bool
        When True (default) the remote document is fetched once per process
        and reused.  A run that generates hundreds of FPIs therefore performs a
        single HTTP request.

    Returns
    -------
    list[dict]
        The "payer_identifier_systems" entries from the reference document.
    """
    global _PAYER_SYSTEMS_CACHE

    if json_path is not None:
        with open(json_path, encoding="utf-8") as systems_file:
            return json.load(systems_file)["payer_identifier_systems"]

    if use_cache and _PAYER_SYSTEMS_CACHE is not None:
        return _PAYER_SYSTEMS_CACHE

    systems_doc = _read_reference_json(
        url=PAYER_SYSTEMS_URL,
        filename="current_payer_identification_systems.json",
    )
    payer_systems = systems_doc["payer_identifier_systems"]

    if use_cache:
        _PAYER_SYSTEMS_CACHE = payer_systems
    return payer_systems


def load_endpoint_types(*, use_cache: bool = True) -> list[dict]:
    """Load endpoint_types.json from the FPI repository's main branch.

    Provided for callers that need the endpoint type vocabulary; it follows the
    same resolution rules as load_payer_systems().
    """
    del use_cache  # Endpoint types are not currently hot-path; always read fresh.
    return _read_reference_json(
        url=ENDPOINT_TYPES_URL,
        filename="endpoint_types.json",
    )


def get_system_namespace(*, system_id: str) -> uuid.UUID:
    """
    Return the UUID5 namespace for a given payer identifier system ID.

    Every system follows the same pattern:

        system_uuid = uuid5(NAMESPACE_DNS, "<system_id>.fhir")

    The ``.fhir`` suffix is a deliberate namespacing convention to avoid
    collisions with other uses of NAMESPACE_DNS.
    """
    return uuid.uuid5(_ROOT_NAMESPACE, f"{system_id}.fhir")


def normalize_legal_name(*, payer_legal_name: str) -> str:
    """
    Normalize a payer legal name for LEGAL_NAME_HASH hashing.

    Rule: lowercase the name, then remove every character that is not a-z
    or 0-9.  Spaces and all punctuation/special characters are removed
    entirely (not replaced).

    Examples
    --------
        "AETNA HEALTH, INC."       ->  "aetnahealthinc"
        "HUMANA INSURANCE CO"      ->  "humanainsuranceco"
        "Blue Cross & Blue Shield" ->  "bluecrossblueshield"
    """
    normalized_name = payer_legal_name.lower()
    normalized_name = re.sub(r"[^a-z0-9]", "", normalized_name)
    return normalized_name


def apply_state_prefix(*, state_code: str, payer_id_value: str) -> str:
    """
    Prefix a state-level identifier value with its two-letter USPS state code.

    Parameters
    ----------
    state_code : str
        Two-letter USPS state code, e.g. "TX".
    payer_id_value : str
        The raw identifier value assigned within that state, e.g. "68775".

    Returns
    -------
    str
        The state-prefixed value, e.g. "TX-68775".  If the value is already
        correctly prefixed with the given state code, it is returned unchanged.
    """
    normalized_state_code = state_code.strip().upper()
    if not re.fullmatch(r"[A-Z]{2}", normalized_state_code):
        raise ValueError(
            f"FPI_maker_cli.py Error: state_code must be a two-letter USPS "
            f"state code, got '{state_code}'."
        )
    if payer_id_value.startswith(f"{normalized_state_code}-"):
        return payer_id_value
    return f"{normalized_state_code}-{payer_id_value}"


def generate_fpi(*, system_id: str, payer_id_value: str) -> str:
    """
    Generate a deterministic Federated Payer Identifier (FPI) UUID5 string.

    Parameters
    ----------
    system_id : str
        One of the ``id`` values from the payer identifier systems reference
        file, e.g. ``"NAIC_ID"``.
    payer_id_value : str
        The actual identifier value within that system, e.g. ``"78700"``.
        For state-level systems (see STATE_LEVEL_SYSTEM_IDS) this value MUST
        already carry the two-letter state prefix, e.g. ``"TX-68775"``
        (see apply_state_prefix).
        For LEGAL_NAME_HASH the value is the payer legal name; it is
        automatically normalized here (lowercased, non a-z0-9 removed) before
        hashing, so raw and pre-normalized names produce the same FPI.

    Returns
    -------
    str
        A UUID5 string that is the FPI, e.g.
        ``"68d4ceb9-93f6-548c-912b-f9f43eb79683"``.

    Example
    -------
        >>> from tools.FPI_maker_cli import generate_fpi
        >>> fpi = generate_fpi(system_id="NAIC_ID", payer_id_value="78700")
        >>> print(fpi)
        68d4ceb9-93f6-548c-912b-f9f43eb79683
    """
    if system_id in FPI_SOURCE_EXCLUDED_SYSTEM_IDS:
        raise ValueError(
            f"FPI_maker_cli.py Error: system '{system_id}' cannot be used as "
            f"an FPI source namespace — you cannot derive an FPI from another FPI."
        )
    if system_id in STATE_LEVEL_SYSTEM_IDS and not _STATE_PREFIX_PATTERN.match(payer_id_value):
        raise ValueError(
            f"FPI_maker_cli.py Error: '{system_id}' is a state-level identifier "
            f"system; the value must be prefixed with the two-letter USPS state "
            f"code and a hyphen (e.g. 'TX-68775'), got '{payer_id_value}'. "
            f"Use apply_state_prefix() to build the value."
        )
    if system_id == LEGAL_NAME_HASH_SYSTEM_ID:
        payer_id_value = normalize_legal_name(payer_legal_name=payer_id_value)
    system_namespace = get_system_namespace(system_id=system_id)
    return str(uuid.uuid5(system_namespace, payer_id_value))


def get_system_by_id(*, system_id: str, payer_systems: list[dict] | None = None) -> dict | None:
    """Return the payer systems entry for *system_id*, or None if not found."""
    if payer_systems is None:
        payer_systems = load_payer_systems()
    for system in payer_systems:
        if system["id"] == system_id:
            return system
    return None


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

def _print_separator(*, char: str = "─", width: int = 60) -> None:
    print(char * width)


def _get_selectable_systems(*, payer_systems: list[dict]) -> list[dict]:
    """Return the payer systems that may be used as FPI source namespaces."""
    return [
        system for system in payer_systems
        if system["id"] not in FPI_SOURCE_EXCLUDED_SYSTEM_IDS
    ]


def _prompt_system_choice(*, payer_systems: list[dict]) -> dict:
    """
    Interactively ask the user to pick a payer identifier namespace.
    Returns the chosen system dict from the loaded payer systems.
    """
    selectable_systems = _get_selectable_systems(payer_systems=payer_systems)

    print()
    _print_separator()
    print("  FPI Maker — Federated Payer Identifier Generator")
    _print_separator()
    print()
    print("Available payer identifier namespaces:")
    print(f"(loaded from {PAYER_SYSTEMS_URL})")
    print()

    for menu_index, system in enumerate(selectable_systems, start=1):
        defunct_tag = "  [DEFUNCT]" if system.get("is_defunct") else ""
        state_tag = "  [STATE-PREFIXED]" if system["id"] in STATE_LEVEL_SYSTEM_IDS else ""
        acronym = system.get("acronym", system["id"])
        print(f"  {menu_index:>2}. {system['id']} ({acronym}){defunct_tag}{state_tag}")

    print()

    while True:
        raw = input("Select a namespace by number: ").strip()
        if not raw.isdigit():
            print("  Please enter a number.")
            continue
        choice = int(raw)
        if 1 <= choice <= len(selectable_systems):
            return selectable_systems[choice - 1]
        print(f"  Please enter a number between 1 and {len(selectable_systems)}.")


def _prompt_state_code() -> str:
    """Prompt the user for the two-letter USPS state code for a state-level system."""
    while True:
        raw = input("Enter the two-letter USPS state code (e.g. TX): ").strip().upper()
        if re.fullmatch(r"[A-Z]{2}", raw):
            return raw
        print("  Please enter exactly two letters (e.g. TX).")


def _prompt_payer_id(*, system: dict) -> str:
    """Prompt the user for the actual payer identifier value."""
    print()
    print(f"  System   : {system['id']} ({system.get('acronym', system['id'])})")
    print(f"  Authority: {system.get('assigning_authority', 'UnknownBecauseNotInReferenceData')}")
    print(f"  About    : {system.get('description', '')}")
    if system.get("is_defunct"):
        print("  ⚠️  NOTE: This identifier system is marked as DEFUNCT.")
    print()

    while True:
        raw = input(f"Enter the {system['id']} value: ").strip()
        if raw:
            break
        print("  Value cannot be empty. Please try again.")

    if system["id"] in STATE_LEVEL_SYSTEM_IDS:
        if _STATE_PREFIX_PATTERN.match(raw):
            print(f"  Value already carries a state prefix: {raw}")
            return raw
        print()
        print(f"  ⚠️  {system['id']} values are only unique within a single state.")
        print("  The value will be prefixed with the two-letter state code (e.g. 'TX-68775').")
        state_code = _prompt_state_code()
        prefixed_value = apply_state_prefix(state_code=state_code, payer_id_value=raw)
        print(f"  Using state-prefixed value: {prefixed_value}")
        return prefixed_value

    return raw


def _print_result(*, system: dict, payer_id_value: str) -> None:
    """Print the generated FPI together with the Python code needed to reproduce it."""
    system_id = system["id"]
    system_namespace = get_system_namespace(system_id=system_id)
    fpi = generate_fpi(system_id=system_id, payer_id_value=payer_id_value)

    # For LEGAL_NAME_HASH the value is normalized before hashing; show the
    # normalized value in the reproduction code so the printed code actually
    # reproduces the FPI.
    if system_id == LEGAL_NAME_HASH_SYSTEM_ID:
        normalized_value = normalize_legal_name(payer_legal_name=payer_id_value)
        if normalized_value != payer_id_value:
            print()
            print(f"  Legal name normalized for hashing: \"{payer_id_value}\" -> \"{normalized_value}\"")
        payer_id_value = normalized_value

    print()
    _print_separator()
    print("  Python code to reproduce this FPI")
    _print_separator()
    print()
    print("    import uuid")
    print()
    print(f"    system_namespace = uuid.uuid5(uuid.NAMESPACE_DNS, \"{system_id}.fhir\")")
    print(f"    # system_namespace == uuid.UUID(\"{system_namespace}\")")
    print()
    print(f"    fpi = str(uuid.uuid5(system_namespace, \"{payer_id_value}\"))")
    print()
    _print_separator()
    print("  Generated FPI")
    _print_separator()
    print()
    print(f"    {fpi}")
    print()
    _print_separator()


def _run_again() -> bool:
    """Ask whether the user wants to generate another FPI."""
    print()
    raw = input("Generate another FPI? [y/N]: ").strip().lower()
    return raw in ("y", "yes")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Interactive CLI entry point."""
    payer_systems = load_payer_systems()
    while True:
        system = _prompt_system_choice(payer_systems=payer_systems)
        payer_id_value = _prompt_payer_id(system=system)
        _print_result(system=system, payer_id_value=payer_id_value)

        if not _run_again():
            print()
            print("Goodbye.")
            print()
            break


if __name__ == "__main__":
    main()