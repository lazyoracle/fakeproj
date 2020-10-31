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

There are markers for individual modules from the library, eg, 

```bash
pytest -v -m "goodmodule" --cov=fakeproj test/
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

* Unit Testing (Python 3.6, 3.7, 3.8 on ubuntu:latest)  ![unit test](https://github.com/lazyoracle/fakeproj/workflows/Unit%20Testing/badge.svg)
* Code Coverage   ![coverage](https://github.com/lazyoracle/fakeproj/workflows/Code%20Coverage/badge.svg)
* Code Complexity (Maximum CC of B/B/A)  ![complexity test](https://github.com/lazyoracle/fakeproj/workflows/Code%20Complexity/badge.svg)
* Build Testing (Python 3.6, 3.7, 3.8 on {ubuntu, macos, windows}:latest)  ![build test](https://github.com/lazyoracle/fakeproj/workflows/Python%20package%20Build/badge.svg)

### Code Formatting

This project uses <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
