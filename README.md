# CMS Payer Endpoint Seed

This is the github repo where CMS is developing the data that will be published in the Preview Edition of the [National Provider Directory](https://directory.cms.gov). 

Please contact Fred Trotter through the [CMS Health Tech Ecosystem](https://www.cms.gov/initiatives/health-technology-ecosystem/overview) for access.

The initial version of this repo is a port from the same functionality previously stored in the [Federated Payer Identifier](https://github.com/ftrotter-gov/FederatedPayerIdentifier) repo.

## Understanding the data format

The .well-known file format used to model payer data in this model is intended to be compatible with the data structures defined for Payers, Plans, Networks and Endpoints in the [FAST FHIR NDH IG Standard](https://build.fhir.org/ig/HL7/fhir-us-ndh/en/resourceRelationship.html). 

It is enough data to programatically route from a health insurance card (physicial or digital) to the correct Payer Endpoints associated with those cards.

Please read about the [.well-known data format on the FederatedPayerIdentfier repo](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/WellKnownFileFormat.md).


## Correcting Payer Data

If you are NOT the payer in question you can submit [general Data Correction Request pull request here](REPLACEME)

If you ARE the payer in question you should submit a [Payer Data Correction Request](REPLACEME)



## Contents

* [`payer_index_files/`](payer_index_files) — the trusted working copies of the
  payer well-known index files, organized by plan category.
* [`tools/`](tools) — the scripts that generate, enrich, clean, and report on
  those index files. All deterministic FPI generation lives in
  `tools/FPI_maker_cli.py`.
* [`reports/`](reports) — generated artifacts produced by
  `tools/same_payer_different_plans_report.py`.
* [`docs/`](docs) — supporting design documents, including the
  [NPD Endpoint Feedback API](docs/npd-how-did-it-go-api.md) proposal.
* [`mockup_data/`](mockup_data) and [`raw_data_sources/`](raw_data_sources) —
  curation inputs and the raw data conversion area.

## Reference data

This repository does **not** keep its own copy of the payer identifier
reference data. That data is owned by the Federated Payer Identifier repository
and is read at runtime from its `main` branch:

<https://github.com/ftrotter-gov/FederatedPayerIdentifier/tree/main/reference_data>

`tools/FPI_maker_cli.py` downloads
`current_payer_identification_systems.json` from that location and caches it
for the life of the process, so the approved list of payer identifier systems
can never go stale here. Running the tools therefore requires network access.
To work offline, or to pin a specific revision, set the
`FPI_REFERENCE_DATA_DIR` environment variable to a local directory containing
that file:

```bash
export FPI_REFERENCE_DATA_DIR=/path/to/reference_data
```

## Specification documents

The normative specification documents remain in the
[Federated Payer Identifier](https://github.com/ftrotter-gov/FederatedPayerIdentifier)
repository:

* [Federated Payer Identifier Specification](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/FederatedPayerIdentifierSpecification.md)
* [Generating Federated Payer Identifiers](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/GeneratingFederatedPayerIdentifiers.md)
* [Payer well-known index format](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/WellKnownFileFormat.md)
* [All-at-once provider directory downloads](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/AllAtOnce.md)
* [Future steps](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/FutureSteps.md)

## Running the tools

The tools are standard-library-only Python 3 and have no third-party
dependencies.

```bash
python3 -m unittest discover -s tools/tests          # validate FPI generation
python3 tools/seed_medicare_advantage/seed.py        # (re)generate seed files
python3 tools/same_payer_different_plans_report.py   # regenerate reports
```


## Policies

### Open Source Policy

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.


### Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
