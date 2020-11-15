# fakeproj: DevOps for Dummies

![unit test](https://github.com/lazyoracle/fakeproj/workflows/Unit%20Testing/badge.svg)
![integration test](https://github.com/lazyoracle/fakeproj/workflows/Integration%20Testing/badge.svg)
![coverage](https://github.com/lazyoracle/fakeproj/workflows/Code%20Coverage/badge.svg)
[![codecov](https://codecov.io/gh/lazyoracle/fakeproj/branch/master/graph/badge.svg)](https://codecov.io/gh/lazyoracle/fakeproj)
![complexity test](https://github.com/lazyoracle/fakeproj/workflows/Code%20Complexity/badge.svg)
![build test](https://github.com/lazyoracle/fakeproj/workflows/Python%20package%20Build/badge.svg)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Documentation Status](https://readthedocs.org/projects/fakeproj/badge/?version=latest)](https://fakeproj.readthedocs.io/en/latest/?badge=latest)

A dummy project to introduce various DevOps tools and Best Practices to Python developers. Follow along with the tutorial on [fakeproj.readthedocs.io](https://fakeproj.readthedocs.io)

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

* Unit Testing (Python 3.6, 3.7, 3.8 on ubuntu:latest)
* Code Coverage
* Code Complexity (Maximum CC of B/B/A)
* Build Testing (Python 3.6, 3.7, 3.8 on {ubuntu, macos, windows}:latest)

### Code Formatting

This project uses [Black](https://black.readthedocs.io/en/stable/) for Code Formatting

## To-Do

- [ ] Integration Testing
- [ ] Populate Docs
- [ ] Git Tags and Releases
- [ ] Packaging and Deployment
