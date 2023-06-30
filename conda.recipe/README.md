# Run
```
for i in 8 9 10 11; do conda mambabuild conda.recipe/ --python 3.$i; done
conda convert --platform osx-64 /path/to/package.tar.bz2 -o outputdir/
```