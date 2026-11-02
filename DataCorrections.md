Correcting Payer Data
===================

This document explains how to request a correction to the payer data published
in this repository. It is an information quality request for correction under
the CMS Information Quality Guidelines.

**The submission links below are meant to be clicked on GitHub.** They open
GitHub's pull request compare page, so they will not do anything useful from a
local file viewer.

## Is this the right place?

| Your situation | Where to go |
| :------------- | :---------- |
| Payer data that lives in this repository | Continue with this document |
| National Provider Directory data that is NOT payer data and is NOT in this repository | Use the **Feedback** button on [directory.cms.gov](https://directory.cms.gov) |
| General data quality requests unrelated to the National Provider Directory | Email [infoquality@cms.hhs.gov](mailto:infoquality@cms.hhs.gov) |

## Which template should I use?

There are two pull request templates. Pick based on your relationship to the
payer whose data is wrong.

* **You are NOT the payer** — use the *general* data correction template. It
  asks why the data is in error, what it should say, and how the error affects
  you.
* **You ARE the payer** (or you represent them) — use the *payer* data
  correction template. It asks what the data should say, your relationship to
  the payer, and the location of your own `.well-known` file.

Please make sure your public GitHub profile has appropriate contact
information. We may not be able to process requests from users we cannot
contact.

## How to submit

First, [fork this repository](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/fork)
and commit your proposed data change to a branch in your fork. See the
[payer well-known index format](https://github.com/ftrotter-gov/FederatedPayerIdentifier/blob/main/WellKnownFileFormat.md)
for documentation of the file format you are editing.

Then open a pull request using one of the links below.

### If you are reading this on your own fork

These relative links open the compare page on *your* fork. GitHub defaults the
base repository of a fork's pull request to the upstream parent, so they point
back at this repository automatically — you only need to choose your branch in
the **compare** drop-down.

* [General Data Correction Request](../../compare?template=general-data-quality-correction.md)
* [Payer Data Correction Request](../../compare?template=payer-data-quality-correction.md)

### If you are reading this on the main repository

These absolute links open the compare page here. Click **compare across forks**
and select your fork and branch.

* [General Data Correction Request](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare?template=general-data-quality-correction.md)
* [Payer Data Correction Request](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare?template=payer-data-quality-correction.md)

### If you have already pushed your branch

You can skip the drop-downs entirely by editing the URL directly. Replace
`YOUR-USERNAME` and `YOUR-BRANCH`, and use whichever template name applies:

```
https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare/main...YOUR-USERNAME:CMSPayerEndpointSeed:YOUR-BRANCH?quick_pull=1&template=payer-data-quality-correction.md
```

## If a link does not work

If one of the links above returns a **404**, open a pull request the normal way
from your fork and choose the template manually by appending
`?template=payer-data-quality-correction.md` (or
`general-data-quality-correction.md`) to the compare URL.

A maintainer will apply the `data_correction` label and assign the request
during triage. Most contributors do not have permission to set labels or
assignees themselves, and GitHub returns a 404 rather than ignoring query
parameters the viewer is not allowed to use.

## What happens next

The request is reviewed against the data in this repository and against the
source data it was derived from. Corrections that are accepted are merged into
the `payer_index_files/` trusted working copies and flow into the Preview
Edition of the [National Provider Directory](https://directory.cms.gov).
