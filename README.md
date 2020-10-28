# fakeproj

A dummy project to test python code quality tools

## Installation

```bash
pip install . 
```

### Developer Setup

```bash
pip install -r requirements.txt
```

### Testing

This project uses [`pytest`](https://docs.pytest.org/en/latest/) for testing. 

```bash
pytest -s -v --cov=fakeproj test/
```

### Complexity

```bash
radon cc -a .
xenon --max-absolute B --max-modules B --max-average A .
```

### Docstrings

```bash
docstr-coverage .
```

### GitHub Actions

* Integration Testing (Python 3.6, 3.7, 3.8 on Ubuntu:latest)
* Code Coverage
* Code Complexity (Maximum CC of B/B/A)
* Build Testing (Python 3.6, 3.7, 3.8 on {ubuntu, macos, windows}:latest)

### Code Formatting
This project uses [`black`](https://black.readthedocs.io/en/stable/) for code styling. 
