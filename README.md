# python_tools

A reusable Python library that can be integrated into your project using either:

* **PyPI** — install the published package directly.
* **GitHub** — install the package directly from the source repository.

## Installation

### From GitHub

#### pip

Install directly from the repository:

```bash
pip install "python-tools @ git+https://github.com/jtl0079/python_tools.git@main"
```

#### `pyproject.toml`

Add the package to your project's dependencies:

```toml
[project]
dependencies = [
    "python-tools @ git+https://github.com/jtl0079/python_tools.git@main",
]
```

## Usage

After installation, import the library in your Python project:

```python
import python_tools
```
