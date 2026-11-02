Repository Contents
===================

What lives where in this repository.

## Data

* [`payer_index_files/`](payer_index_files) — the trusted working copies of the
  payer well-known index files, organized by plan category. These are the
  authoritative copies maintained here, and they are what a
  [data correction request](DataCorrections.md) changes.
* [`mockup_data/`](mockup_data) and [`raw_data_sources/`](raw_data_sources) —
  curation inputs and the raw data conversion area. Material here is staging
  input, not published output.

## Code

* [`tools/`](tools) — the scripts that generate, enrich, clean, and report on
  the index files. All deterministic FPI generation lives in
  [`tools/FPI_maker_cli.py`](tools/FPI_maker_cli.py); no other tool may
  generate Federated Payer Identifiers. See [`tools/ReadMe.md`](tools/ReadMe.md)
  for the per-tool breakdown, and [RunSeed.md](RunSeed.md) for how to run them.

## Generated output

* [`reports/`](reports) — generated artifacts produced by
  [`tools/same_payer_different_plans_report.py`](tools/same_payer_different_plans_report.py).
  These are regenerated from the index files and should not be hand-edited.

## Documentation

* [`DataCorrections.md`](DataCorrections.md) — how to request a correction to
  the payer data in this repository. The submission links there are currently
  under test.
* [`ReferenceData.md`](ReferenceData.md) — where the payer identifier reference
  data comes from, how to work offline, and the normative specification
  documents.
* [`RunSeed.md`](RunSeed.md) — how to run the tests, regenerate the seed files,
  and regenerate the reports.
* [`docs/`](docs) — supporting design documents, including the
  [NPD Endpoint Feedback API](docs/npd-how-did-it-go-api.md) proposal.
* [`COMMUNITY.md`](COMMUNITY.md) — project members and their roles.
