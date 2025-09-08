# GitHub Actions Pipeline Assignment

![Python CI](https://github.com/kunal-purohit/github-actions-pipeline/actions/workflows/main.yml/badge.svg)

This repository demonstrates a Python project with automated testing using GitHub Actions.

## Overview

-   The project contains `app.py` with basic utility functions.
-   Tests are located in the `tests/` directory and are executed using `pytest`.

## GitHub Actions Pipeline

We have set up a GitHub Actions workflow that automatically runs tests on every push or pull request to the `main` branch.

### Workflow Details

-   **Workflow file**: `.github/workflows/main.yml`
-   **Trigger**:
    -   On `push` to `main`
    -   On `pull_request` targeting `main`
-   **Steps**:
    1. Checkout repository code.
    2. Set up Python 3.x environment with pip caching enabled.
    3. Install dependencies from `requirements.txt`.
    4. Run all tests using `pytest`.
