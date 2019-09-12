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

.. literalinclude:: example_travis.yml

You can customize this to your liking. For example, if you are migrating a
large amount of existing code that is not compliant with PEP8, you may want to
remove the line that does ``flake8`` style-checking.

Activate Travis-CI for Your GitHub Repository
---------------------------------------------

#. Go to https://travis-ci.org and sign in with your GitHub account.
#. You will be prompted to authorize Travis-CI to access your GitHub account.
   Authorize it.
#. You will be redirected to https://travis-ci.org/profile, which shows a list
   of your GitHub repositories. If necessary, click the "Sync Account" button
   to refresh that list.
#. Find your new repository in the list. Click the on/off switch next to its
   name activate Travis-CI on that repository.
#. Click the repository name, which will direct you to the list of *builds* at
   ``https://travis-ci.org/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/builds``. The
   list will currently be empty. You'll see construction cones.
#. The next time you open a pull request or push a new commit to the master
   branch, Travis-CI will kick off a new build, and that list will update.

.. note::

    If this repository belongs to a GitHub *organization* (e.g.
    http://github.com/NSLS-II) as opposed to a personal user account
    (e.g. http://github.com/danielballan) you should follow Steps 3-5
    above for the organization's profile at
    ``https://travis-ci.org/profile/YOUR_GITHUB_ORGANIZATION``. It does no
    harm to *also* activate Travis-CI for your personal fork at
    ``https://travis-ci.org/profile``, but it's more important to activate it for
    the upstream fork associated with the organization.
