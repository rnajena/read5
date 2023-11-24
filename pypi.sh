python3 -m pip install --user --upgrade setuptools wheel build
python3 -m build

python setup-ont.py sdist
python setup-ont.py bdist_wheel
twine upload dist/*