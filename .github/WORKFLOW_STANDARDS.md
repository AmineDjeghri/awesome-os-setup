# GitHub Actions Workflow Standards

This repository uses a **centralized reusable workflow** approach to avoid duplicating some common steps across all workflow files.

## Architecture

### Base Reusable Workflow
All workflows use `_base-job.yaml` which defines:
- **Runner**: `ubuntu-latest` (single source of truth)
- **Python version**: `3.13` (default, can be overridden)
- Standard steps: checkout, install dependencies, run command

### How It Works

Instead of defining jobs with steps in each workflow file, we call the base workflow:

```yaml
jobs:
  my-job:
    uses: ./.github/workflows/_base-job.yaml
    with:
      job-name: 'My Job Name'
      command: 'make my-command'
      fetch-depth: 0  # optional
      python-version: '3.13'  # optional
```

## Benefits

✅ **Single source of truth** - `runs-on` is defined once in `_base-job.yaml`
✅ **Easy updates** - Change the runner in one place to update all workflows
✅ **Consistent structure** - All workflows follow the same pattern
✅ **Less duplication** - Reduced boilerplate code

## Updating the Runner

To change the runner for all workflows, edit only one file:

**File**: `.github/workflows/_base-job.yaml`

```yaml
jobs:
  run-job:
    runs-on: ubuntu-latest  # ← Change this line
```

## Current Workflows

All workflows use the base reusable workflow:
- `pre-commit.yaml` - Runs pre-commit hooks
- `tests.yaml` - Runs pytest tests
- `build-package.yaml` - Builds Python package
- `deploy-docs.yaml` - Deploys documentation to GitHub Pages
- `publish-wheel.yaml` - Publishes wheel (draft)
- `pipeline.yaml` - Orchestrates all workflows

## Adding New Workflows

To create a new workflow:

```yaml
name: My New Workflow

on:
  workflow_call:

jobs:
  my-job:
    uses: ./.github/workflows/_base-job.yaml
    with:
      job-name: 'My Job'
      command: 'make my-command'
```
