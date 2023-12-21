### Hexlet tests and linter status:
[![Actions Status](https://github.com/Roodmann/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Roodmann/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/08a3050c6398933601a6/maintainability)](https://codeclimate.com/github/Roodmann/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/08a3050c6398933601a6/test_coverage)](https://codeclimate.com/github/Roodmann/python-project-50/test_coverage)
[![Python CI](https://github.com/Roodmann/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Roodmann/python-project-50/actions/workflows/pyci.yml)




# **Gendiff** - compare two json and/or yaml files
This utility calculate differences between 2 files in json or yaml format. Differences can be represented by 3 formats.

## Description

- stylish format. Shows all keys and values ​​from the first and      second files, the status of the key is marked with a plus or minus, depending on whether it was added or removed. 
- plain format. Data about keys and their status is displayed as strings. If the key is not modified in any way, the nested keys are displayed as '[complex value]'.
- json format. Difference between two files is shown by json format


## System requirements

- Python (3.10)
- Poetry
- GIT
- Pyyaml (6.0.1)

### Installation
To install and run the project, you will need Python version 3.10 and higher.

```
pip install --user git+https://github.com/Roodmann/python-project-50
```
### Get diffrence between two json files

[Demonstration](https://asciinema.org/a/qDgGUfPEGNTQflKTUQZNsvyir)