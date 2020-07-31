===============
Getting Started
===============

In this section you will:

* Sign up for Github.
* Generate a scaffold for your new Python project.
* Upload it to GitHub.
* Install your new Python project for development.

Then, in the next section, we will begin to move your scientific code into that
template.

You will need a Terminal (Windows calls it a "Command Prompt") and a plain text
editor. Any will do; we won't assume anything about the editor you are using.
If you are looking for a recommendation for beginners, the `Atom Editor
<https://atom.io/>`_ by GitHub is a good one. For minimalists, ``nano`` on
Linux or OSX and Notebook on Windows will get you up and running.

Reading the steps that follow, you might reasonably wonder, "Why isn't there
just an automated script for this?" We prefer to do this process manually so
that we are forced to think carefully about each step, notice when something
goes wrong, and debug if necessary. We recommend you do the same.

#. `Sign up for GitHub <http://github.com/>`_.

#. Verify that you have Python 3.

   .. code-block:: bash
  
      python3 --version
  
   If necessary, install it by your method of choice: apt, Homebrew, conda,
   etc.

#. Create an *environment*, a sandboxed area for installing software that is
   separate from the system defaults. This is not essential, but it is
   strongly encouraged. It ensures that your project and its software
   dependencies will not interfere with other Python software on your system.
   There are several tools for this.  But the simplest is Python's built-in
   ``venv`` (short for "virtual environments"), illustrated here.

   Do this once:

   .. code-block:: bash

      python3 -m venv my-env

   The term ``my-env`` can be anything. It names the new environment.

   Do this every time you open up a new Terminal / Command Prompt to work on
   your project:

   .. code-block:: bash

      . my-env/bin/activate

   .. note::

      If you are a conda user, you may prefer a conda environment:

      .. code-block:: bash

         conda create -n my-env python=3.7
         conda activate my-env

#. Verify that you have git installed.

   .. code-block:: bash
  
      git

   If necessary, install it by your method of choice (apt, Homebrew, conda, etc.).

#. Choose a name for your project.

   Ideal names are descriptive, succinct, and easy to Google. Think about who
   else might be interested in using or contributing to your project in the
   future, and choose a name that will help that person discover your project.
   There is no need to put "py" in the name; usually your user will already
   know that this is a Python project.

   Check that the name is not already taken by
   `searching for it on the Python Package Index (PyPI) <https://pypi.org/>`_.

#. Install cookiecutter.

   .. code-block:: bash

      python3 -m pip install --upgrade cookiecutter

#. Generate a new Python project using our cookiecutter template.

   .. code-block:: bash
   
      cookiecutter https://github.com/NSLS-II/scientific-python-cookiecutter


   You will see the following the prompts. The default suggestion is given in square brackets.

   For the last question, ``minimum_supported_python_version``, we recommend
   supporting back to Python 3.6 unless you have a need for newer Python
   features.

   .. code-block:: bash

      full_name [Name or Organization]: Brookhaven National Lab
      email []: dallan@bnl.gov
      github_username []: danielballan
      project_name [Your Project Name]: Example
      package_dist_name [example]:
      package_dir_name [example]:
      repo_name [example]:
      project_short_description [Python package for doing science.]: Example package for docs.
      year [2018]:
      Select minimum_supported_python_version:
      1 - Python 3.6
      2 - Python 3.7
      3 - Python 3.8
      Choose from 1, 2, 3 [1]:

   This generates a new directory, ``example`` in this case, with all the
   "scaffolding" of a working Python project.

   .. code-block:: bash

      $ ls example/
      AUTHORS.rst        MANIFEST.in     example                 setup.cfg
      CONTRIBUTING.rst   README.rst      requirements-dev.txt    setup.py
      LICENSE            docs            requirements.txt        versioneer.py

   .. note::

      Cookiecutter prompted us for several variations of *name*.
      If are you wondering what differentiates all these names, here's a primer:

      * ``project_name`` -- Human-friendly title. Case sensitive. Spaces allowed.
      * ``package_dist_name`` -- The name to use when you ``pip install ___``.
        Dashes and underscores are allowed. Dashes are conventional. Case
        insensitive.
      * ``package_dir_name`` --- The name to use when you ``import ___`` in Python.
        Underscores are the only punctuation allowed. Conventionally lowercase.
      * ``repo_name`` --- The name of the GitHub repository. This will be the
        name of the new directory on your filesystem.

