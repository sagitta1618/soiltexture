#!/bin/bash
# build the python package for pypi

# compile source distribution
python3 setup.py sdist bdist_wheel
# only the source distribution allows to run post install script to download binaries

#python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#python3 -m twine upload dist/*
