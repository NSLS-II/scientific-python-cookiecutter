=====================
Writing Documentation
=====================

Build the docs
--------------

The cookiecutter template generated some documentation to start from.

.. code-block:: none

      example/
      (...)
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
      (...)

The ``.rst`` files are source code for our documentation. To build HTML pages
from this source, run:

.. code-block:: bash

   make -C docs html

You should see some log message ending in ``build succeeded.``

This output HTML will be located in ``docs/build/html``. In your Internet
browser, open ``file:///.../docs/build/html/index.html``, where ``...`` is the
path to your project directory. If you aren't sure sure where that is, type
``pwd``.

Update the docs
---------------

The source code for the documentation is located in ``docs/source/``.
Sphinx uses a markup language called ReStructured Text (.rst). We refer you to
`this primer <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
to learn how to denote headings, links, lists, etc.

Sphinx formatting is quite picky, much less forgiving than HTML. We recommend
running ``make -C docs html`` often to check that the documentation builds
successfully. Remember to commit your changes to git periodically.

Good documentation includes both:

* API documentation, listing every public object in the library and its usage
* Examples and tutorials with prose explaining how and why a library is meant
  to be used

API Documentation
-----------------

Most the work of writing good API documentation goes into writing good,
accurate docstrings. Sphinx can scrape that content and generate HTML from it.
Again, most scientific Python libraries use the
`numpydoc standard <https://numpydoc.readthedocs.io/en/latest/format.html>`_.

Prose and examples
------------------
