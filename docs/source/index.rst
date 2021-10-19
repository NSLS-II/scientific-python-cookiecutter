.. Packaging Scientific Python documentation master file, created by
   sphinx-quickstart on Thu Jun 28 12:35:56 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bootstrap a Scientific Python Library
=====================================

This is a tutorial with a template for packaging, testing, documenting, and
publishing scientific Python code.

Do you have a folder of disorganized scientific Python scripts? Are you always
hunting for code snippets scattered across dozens of Jupyter notebooks? Has it
become unwieldy to manage, update, and share with collaborators? This tutorial
is for you.

See this lightning talk from Scipy 2018 for a short overview of the motivation
for and scope of this tutorial.

.. youtube:: 1HDq7QoOlI4?start=1961

Starting from a working, full-featured template, you will:

* Move your code into a version-controlled, installable Python package.
* Share your code on GitHub.
* Generate documentation including interactive usage examples and plots.
* Add automated tests to help ensure that new changes don't break existing
  functionality.
* Use a free CI (continuous integration) service to automatically run your
  tests against any proposed changes and automatically publish the latest
  documentation when a change is made.
* Publish a release on PyPI so that users and collaborators can install your
  code with pip.

.. toctree::
   :maxdepth: 2

   philosophy
   preliminaries
   the-code-itself
   guiding-design-principles
   ci
   pre-commit
   writing-docs
   including-data-files
   publishing-docs
   publishing-releases
   advanced-testing
   environments
   further-reading
