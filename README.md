# Tekniskt case - Annotation conversion

## Build package

```bash
pip install -r dev-requirements.txt
nox -s build_package
```

## Run tests

```bash
pip install -r dev-requirements.txt
nox -s build_package tests
```


## Install package

```bash
pip install -r dev-requirements.txt
nox -s build_package
pip install dist/*
```


## Run API (after installing package)
```bash
run_convert_api
```

API is hosted at address shown in terminal, e.g. `http://127.0.0.1:5000`

Endpoint is `/api` and is called with parameter payload