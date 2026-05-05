# Anburan InsolePrint Open Edition (v0.1)

Anburan InsolePrint Open Edition is an **independent open-source edition** for everyday footwear fit exploration and 3D printing experimentation.

New here? Start with [QUICK_START.md](QUICK_START.md).

It is designed for:
- personal users
- makers and hobbyists
- small studios
- footwear/insole developers
- 3D printing practitioners

## What this project is

This repository provides a lightweight CLI workflow that:
- accepts simple manual foot measurements
- applies transparent non-medical comfort-oriented heuristics
- generates a **basic placeholder insole-like STL**
- estimates basic personal print readiness
- writes a concise JSON result

## What v0.1 can do

- Validate structured input JSON.
- Produce a basic insole-like placeholder mesh for printer testing.
- Return simple fit notes and caution flags.
- Estimate print time/readiness with straightforward assumptions.

## What v0.1 cannot do

- Not suitable for medical, clinical, orthotic, or therapeutic use.
- Does not provide diagnosis, treatment, correction, orthotic prescription, clinical recommendation, therapeutic advice, or medical recommendation.
- Does not provide biomechanical correction logic.
- Does not support commercial fitting claims.
- Does not include internal or proprietary Anburan systems or confidential rules.
- Does not include web app/cloud/database/authentication features.

## Non-medical boundary

This software is **not a medical device** and **not a diagnostic tool**.
Use it only for everyday footwear fit exploration and 3D printing experimentation.

## Installation

Requirements:
- Python 3.10+

```bash
python -m pip install -U pip
```

## Run the CLI

See also: [docs/input-guide.md](docs/input-guide.md) for a field-by-field explanation of the sample input.

```bash
python -m app.cli --input examples/sample_input.json --output examples/sample_output.json --stl examples/sample_insole.stl
```

The CLI will:
1. validate input
2. apply simple transparent rules
3. generate STL
4. write output JSON
5. print terminal summary

## Run tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Feedback

Please test cautiously and submit feedback through repository issues using templates in `feedback/`:
- `feedback/issue_template.md`
- `feedback/field_test_template.md`

Helpful feedback includes printer setup, print outcome, and plain-language comfort observations.

## Public release readiness

- **Current status:** v0.1 scaffold
- **Intended users:** personal users, makers, small studios, and 3D printing practitioners
- **Not for:** medical, clinical, orthotic, therapeutic, or commercial fitting claims
- Users should test cautiously and submit feedback through Issues

## Contributing and feedback

- See [CONTRIBUTING.md](CONTRIBUTING.md)
- See [SECURITY.md](SECURITY.md)
- Open [GitHub Issues](../../issues)
- Review [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md)
