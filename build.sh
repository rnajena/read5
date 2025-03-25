python3 -m pip install --user --upgrade setuptools wheel build
python3 -m build
twine upload dist/*