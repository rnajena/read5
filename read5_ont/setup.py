from setuptools import setup, find_packages
import versioneer

requirements = [
    'h5py>=3.0',
    'vbz-h5py-plugin>=1.0',
    'numpy>=1.20',
    'pod5>=0.2.3',
]

with open("README.rst", "r") as rst:
    long_description = rst.read()

setup(
    name='read5_ont',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Wrapper to read fast5 and pod5 files.",
    long_description=long_description,
    license="GNU General Public License v3",
    author="Jannes Spangenberg",
    author_email='jannes.spangenberg@uni-jena.de',
    url='https://github.com/JannesSP/read5',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=requirements,
    keywords=['read5', 'fast5', 'pod5', 'ONT', 'Oxford Nanopore Technologies', 'Nanopore', 'raw data', 'wrapper'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ]
)