# Python Project Template Readm

## Introduction

## Usage

Create a virtual env and activate it:

```bash
python -m venv .env
.\.env\Scripts\activate
```

Use with cookiecutter. First install cookiecutter and pipx:

```bash
pip install pipx
```

run cookiecutter with

```bash
pipx run cookiecutter https://github.com/stkr22/cookiecutter-python-project
```

The project root directory already exist(e.g. you cloned an existing remote repository)? Just go to the root folder of where the repository is located and:

```bash
pipx run cookiecutter -f https://github.com/stkr22/cookiecutter-python-project
```

This will overwrite the existing folder with the template. 
