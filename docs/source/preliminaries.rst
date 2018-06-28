===============
Getting Started
===============

At the end of this section you will have:

* Signed up for Github
* Generated a template for your Python project, complete with example
  documentation and a testing framework
* Uploaded it to GitHub

Then, in the next section, we will begin to move your scientific code into that
template.

1. `Sign up for GitHub <http://github.com/>`_.

2. Verify that you have Python 3.6+.

  .. code-block:: bash
  
     python3 --version
  
  If necessary, install it by your method of choice (apt, Homebrew, conda, etc.).

3. Verify that you have git installed. 

  .. code-block:: bash
  
     git

  If necessary, install it by your method of choice (apt, Homebrew, conda, etc.).

4. Choose a name for your project. Ideal names are descriptive, succinct, and
   easy to Google. Think about who else might be interested in using or
   contributing to your project in the future, and choose a name that will help
   that person discover your project. There is no need to put "py" in the name;
   usually your user will already know that this is a Python project.

5. Generate a template using cookiecutter.

   .. code-block:: bash

    pip install cookiecutter
    cookiecutter https://github.com/NSLS-II/packaging-scientific-python

6. Take a moment to see what we have. In this top directory, we have files
   related to installing the Python packages. There is a ``requirements.txt``
   file listing the other Python packages that our package depends on. There
   a template of documentation in the ``docs`` directory. There is a
   ``LICENSE`` and a list of authors.

   .. code-block:: bash

      $ cd science-doer
      $ ls
      AUTHORS.rst        MANIFEST.in     requirements-dev.txt    setup.cfg
      CONTRIBUTING.rst   README.rst      requirements.txt        setup.py
      LICENSE            docs            science_doer            versioneer.py

   We are mostly concerned with the ``science_doer`` directory, which is the
   Python package itself.

   .. code-block:: bash

      $ ls science_doer/
      __init__.py    _version.py    tests

   This is where we'll put the scientific code. But first, we should
   version-control our project using git.

7. Make your template a git repository.

   .. code-block:: bash

    $ git init
    Initialized empty Git repository in (...)

8. Make the first "commit". If we break anything in later steps, we can always
   roll back to this clean initial state.

   .. code-block:: bash

      $ git add .
      $ git commit -am "Initial commit."

9. `Create a new repository on GitHub <https://github.com/new>`_,
   naming it with the ``repo_name`` from your cookiecutter input above.

   .. important::

      Do **not** check "Initialize this repository with a README".

10. Configure your local repository to know about the remote repository on
    GitHub...

    .. code-block:: bash

       $ git add remote origin https://github.com/YOUR_GITHUB_USER_NAME/YOUR_REPOSITORY_NAME.

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

       If this repository is to belong to a GitHub *organiziation* (e.g.
       http://github.com/NSLS-II) as opposed to a specific user account
       (e.g. http://github.com/danielballan) it is conventional to name the
       organization remote ``upstream`` instead of ``origin``.

       .. code-block:: bash

           $ git add remote upstream https://github.com/ORGANIZATION_NAME/YOUR_REPOSITORY_NAME.
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

           $ git add remote origin https://github.com/YOUR_GITHUB_USER_NAME/YOUR_REPOSITORY_NAME.

Next, let's start moving your scientific code into the project.
