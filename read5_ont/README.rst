Installation
------------

Pypi/pip
~~~~~~~~

.. code:: bash

   pip install read5_ont

Conda
~~~~~

Pod5 is now available via `conda <https://anaconda.org/jannessp/pod5>`__ (19.07.2023).

.. code:: bash

   conda install mamba
   mamba create -n read5_ont -c jannessp read5_ont
   conda activate read5_ont

Alternatively you can create the environment using the
`conda.recipe/env.yml <conda.recipe/env.yml>`__ file.

.. code:: bash

   conda install mamba
   mamba env create -f conda.recipe/env.yml
   conda activate read5_ont

--------------

Usage
-----

`Click here to see a full documentation about the classes and
function. <https://jannessp.github.io/read5.github.io/>`__

*my_file* can be a fast5 or pod5 file. The wrapper detects
the file format depending on the file extension.

Small example:
~~~~~~~~~~~~~~

.. code:: python

   from read5 import read # or from read5.Reader import read

   r5 = read(my_file) # file with on of these extensions: .fast5, .pod5
   for readid in r5:
       signal = r5.getSignal(readid) # returns raw integer values stored in the file
       pA_signal = r5.getpASignal(readid) # returns pA signal
       norm_signal = r5.getZNormSignal(readid) # returns normalised read signal: norm_signal = (signal - median(signal)) / mad(signal)
       channel = r5.getChannelNumber(readid)
       sampleid = r5.getSampleID(readid)
       runid = r5.getRunID(readid)

   readid_list = r5.getReads()

File Reader Classes
~~~~~~~~~~~~~~~~~~~

If you want to use the file readers you can import the corresponding
class like this:

.. code:: python

   from read5.Fast5Reader import Fast5Reader # contains the Fast5 Reader class
   from read5.Pod5Reader import Pod5Reader # contains the Pod5 Reader class

Abstract File Reader Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   from read5.AbstractFileReader import AbstractFileReader

Possible Exceptions
~~~~~~~~~~~~~~~~~~~

.. code:: python

   from read5.Exceptions import UnknownFileFormatException, UnknownNormalizationMode

-  UnknownFileFormatException: is raised, when the file extension does
   not match one of [‘.fast5’, ‘.pod5’]
-  UnknownNormalizationMode: is raised, when an unknown mode is provided
   for the signal normalization function

Full Documentation
------------------

Created with `pdoc3 <https://pdoc3.github.io/pdoc/>`__. Can be found
`here <https://jannessp.github.io/read5.github.io/>`__.
