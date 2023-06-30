# Run
```
conda mambabuild conda.recipe/ --variants "{python: [3.8, 3.9, 3.10, 3.11]}"
conda convert --platform osx-64 /path/to/package.tar.bz2 -o outputdir/
```