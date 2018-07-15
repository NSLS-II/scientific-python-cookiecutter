=================================
Environments and Package Managers
=================================

Throughout this tutorial, we used ``pip``, a Python package manager, to install
our software and other Python software we needed. In :doc:`preliminaries`, we
used ``venv`` to create a "virtual environment", a sandbox separate from the
general system Python where we could install and use software without
interfering with any system Python tools or other projects.

There are many alternatives to ``venv``.
`This post of Stack Overflow <https://stackoverflow.com/a/41573588/1221924>`_
is a good survey of the field.

Conda
-----

Conda, which is both a package manager (like ``pip``) and an virtual
environment manager (like ``venv``) was developed specifically for the
scientific Python community. Conda is not limited to Python packages: it has
grown into a general-purpose user-space package manager. Many important
scientific Python packages have important dependencies that aren't Python
packages and can't be installed using ``pip``. Before conda, the user had to
sort out how to install these extra dependencies using the system package
manager, and it was a common pain point. Conda can install all of the
dependencies.

Conda is conceptually a heavier lift that ``pip`` and ``venv``, which is why we
still with the basics in :doc:`preliminaries`, but it is extremely popular
among both beginners and experts, and we recommend becoming familiar with it.

Check whether ``conda`` is already installed:

.. code-block:: bash

   conda

If that is not found, follow the steps in the
`conda installation guide <https://conda.io/docs/user-guide/install/index.html>`_,
which has instructions for Windows, OSX, and Linux. It offers both miniconda (a
minimal installation) and Anaconda. For our purposes, either is suitable.
Miniconda is a faster installation.

Now, create an environment.

.. code-block:: bash

   conda create -n my-env python=3.6

The term ``my-env`` can be anything. It names the new environment.

Every time you open up a new Terminal / Command Prompt to work on your
project, activate that environment. This means that when you type ``python3``
or, equivalently, ``python`` you will be getting a specific installation of
Python and Python packages, separate from any default installation on your
machine.

.. code-block:: bash

   conda activate my-env

The use of virtual environments leads to multiple instances of ``python``,
``pip``, ``ipython``, ``pytest``, ``flake8`` and other executables on your
machine. If you encounter unexpected behavior, use ``which ____`` to see which
environment a given command is coming  from. (Linux and OSX only.)
