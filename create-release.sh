#!/bin/sh

set -e

if [ ! -z "$(git status -s)" ]
then
	echo "Aborting, please commit the changes first"
	exit 1
fi

if [ ! -z "$(git clean -fdxn)" ]
then
	echo "Aborting, please remove left-over files first."
	exit 1
fi

python setup.py sdist bdist_wheel

# Use --repository testpypi for testing
python -m twine upload --repository testpypi dist/*
