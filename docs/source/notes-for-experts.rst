===========================
Philosophy of this Tutorial
===========================

This is an opinionated tutorial, and it streamlines the setup and
configuration at the expense of some flexibility.

Generally speaking, we aim to nudge scientist--developers toward good practices
and standard tools (e.g. setup.py, pytest, flake8) but stop short of the *full*
stack of tools used by large scientific Python projects. Our aim to help small-
and medium-sized projects start off on the right foot, keeping in mind that too
much development infrastructure can be overwhelming to those who haven't yet
encountered the need for it.

Assumptions:

* We assume the project will support the last two minor releases of Python.
  (As of this writing, that's Python 3.6 and Python 3.7.) Python 2 is near its
  scheduled end of life, and Python 3 has
  `many well-documented benefits <https://python-3-for-scientists.readthedocs.io/en/latest/>`_
  for scientific applications.
* We integrate with GitHub, Travis-CI, and GitHub Pages. We welcome
  pull-requests to generalize to other services, provided that the process for
  users remains streamlined.
