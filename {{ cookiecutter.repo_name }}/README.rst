{% set section_separator = "=" * cookiecutter.project_name | length -%}
{{ section_separator }}
{{ cookiecutter.project_name }}
{{ section_separator }}

.. image:: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions/workflows/testing.yml/badge.svg
   :target: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions/workflows/testing.yml


.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}


{{ cookiecutter.project_short_description}}

* Free software: 3-clause BSD license
* Documentation: (COMING SOON!) https://{{ cookiecutter.github_username}}.github.io/{{ cookiecutter.repo_name }}.

Features
--------

* TODO
