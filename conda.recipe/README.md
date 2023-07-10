# Run
```bash
conda mambabuild conda.recipe/ -m conda.recipe/conda_build_config.yaml
conda convert --platform osx-64 /path/to/package.tar.bz2 -o outputdir/
```