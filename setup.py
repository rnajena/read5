from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
    'python>=3.0',
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
    packages=['read5'],
    
    install_requires=requirements,
    keywords='Read5',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
