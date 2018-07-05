=============================
Continous Integration Testing
=============================

In this section you will:

* Understand the benefits Continuous Integration.
* Configure Travis-CI, a "continuous integration" service, to operate on your
  GitHub repository.

What is CI for?
---------------

If "Continuous Integration" (CI) is new to you, we refer you to
`this excellent Software Carpentry tutorial <https://katyhuff.github.io/python-testing/08-ci/>`_
on the subject. To summarize, CI speeds development by checking out your code on
a fresh, clean server, installing your software, running the tests, and
reporting the results. This helps you ensure that your code will work on your
colleague's computer---that it doesn't accidentally depend on some local detail
of your machine. It also creates a clear, public record of whether the tests
passed or failed, so if things are accidentally broken (say, while you are on
vacation) you can trace when the breaking change occurred.

Travis-CI Configuration
-----------------------

The cookiecutter template has already generated a configuration file for
Travis-CI, which is one of several CI services that are free for public
open-source projects.

.. literalinclude:: ../../{{ cookiecutter.repo_name }}/.travis.yml

You can customize this to your liking. For example, if you are migrating a
large amount of existing code that is not compliant with PEP8, you may want to
remove the line that does ``flake8`` style-checking.

Activate Travis-CI for Your GitHub Repository
---------------------------------------------

.. warning::

   The following instructions are not yet well tested.
   `Feedback is welcome!  <https://github.com/NSLS-II/packaging-scientific-python/issues/new>`_

1. Go to https://travis-ci.org and sign in with your GitHub account.
2. Go to https://travis-ci.org/profile, which shows a list of your GitHub
   repositories. Click the "Sync Account" button to refresh that list.
3. Find your Python package in the list, and click the on/off switch to
   activate Travis-CI on that repository.

The next time you open a pull request or push a new commit to the master
branch, Travis-CI will kick off a *build*, which you can see at
``https://travis-ci.org/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/builds``.
