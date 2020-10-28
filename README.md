# fakeproj

A dummy project to test python code quality tools

## Usage

### Testing

```bash
pytest -s -v -cov=fakeproj test/
```

### Complexity

```bash
radon cc -a .
```

### Docstrings

```bash
docstr-coverage .
```

### GitHub Actions
