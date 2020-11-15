Structuring your Project
================================

Structuring the project repository into useful directories is an essential first step
in ensuring that your code stays organised and new contributors or users of your 
repository can intuitively know where to look for what.

.. toctree::
   :titlesonly:

*********************************************
Code - Test - Docs
*********************************************

Most python projects have 4 major parts:

1. Source Code
2. Tests and Benchmarks
3. Documentation
4. Configuration Files

The typical repository structuring involves keeping all your source code in a :code:`src/`
or :code:`project_name/` and all your documentation in a :code:`docs/` directory. The tests 
can either reside along side the code or be in a separate :code:`test/` directory in the 
repository root. For the tutorial repository `fakeproj <https://github.com/lazyoracle/fakeproj>`_, 
we choose the latter, as below:
::

   fakeproj/
   ├── docs
   │   └── source
   ├── fakeproj
   │   ├── fakedir
   │   └── gooddir
   └── test

The `Qiskit <https://github.com/Qiskit/qiskit-terra>`_ repository follows a similar structure:
::

   qiskit-terra/
   ├── docs
   │   ├── _static
   │   ├── _templates
   │   ├── apidocs
   │   ├── images
   │   └── source_images
   ├── examples
   │   ├── python
   │   └── qasm
   ├── qiskit
   │   ├── assembler
   │   ├── circuit
   │   ├── compiler
   │   ├── converters
   │   ├── dagcircuit
   │   ├── extensions
   │   ├── providers
   │   ├── pulse
   │   ├── qasm
   │   ├── qobj
   │   ├── quantum_info
   │   ├── result
   │   ├── scheduler
   │   ├── schemas
   │   ├── test
   │   ├── tools
   │   ├── transpiler
   │   ├── validation
   │   └── visualization
   ├── releasenotes
   │   └── notes
   ├── test
   │   ├── ipynb
   │   ├── python
   │   └── randomized
   └── tools

However, tests in `Numpy <https://github.com/numpy/numpy>`_ reside closer to the code being tested:
::

   numpy/numpy
   ├── compat
   │   └── tests
   ├── core
   │   ├── code_generators
   │   ├── include
   │   ├── src
   │   └── tests
   ├── distutils
   │   ├── checks
   │   ├── command
   │   ├── fcompiler
   │   ├── mingw
   │   └── tests
   ├── doc
   ├── f2py
   │   ├── src
   │   └── tests
   ├── fft
   │   └── tests
   ├── lib
   │   └── tests
   ├── linalg
   │   ├── lapack_lite
   │   └── tests
   ├── ma
   │   └── tests
   ├── matrixlib
   │   └── tests
   ├── polynomial
   │   └── tests
   ├── random
   │   ├── _examples
   │   ├── include
   │   ├── src
   │   └── tests
   ├── testing
   │   ├── _private
   │   └── tests
   ├── tests
   └── typing
      └── tests

This is typically a matter of style and policy. The general practice is if you wish your tests 
to be installed as a part of your library, you keep them closer to your code while if the tests
are only meant to be used for development, you keep them in a separate directory.

*********************************************
Modules and Imports
*********************************************
.. init file, relative imports

*********************************************
Configuration Files
*********************************************

There will always be various configuration files in your repository that interact with the services
you use to maintain your code. These are typically stored in the root of the directory because that is
where most services will look for these files (unless otherwise specified). We list some common ones below:

* :code:`.gitignore` - Files you don't want :code:`git` to track (`Useful gitignores <https://github.com/github/gitignore>`_)
* :code:`.pre-commit-config.yaml` - :doc:`pre-commit`
* :code:`pytest.ini` or :code:`conftest.py` - :doc:`test-coverage`
* :code:`.github/` - :doc:`ci-cd`

*********************************************
README
*********************************************
.. Best practices, badges

