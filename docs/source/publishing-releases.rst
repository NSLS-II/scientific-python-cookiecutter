===================
Publishing Releases
===================

1. Choose a version number. The convention following by most scientific Python
   packages is ``vMAJOR.MINOR.MICRO``, as in ``v1.3.0``. A good number to start
   with is ``v0.1.0``.

   These numbers have meanings.
   The goal is to communicate to the user whether upgrading will break anything
   in *their* code that will need to be updated in turn.
   
   * Incrementing the ``MICRO`` number (``v1.3.0`` -> ``v1.3.1``) means, "I
     have fixed some bugs, but I have not added any major new features or
     changed any names. All of your code should still work without changes."
   * Incrementing the ``MINOR`` number (``v1.3.0`` -> ``v1.4.0``) means, "I
     have added some new features and changed some minor things. Your code
     should work with perhaps some small updates."
   * Incrementing the ``MAJOR`` number (``v1.3.0`` -> ``v2.0.0``) means, "I
     have made major changes that will probably require you to update your
     code."

   Additionally, if the ``MAJOR`` version is ``0``, the project is considered
   to be in early development and may make major breaking changes in minor
   releases.

   Obviously this is an imprecise system. Think of it a highly-compressed,
   lossy representation of how painful it will be for the user to upgrade.

2. Type ``git status`` and check that you are on the ``master`` branch with no
   uncommitted code.

3. Mark the release with an empty commit, just to leave a marker. This is
   optional, but it makes it easier to find the release when skimming through
   the git history.

   .. code-block:: bash

      git commit --allow-empty -m "REL: vX.Y.Z"

4. Tag the commit.

   .. code-block:: bash

      git tag vX.Y.Z  # Don't forget the leading v

5. Verify that the ``__version__`` attribute is correctly updated.

   The version is reported in three places:

   1. The git tag
   2. The version parameter in the ``setup.py`` file
   3. Your package's ``__version__`` attribute, in Python

   `Versioneer <https://github.com/warner/python-versioneer>`_, which was
   included and configured for you by the cookiecutter template, automatically
   keeps these three in sync. Just to be sure that it worked properly, start up
   Python, import the module, and check the ``__version__``.  It should have
   automatically updated to match the tag. The leading ``v`` is not included.

   .. code-block:: python

      import your_package
      your_package.__version__  # should be 'X.Y.Z'

5. Push the new commit and the tag to ``master``.

   .. code-block:: bash

      git push origin master
      git push origin vX.Y.Z

   .. note::

        Check your remotes using ``git remote -v``. If your respoitory is
        stored in an organization account, you may need to push to ``upstream``
        as well as ``origin``

6. Publish a release on PyPI.

   .. code-block:: bash

       python setup.py sdist
       python setup.py bdist_wheel
       pip install twine
       twine upload dist/*

The package is now installable with pip. It may take a couple minutes to become
available.
