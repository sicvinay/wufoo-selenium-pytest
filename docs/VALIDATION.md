# Validation

Local validation on 16 November 2026, Python 3.12/Linux:

- 40 algorithm and configuration tests passed.
- Eight Selenium UI cases and one opt-in live case collect successfully.
- Every authored Python file parses successfully.
- Exact historical login strings were checked against the clean source and removed.
- A local Chrome startup probe failed with SessionNotCreatedException; no local
  browser-pass claim is made. GitHub Actions runs the real UI tests independently.
- Live Wufoo login was not attempted and no original credentials were used.

The CI workflow runs the 48 non-live cases with two parallel workers on Python
3.12, 3.13 and 3.14 and uploads HTML/JUnit reports. Demo UI success does not
validate the real Wufoo service or the current live account login selectors.
