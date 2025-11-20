# YAMSPy Developer Guide

This guide provides instructions on how to set up your development environment for YAMSPy.

## Prerequisites

- Python 3.7+
- Git

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ikatrechko/YAMSPy.git
    cd YAMSPy
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    ```bash
    # On Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    Install the project in editable mode along with the test dependencies.
    ```bash
    pip install -e .[test]
    ```

## Running Tests

To ensure everything is working correctly, run the test suite using `pytest`:
```bash
pytest
```

## Building the Project

To build the source archive and wheel for distribution, use the `build` package:
```bash
pip install build
python -m build
```
The distributable packages will be created in the `dist/` directory.