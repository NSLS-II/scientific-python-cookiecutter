============================
Publishing the Documentation
============================

In this section you will publish your documentation on a public website hosted
by GitHub Pages.

This section assume you have already set up Travis-CI, as we covered in a
previous section, :doc:`ci`.

We recommend `doctr <https://drdoctr.github.io/doctr/>`_ a tool that configures
Travis-CI to automatically publish your documentation every time the master
branch is updated.

Just type ``doctr configure`` and follow the prompts. Example:

.. code-block:: bash

    $ doctr configure
    Welcome to Doctr.

    We need to ask you a few questions to get you on your way to automatically
    deploying from Travis CI to GitHub pages.

    What is your GitHub username? YOUR_GITHUB_USERNAME
    Enter the GitHub password for YOUR_GITHUB_USERNAME:
    A two-factor authentication code is required: app
    Authentication code: XXXXXX
    What repo do you want to build the docs for (org/reponame, like 'drdoctr/doctr')? YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
    What repo do you want to deploy the docs to? [YOUR_GITHUB_USERNAME/YOUR_REPO_NAME]

    The deploy key has been added for YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.

    You can go to https://github.com/NSLS-II/NSLS-II.github.io/settings/keys to revoke the deploy key.

    ================== You should now do the following ==================

    1. Add the file  github_deploy_key_your_github_username_your_repo_name.enc to be staged for commit:

        git add github_deploy_key_your_github_username_your_repo_name.enc

    2. Add these lines to your `.travis.yml` file:

        env:
        global:
            # Doctr deploy key for YOUR_GITHUB_USERNAME/YOUR_REPO_NAME
            - secure: "<REDACTED>"

        script:
        - set -e
        - <Command to build your docs>
        - pip install doctr
        - doctr deploy --built-docs <path/to/built/html/> --deploy-repo YOUR_GITHUB_USERNAME/YOUR_REPO_NAME <target-directory>

    Replace the text in <angle brackets> with the relevant
    things for your repository.

    Note: the `set -e` prevents doctr from running when the docs build fails.
    We put this code under `script:` so that if doctr fails it causes the
    build to fail.

    3. Commit and push these changes to your GitHub repository.
    The docs should now build automatically on Travis.

    See the documentation at https://drdoctr.github.io/ for more information.

Another popular option for publishing documentation is
`https://readthedocs.org/ <https://readthedocs.org/>`_ . We slightly prefer
using Travis-CI + GitHub Pages because it is easier to debug any installation
issues. It is also more efficient: we have to build the documentation on
Travis-CI anyway to verify that any changes haven't broken them, so we might as
well upload the result and be done, rather than having readthedocs build them
again.
