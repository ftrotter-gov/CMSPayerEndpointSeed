Running the Tools
===================

How to validate, regenerate the seed files, and regenerate the reports.

## Requirements

The tools are standard-library-only Python 3 and have no third-party
dependencies. There is nothing to install.

Most tools read the payer identifier reference data over the network at
runtime. See [ReferenceData.md](ReferenceData.md) for what is fetched and how
to work offline.

Run all commands from the repository root.

## Commands

```bash
python3 -m unittest discover -s tools/tests          # validate FPI generation
python3 tools/seed_medicare_advantage/seed.py        # (re)generate seed files
python3 tools/same_payer_different_plans_report.py   # regenerate reports
```

### Validate FPI generation

```bash
python3 -m unittest discover -s tools/tests
```

Runs the test suite in [`tools/tests/`](tools/tests). Run this before and after
any change to [`tools/FPI_maker_cli.py`](tools/FPI_maker_cli.py), since all
deterministic Federated Payer Identifier generation goes through that module.

### Regenerate the seed files

```bash
python3 tools/seed_medicare_advantage/seed.py
```

Regenerates the Medicare Advantage well-known index files into
[`payer_index_files/`](payer_index_files).

### Regenerate the reports

```bash
python3 tools/same_payer_different_plans_report.py
```

Regenerates the artifacts in [`reports/`](reports). Those files are generated
output — regenerate them rather than editing them by hand.

## Reviewing the results

These tools rewrite files in place, and git history is the current audit and
recovery mechanism. Check `git diff` after a run and commit deliberately, so an
unintended rewrite does not get mixed into an unrelated change.

See [`tools/ReadMe.md`](tools/ReadMe.md) for the per-tool breakdown and the
current limitations of this tooling.
