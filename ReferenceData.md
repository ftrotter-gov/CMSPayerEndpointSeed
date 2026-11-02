Reference Data and Specifications
===================

Where the payer identifier reference data comes from, and where the normative
specifications live. Neither is maintained in this repository.

## Reference data

This repository does **not** keep its own copy of the payer identifier
reference data. That data is owned by the Federated Payer Identifier repository
and is read at runtime from its `main` branch:

<https://github.com/ftrotter-gov/FederatedPayerIdentifier/tree/main/reference_data>

`tools/FPI_maker_cli.py` downloads
`current_payer_identification_systems.json` from that location and caches it
for the life of the process, so the approved list of payer identifier systems
can never go stale here. Running the tools therefore requires network access.

### Working offline

To work offline, or to pin a specific revision, set the
`FPI_REFERENCE_DATA_DIR` environment variable to a local directory containing
that file:

```bash
export FPI_REFERENCE_DATA_DIR=/path/to/reference_data
```

See [RunSeed.md](RunSeed.md) for running the tools that consume this data.

## Specification documents

The normative specification documents remain in the
[Federated Payer Identifier](https://github.com/ftrotter-gov/FederatedPayerIdentifier)
repository:

* [Federated Payer Identifier Specification](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/FederatedPayerIdentifierSpecification.md)
* [Generating Federated Payer Identifiers](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/GeneratingFederatedPayerIdentifiers.md)
* [Payer well-known index format](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/WellKnownFileFormat.md)
* [All-at-once provider directory downloads](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/AllAtOnce.md)
* [Future steps](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/FutureSteps.md)