#. Take a moment to see what we have. (Some systems treat files whose name
   begins with ``.`` as "hidden files", not shown by default. Use the ``ls -a``
   command in the Terminal to show them.)

   .. The following code-block output was generated using `tree -a example/`.

   .. code-block:: none

      example/
      ├── .flake8
      ├── .gitattributes
      ├── .gitignore
      ├── .travis.yml
      ├── AUTHORS.rst
      ├── CONTRIBUTING.rst
      ├── LICENSE
      ├── MANIFEST.in
      ├── README.rst
      ├── docs
      │   ├── Makefile
      │   ├── build
      │   ├── make.bat
      │   └── source
      │       ├── _static
      │       │   └── .placeholder
      │       ├── _templates
      │       ├── conf.py
      │       ├── index.rst
      │       ├── installation.rst
      │       ├── release-history.rst
      │       └── usage.rst
      ├── example
      │   ├── __init__.py
      │   ├── _version.py
      │   └── tests
      │       └── test_examples.py
      ├── requirements-dev.txt
      ├── requirements.txt
      ├── setup.cfg
      ├── setup.py
      └── versioneer.py

   In this top ``example/`` directory, we have files specifying metadata about
   the Python package (e.g. ``LICENSE``) and configuration files related to
   tools we will cover in later sections. We are mostly concerned with the
   ``example/example/`` subdirectory, which is the Python package itself. This
   is where we'll put the scientific code. But first, we should version-control
   our project using git.

#. Change directories into your new project.

   .. code-block:: bash

      cd example

   We are now in the top-level ``example/`` directory---not ``example/example``!

#. Make the directory a git repository.

   .. code-block:: bash

      $ git init
      Initialized empty Git repository in (...)

#. Make the first "commit". If we break anything in later steps, we can always
   roll back to this clean initial state.

   .. code-block:: bash

      $ git add .
      $ git commit -m "Initial commit."

#. `Create a new repository on GitHub <https://github.com/new>`_,
   naming it with the ``repo_name`` from your cookiecutter input above.

   .. important::

      Do **not** check "Initialize this repository with a README".

#. Configure your local repository to know about the remote repository on
   GitHub...

   .. code-block:: bash

      $ git remote add origin https://github.com/YOUR_GITHUB_USER_NAME/YOUR_REPOSITORY_NAME.

   ... and upload the code.

   .. code-block:: bash

      $ git push -u origin master
      Counting objects: 42, done.
      Delta compression using up to 4 threads.
      Compressing objects: 100% (40/40), done.
      Writing objects: 100% (42/42), 29.63 KiB | 0 bytes/s, done.
      Total 42 (delta 4), reused 0 (delta 0)
      remote: Resolving deltas: 100% (4/4), done.
      To github.com:YOUR_GITHUB_USER_NAME/YOUR_REPO_NAME.git
       * [new branch]      master -> master
         Branch master set up to track remote branch master from origin.


   .. note::

      If this repository is to belong to a GitHub *organization* (e.g.
      http://github.com/NSLS-II) as opposed to a personal user account
      (e.g. http://github.com/danielballan) it is conventional to name the
      organization remote ``upstream`` instead of ``origin``.

      .. code-block:: bash

          $ git remote add upstream https://github.com/ORGANIZATION_NAME/YOUR_REPOSITORY_NAME.
          $ git push -u upstream master
          Counting objects: 42, done.
          Delta compression using up to 4 threads.
          Compressing objects: 100% (40/40), done.
          Writing objects: 100% (42/42), 29.63 KiB | 0 bytes/s, done.
          Total 42 (delta 4), reused 0 (delta 0)
          remote: Resolving deltas: 100% (4/4), done.
          To github.com:ORGANIZATION_NAME/YOUR_REPO_NAME.git
           * [new branch]      master -> master
             Branch master set up to track remote branch master from upstream.

      and, separately, add your personal fork as ``origin``.

      .. code-block:: bash

          $ git remote add origin https://github.com/YOUR_GITHUB_USER_NAME/YOUR_REPOSITORY_NAME.

#. Now let's install your project for development.

   .. code-block:: python

      python3 -m pip install -e .

   .. note::

      The ``-e`` stands for "editable". It uses simlinks to link to the actual
      files in your repository (rather than copying them, which is what plain
      ``pip install .`` would do) so that you do not need to re-install the
      package for an edit to take effect.

      This is similar to the behavior of ``python setup.py develop``. If you
      have seen that before, we recommend always using ``pip install -e .``
      instead because it avoids certain pitfalls.

#. Finally, verify that we can import it.

   .. code-block:: bash

      python3

   .. code-block:: python

      >>> import your_package_name

#. Looking ahead, we'll also need the "development requirements" for our
   package. These are third-party Python packages that aren't necessary to
   *use* our package, but are necessary to *develop* it (run tests, build the
   documentation). The cookiecutter template has listed some defaults in
   ``requirements-dev.txt``. Install them now.

  .. code-block:: bash

     python3 -m pip install --upgrade -r requirements-dev.txt

Now we have a working but empty Python project. In the next section, we'll
start moving your scientific code into the project.
