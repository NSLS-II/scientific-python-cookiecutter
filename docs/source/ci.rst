=============================
Continous Integration Testing
=============================

In this section you will:

* Understand the benefits Continuous Integration.
* Configure Travis-CI, a "continuous integration" service, to operate on your
  GitHub repository.

If "Continuous Integration" (CI) is new to you, we refer you to
`this excellent Software Carpentry tutorial <https://katyhuff.github.io/python-testing/08-ci/>`_
on the subject. To summarize, CI speeds development by checking out your code on
a fresh, clean server, installing your software, running the tests, and
reporting the results. This helps you ensure that your code will work on your
colleague's computer---that is doesn't accidentally depend on some local detail
of your machine. It also creates a clear, public record of whether the tests
passed or failed, so if things are accidentally broken (say, while you are on
vacation) you can trace when the breaking change occurred.

The cookiecutter template has already generated a configuration file for
Travis-CI.

.. literalinclude:: ../../{{ cookiecutter.repo_name }}/.travis.yml
