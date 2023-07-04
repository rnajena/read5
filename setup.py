from setuptools import setup, find_packages
import versioneer

requirements = [
    # package requirements go here
    'h5py>=3.0',
    'ont_vbz_hdf_plugin>=1.0',
    'pyslow5>=1.0.0',
    'numpy',
    # 'pod5' # currently only avaible via pipy
]

setup(
    name='Read5',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Wrapper to read fast5, slow5, blow5 and pod5 files.",
    license="GNUv3",
    author="Jannes Spangenberg",
    author_email='jannes.spangenberg@uni-jena.de',
    url='https://github.com/JannesSP/Read5',
    packages=find_packages(),
    
    install_requires=requirements,
    keywords=['Read5', 'slow5', 'blow5', 'fast5', 'pod5', 'ONT', 'Oxford Nanopore Technologies', 'Nanopore', 'raw data'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
