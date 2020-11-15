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

Most projects have 4 major parts:

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
   .
   .
   .
   │   └── source_images
   ├── examples
   │   ├── python
   │   └── qasm
   ├── qiskit
   │   ├── assembler
   .
   .
   .
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
   .
   .
   .
   ├── fft
   │   └── tests
   ├── lib
   │   └── tests
   .
   .
   .
   └── typing
      └── tests

This is typically a matter of style and policy. The general practice is if you wish your tests 
to be installed as a part of your library, you keep them closer to your code while if the tests
are only meant to be used for development, you keep them in a separate directory.

*********************************************
Packages, Modules and Imports
*********************************************

When working on a large project, you typically want to convert your python scripts to modules and packages 
that can be imported and reused elsewhere in the code. For the tutorial repository this looks as below:
::

   fakeproj/fakeproj/
   ├── __init__.py
   ├── fakedir
   │   ├── __init__.py
   │   └── fakemodule.py
   └── gooddir
      ├── __init__.py
      ├── goodmodule.py
      └── sysmodule.py

The :code:`__init__.py` is the magic ingredient that allows you to convert your Python modules into packages
that can now be imported and used from other directories. In the simplest case, :code:`__init__.py` can just be an empty file, 
but it can also execute initialization code for the package or set the :code:`__all__` variable. The `Python Packages Documentation
<https://docs.python.org/3/tutorial/modules.html#packages>`_ describes this in further details.

A related topic that often confuses new developers working with packages and modules in Python is how the interpretor deals with
Imports - both relative and absolute. We list below some useful resources that address the usual confusions:

* `Relative imports for the billionth time - Stackoverflow <https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time>`_
* `Python PEP 328: import and build package <https://jingwen-z.github.io/python-pep-328-import-and-build-package/>`_

*********************************************
Configuration Files
*********************************************

There will always be various configuration files in your repository that interact with the services
you use to maintain your code. These are typically stored in the root of the directory because that is
where most services will look for these files (unless otherwise specified). Some of these files can also
be combined in the form of :code:`.toml` files, but it is usually advisable to have separate configuration
files for the different services used. We list some common ones below:

* :code:`.gitignore` - Files you don't want :code:`git` to track (`Useful gitignores <https://github.com/github/gitignore>`_)
* :code:`.pre-commit-config.yaml` - :doc:`pre-commit`
* :code:`pytest.ini` or :code:`conftest.py` - :doc:`test-coverage`
* :code:`.github/` - :doc:`ci-cd`

*********************************************
README
*********************************************

The :code:`README.md` is essentially the front page to your repository and it is imperative that you provide
a concise and useful introduction to your project while providing instructions for using and/or contributing
to the code base. Below are some of the useful features that are nice to have in an 
`Awesome README <https://github.com/matiassingers/awesome-readme>`_ :

* Clear description of what the project does
* Table of Contents for easy navigation
* Step-by-Step installation and setup sections 
* Overview of features
* Instructions for Contribution
* Demo screenshot or GIF
* Code snippets demonstrating common features/functionality
* API Overview where applicable
* Badges for stats
* FAQ for common usage and troubleshooting points
* Instructions on filing bugs/feature requests and getting support
* List of Alternatives
* Link to Documentation
* Link to Project Website
* Bibtext for citing the project
* References for further reading
* Contact details - Email or Mailing List or Gitter/Slack
