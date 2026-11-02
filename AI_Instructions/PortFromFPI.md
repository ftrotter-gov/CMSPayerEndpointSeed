Port from FPI repo
==============

This repo contains the CMS payer endpoint seed, which used to be a project that was stored inside the Federated Payer Identifier GitHub repo. I've opened that separate repo in the same scope so that you can see it.
If you look under tools, you'll see the system that generates the various artifacts. In general, the links to the reference data should remain in the Federated PID identifier repo.
The docs should be migrated over:
- everything in docs
- everything in the mock data folder
- everything in pair_index_files
- everything under raw data sources
- everything under reports
However, the reports are a generated artifact, so we should just migrate the tools directory, and then that should work.