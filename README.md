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

* Integration Testing (Python 3.6, 3.7, 3.8 on Ubuntu:latest)  ![integration test](https://github.com/lazyoracle/fakeproj/workflows/Integration%20Testing/badge.svg)
* Code Coverage   ![coverage](https://github.com/lazyoracle/fakeproj/workflows/Code%20Coverage/badge.svg)
* Code Complexity (Maximum CC of B/B/A)  ![complexity test](https://github.com/lazyoracle/fakeproj/workflows/Code%20Complexity/badge.svg)
* Build Testing (Python 3.6, 3.7, 3.8 on {ubuntu, macos, windows}:latest)  ![build test](https://github.com/lazyoracle/fakeproj/workflows/Python%20package%20Build/badge.svg)

### Code Formatting

This project uses [`black`](https://black.readthedocs.io/en/stable/) for code styling.
