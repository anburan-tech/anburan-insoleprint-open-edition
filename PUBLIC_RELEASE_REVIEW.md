# Public Release Review — Anburan InsolePrint Open Edition v0.1

## 1. Current status
- Repository remains Private
- v0.1 scaffold completed
- Release-readiness infrastructure added
- LICENSE completed with full AGPL-3.0 text

## 2. Verified assets
- [x] `app/`
- [x] `core_open/`
- [x] `docs/`
- [x] `examples/`
- [x] `feedback/`
- [x] `tests/`
- [x] `.github/workflows/tests.yml`
- [x] `.github/ISSUE_TEMPLATE/`
- [x] `LICENSE`
- [x] `README.md`
- [x] `TRADEMARK.md`
- [x] `CONTRIBUTING.md`
- [x] `SECURITY.md`
- [x] `PUBLIC_RELEASE_CHECKLIST.md`

## 3. License and trademark boundary
- LICENSE includes full GNU AGPL-3.0 text (Version 3, 19 November 2007), including "END OF TERMS AND CONDITIONS" and "How to Apply These Terms to Your New Programs".
- Trademark boundary is explicitly separated: "Anburan", "安步然", logos, visual identity, and other brand assets are not granted for commercial use solely through open-source code licensing.

## 4. Non-medical boundary
This project is limited to everyday footwear fit exploration and personal 3D printing experimentation. It is not a medical device and does not provide diagnosis, treatment, correction, orthotic prescription, clinical recommendation, therapeutic advice, or medical recommendation.

## 5. Internal asset audit
Repository-wide text audit found no internal Anburan Core logic, ABI/ADFS internal standards implementations, material compensation rules, commercial Print Profiles, partner documents, or real user data. Existing references are boundary/negative statements only.

## 6. Test results
- Unit tests: `python -m unittest discover -s tests -p 'test_*.py' -v` → Passed.
- CLI smoke test: `python -m app.cli --input examples/sample_input.json --output examples/sample_output.json --stl examples/sample_insole.stl` → Passed.

## 7. Remaining blockers before making public
No release blockers found. Human approval is still required before switching repository visibility to Public.

## 8. Final recommendation
Ready for human approval before Public
