from setuptools import setup, find_packages
import versioneer

requirements = [
    # package requirements go here
    'h5py>=3.0',
    # 'ont_vbz_hdf_plugin>=1.0',
    'vbz-h5py-plugin>=1.0', # same as ont_vbz but in pipy
    'pyslow5>=1.0',
    'numpy',
    'pod5>=0.2.3', # currently only avaible via pipy
]

with open("README.rst", "r") as rst:
    long_description = rst.read()

setup(
    name='read5',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Wrapper to read fast5, slow5, blow5 and pod5 files.",
    long_description=long_description,
    license="GNU General Public License v3",
    author="Jannes Spangenberg",
    author_email='jannes.spangenberg@uni-jena.de',
    url='https://github.com/JannesSP/read5',
    packages=find_packages(),
    install_requires=requirements,
    keywords=['read5', 'slow5', 'blow5', 'fast5', 'pod5', 'ONT', 'Oxford Nanopore Technologies', 'Nanopore', 'raw data', 'wrapper'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)