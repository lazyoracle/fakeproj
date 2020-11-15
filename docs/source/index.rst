.. fakeproj documentation master file, created by
   sphinx-quickstart on Wed Nov  4 06:44:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

fakeproj: DevOps for Dummies
======================================

This documentation is intended to serve as a self-paced tutorial to familiarise Python developers with various tools 
that can help them develop, maintain and publish better code while making the experience a lot more enjoyable. The repository
contains sample files that demonstrate all the functionality that we discuss in this tutorial. Ideally, one should start from
an empty repository and follow along the various sections below to write code, documentation & tests and then configure the build
and deployment systems, referring to the sample code whenever necessary. Originally intended for scientific software developers coming
from a non Software Engineering background, the tutorial mainly focuses on developing python libraries (as opposed to webapps). However,
much of the information here is applicable and transferable to other domains of software development as well. 

What this tutorial isn't, is an in-depth treatment of the various tools we describe. Almost always, we will provide a brief introduction
and give a taste of what all can be done using a particular tool and then include links to documentation and tutorials that do a better job in 
giving you a step-by-step guide to using said tools.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   structuring
   dependency
   documentation
   type-hints
   test-coverage
   complexity
   code-format-lint
   collaboration
   pre-commit
   ci-cd
   packaging
   ide-plugins

Indices and Search
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. https://dont-be-afraid-to-commit.readthedocs.io/en/latest/cheatsheet.html
.. https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
.. https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html
