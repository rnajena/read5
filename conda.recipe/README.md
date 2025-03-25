# Run
```bash
VERSION=`hatch version` conda mambabuild conda.recipe/
conda convert --platform osx-64 /path/to/package.tar.bz2 -o outputdir/
anaconda upload /paths/to/packages
```