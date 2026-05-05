# Quick Start Guide

## Who this guide is for

This guide is for first-time users who want to quickly try Anburan InsolePrint Open Edition.

It is a good fit for:
- makers and hobbyists
- people with basic terminal experience
- non-professional developers who want a simple first run

## What you need before starting

Before you begin, make sure you have:
- Python 3.10 or newer
- Git (or a downloaded ZIP of this repository)
- basic terminal access
- slicer software if you want to inspect or print the generated STL

## Step 1: Download or clone the repository

You can either:
- clone with Git, or
- download this repository as a ZIP and extract it

If you use Git:

```bash
git clone https://github.com/anburan-tech/anburan-insoleprint-open-edition.git
cd anburan-insoleprint-open-edition
```

## Step 2: Open a terminal in the project folder

If you downloaded a ZIP, open a terminal in the extracted `anburan-insoleprint-open-edition` folder.

If you cloned with Git, run:

```bash
cd anburan-insoleprint-open-edition
```

## Step 3: Run the sample command

Run:

```bash
python -m app.cli --input examples/sample_input.json --output examples/sample_output.json --stl examples/sample_insole.stl
```

## Step 4: Find the generated files

After the command finishes, you should see:
- `examples/sample_output.json`
- `examples/sample_insole.stl`

## Step 5: Open the STL in slicer software

Open `examples/sample_insole.stl` in your slicer to inspect it and prepare a print if you want.

## Step 6: Submit feedback through GitHub Issues

If anything is unclear, or you want to share results, open an Issue on GitHub.

Your feedback helps improve documentation and first-time setup.

---

This project is for everyday footwear fit exploration and 3D printing experimentation.
It is not for medical, clinical, orthotic, or therapeutic use.
