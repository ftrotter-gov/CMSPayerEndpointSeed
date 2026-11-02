Correcting Payer Data
===================

This document explains how to request a correction to the payer data published
in this repository. It is an information quality request for correction under
the CMS Information Quality Guidelines.

**The submission links below are meant to be clicked on GitHub.** They open
GitHub's pull request form, so they will not do anything useful from a local
file viewer.

## Is this the right place?

| Your situation | Where to go |
| :------------- | :---------- |
| Payer data that lives in this repository | Continue with this document |
| National Provider Directory data that is NOT payer data and is NOT in this repository | Use the **Feedback** button on [directory.cms.gov](https://directory.cms.gov) |
| General data quality requests unrelated to the National Provider Directory | Email [infoquality@cms.hhs.gov](mailto:infoquality@cms.hhs.gov) |

## Submission links — under test

> **We are testing which of these work.** Click one. It should open a pull
> request form that is already filled in. Nothing to copy, paste, edit, or
> delete. If a link does not behave that way, tell us which one.

All three open a pull request against the `data-correction-start` branch, which
exists only to give the link a real diff to work with. Replace its contents
with your actual correction.

### Method 1 — Title and body carried in the link

[**Open a data correction pull request**](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare/main...data-correction-start?quick_pull=1&title=Payer%20data%20correction&body=%23%23%23%20What%20data%20is%20wrong%0A%0A%0A%23%23%23%20What%20it%20should%20say%0A%0A%0A%23%23%23%20Your%20relationship%20to%20this%20payer%20and%20how%20to%20verify%0A%0A%0A---%0ASubmitted%20under%20the%20CMS%20Information%20Quality%20Guidelines.%0A)

The title and body travel inside the URL itself, so no template file has to
resolve.

### Method 2 — Repository default template

[**Open a data correction pull request**](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare/main...data-correction-start?quick_pull=1)

No query parameters beyond opening the form. The body comes from the
repository's default pull request template.

### Method 3 — Title, body, label, and assignee

[**Open a data correction pull request**](https://github.com/ftrotter-gov/CMSPayerEndpointSeed/compare/main...data-correction-start?quick_pull=1&title=Payer%20data%20correction&body=%23%23%23%20What%20data%20is%20wrong%0A%0A%0A%23%23%23%20What%20it%20should%20say%0A%0A%0A%23%23%23%20Your%20relationship%20to%20this%20payer%20and%20how%20to%20verify%0A%0A%0A---%0ASubmitted%20under%20the%20CMS%20Information%20Quality%20Guidelines.%0A&labels=data_correction&assignees=ftrotter-gov)

Same as Method 1, plus the `data_correction` label and an assignee. This is
expected to fail with a 404 for anyone without write access, which is most
people. It is here to confirm whether that is true.
