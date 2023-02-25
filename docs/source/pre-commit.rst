========================
Git hooks and pre-commit
========================

In this section you will:

* Learn about git hooks
* Configure pre-commit, a handy program to set up your git hooks.

What are git hooks for?
-----------------------
`Git hooks <https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>`_ are way of running custom
scripts on your repository either client-side or server-side. In fact, server-side hooks can
be used to trigger things like continuous integration. Here we will focus on some client-side
(i.e. on your local machine) hooks that will ensure certain formatting standards
are met prior to commits. This way, all of your commits are meaningful changes to code, and
your git history doesn't get littered with "apply black" and "fix PEP-8" messages.
Notably these kinds of tests can also be run during
continuous integration (as seen in the configuration of :doc:`Travis-CI<ci>`).

We also include a hook that scrubs any output from jupyter notebooks.
This way, the only time git thinks a notebook has changed is when the contents of the cells have changed.

It's just formatting, who cares?
--------------------------------
Ideally, someone else is going to read your code, and better yet, make changes to it.
Having a consistent code style and format makes that easier. Going a step further,
using an even more specific formatter such as `Black <https://black.readthedocs.io/en/stable/>`_,
ensures that changes to programs produce the smallest changes to text possible.

Configuring pre-commit
----------------------
The cookiecutter template has already generated a configuration file for pre-commit,
which will construct your git hooks.

.. literalinclude:: example_pre-commit.yml

You can customize this to your liking, or not use it entirely.
For example, if you are migrating a large amount of existing code that is not compliant with
PEP8, yet managing notebooks collaboratively,
you may want to remove the section that does ``flake8`` style-checking and  ``black``.

Running ``pre-commit install`` inside the top-level directory of your repository
will use this configuration file to set up git hooks to run prior to completing a commit.

Hooks included in this cookiecutter
-----------------------------------
- ``flake8``: Python style enforcement
- ``black``: An uncompromising formatter complient with flake8
- ``isort``: An import sorter for added consistency
- Select hooks from ``pre-commit-hooks``: Whitespace enfrocement and yaml style-checking
- ``nbstripout``: Jupyter notebook stripping of output

Committing Changes
------------------
Assuming you've decided to keep ``nbstripout``, ``black``, and ``flake8`` as hooks, each
time you commit changes to the repository files will be checked for these standards.
If your files don't fit the standard, the commit will fail.

For example with notebooks and ``nbstripout``:
**Before you commit changes to git** the *output* area of the notebooks must
be cleared. This ensures that (1) the potentially-large output artifacts
(such as figures) do not bloat the repository and (2) users visiting the
tutorial will see a clean notebook, uncluttered by any previous code
execution. This can be accomplished by running ``nbstripout`` before the commit.

If you forget to do this, an error message will protect you from accidentally
committing. It looks like this::

    $ git add .
    $ git commit -m "oops"
    nbstripout...............................................................Failed
    - hook id: nbstripout
    - files were modified by this hook


What happened here? Your attempt to commit has been blocked. The files have
been fixed for you---clearing the outputs from your notebooks, but
git-hooks won't assume you want these fixes committed.
Before trying again to commit, you must add those fixes to the "staged" changes::

    # Stage again to include the fixes that we just applied (the cleared output areas).
    $ git add .

    # Now try committing again.
    $ git commit -m "this will work"
    nbstripout...............................................................Passed
    [main 315536e] changed things
     2 files changed, 44 insertions(+), 18 deletions(-)


The same procedure holds for applying black to files.
**However, Flake8 is a checker and not a formatter.
It will only report issues, not change them.**
