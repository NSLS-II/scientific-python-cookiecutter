===============
The Code Itself
===============

In this section you will:

* Put some scientific code to your Python package.
* Update our package's list of dependencies in ``requirements.txt``.
* Write a test.

A simple function with inline documentation
-------------------------------------------

Let's write a simple function that encodes
`Snell's Law <https://en.wikipedia.org/wiki/Snell%27s_law>`_ and include it in
our Python package.

Look again at the directory structure.

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

Our scientific code should go in the ``example/`` subdirectory, next to
``__init__.py``. Let's make a file named ``refraction.py``.

.. code-block:: python

    # example/refraction.py

    import numpy as np


    def snell(theta_inc, n1, n2):
        """
        Compute the refraction angle using Snell's Law.

        See https://en.wikipedia.org/wiki/Snell%27s_law

        Parameters
        ----------
        theta_inc : float
            Incident angle
        n1 : float
            Refractive index of medium of origin
        n2: : float
            Refractive index of destination medium

        Returns
        -------
        theta : float
            refraction angle

        Examples
        --------
        A ray enters an air--water boundary at 45 degrees. Compute exit angle.
        >>> snell(np.deg2rad(45), 1.00, 1.33)
        0.5605584137424605
        """
        return np.arcsin(n1 / n2 * np.sin(theta_inc))

Notice that this example includes inline documentation --- a "docstring". This
is extremely useful for collaborators, and the most common collaborator is
Future You!

Further, by following the
`numpydoc standard <https://numpydoc.readthedocs.io/en/latest/format.html>`_,
we will be able to automatically generate nice-looking HTML documentation
later. Notable features:

* There is a succinct, one-line summary of the functions use. It must one line.
* There is an optional paragraph elaborating on that summary.
* There is a list of parameters with the structure

  .. code-block :: none

     parameter_name : parameter_type
         optional description

  Note that space before the ``:``. That is part of the standard.
* Finally, there is an optional block of examples.

Update Requirements
-------------------

Notice that our package has a third-party dependency, numpy. We should
update our package's ``requirements.txt``.

.. code-block:: text

   # requirements.txt

   # List required packages in this file, one per line.
   numpy

Our cookiecutter configured ``setup.py`` to read this file. It will ensure that
numpy is installed when our package is installed.

We can test it by reinstalling the package.

.. code-block:: bash

   python3 -m pip install --user -e .

Try it
------

Try importing and using the function.


.. code-block:: python

    >>> from example.refraction import snell
    >>> import numpy as np
    >>> snell(np.deg2rad(45), 1.00, 1.33))
    1.2239576240104186

The docstring can be viewed with :func:`help`.

.. code-block:: python

    >>> help(snell)

Or, as a shortcut, use ``?`` in IPython/Jupyter.

.. ipython:: python
   :verbatim:

   snell?

Run the Tests
-------------

You should add a test right away while the details are still fresh in mind.
Writing tests encourages you to write modular, reusable code, which is easier
to test.

The cookiecutter template included an example test suite with one test:

.. code-block:: python

   # example/tests/test_examples.py

   def test_one_plus_one_is_two():
       assert 1 + 1 == 2

Before writing our own test, let's practice running that test to check that
everything is working.

First, install the "development requirements" for our package. These are
third-party Python packages that aren't necessary to *use* our package, but are
necessary to *develop* it (run tests, build the documentation). The cookiecutter
template has listed some defaults in ``requirements-dev.txt``.

.. code-block:: bash

   python3 -m pip install --upgrade --user -r requirements-dev.txt

Now run the tests like so.

.. code-block:: bash

   pytest

This walks through all the directories and files in our package that start with
the word 'test' and collects all the functions whose name also starts with
``test``. Currently, there is just one, ``test_one_plus_one_is_two``.
``pytest`` runs that function. If no exceptions are raised, the test passes.

The output should look something like this:

.. code-block:: bash

   ======================================== test session starts ========================================
   platform darwin -- Python 3.6.4, pytest-3.6.2, py-1.5.4, pluggy-0.6.0
   benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
   rootdir: /private/tmp/test11/example, inifile:
   plugins: xdist-1.22.2, timeout-1.2.1, rerunfailures-4.0, pep8-1.0.6, lazy-fixture-0.3.0, forked-0.2, benchmark-3.1.1
   collected 1 item

   example/tests/test_examples.py .                                                              [100%]

   ===================================== 1 passed in 0.02 seconds ======================================

.. note:: 

   The output of ``pytest`` is customizable. Commonly useful command-line
   arguments include:

   * ``-v`` verbose
   * ``-s`` Do not capture stdout/err per test.
   * ``-k EXPRESSION`` Filter tests by pattern-matching test name.

   Consult the `pytest documentation <https://docs.pytest.org/en/latest/>`_
   for more.

Write a Test
------------

Let's add a test to ``test_examples.py`` that exercises our ``snell`` function.
We can delete ``test_one_plus_one_is_two`` now.

.. code-block:: python

   # example/tests/test_examples.py

   import numpy as np


   def test_perpendicular():
       # For any indexes, a ray normal to the surface should not bend.
       # We'll try a couple different combinations of indexes....

       actual = snell(0, 2.00, 3.00)
       expected = 0
       assert actual == expected

       actual = snell(0, 3.00, 2.00)
       expected = 0
       assert actual == expected


   def test_air_water():
       n_air, n_water = 1.00, 1.33
       actual = snell(np.deg2rad(45), n_air, n_water)
       expected = 0.5605584137424605
       assert np.allclose(actual, expected)

Things to notice:

* It is sometime useful to put multiple ``assert`` statements in one test. You
  should make a separate test for each *behavior* that you are checking. When a
  monolithic, multi-step tests fails, it's difficult to figure out why.
* When comparing floating-point numbers (as opposed to integers) you should not
  test for exact equality. Use :func:`numpy.allclose`, which checks for
  equality within a (configurable) tolerance. Numpy provides several
  `testing utilities <https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.testing.html>`_,
  which should always be used when testing numpy arrays.
* Remember that the names of all test modules and functions must begin with
  ``test`` or they will not be picked up by pytest!

Lint: Check for suspicious-looking code
---------------------------------------

A `linter <https://en.wikipedia.org/wiki/Lint_(software)>`_ is a tool that
analyzes code to flag potential errors. For example, it can catch variables you
defined by never used, which is likely a spelling error.

The cookiecutter configured ``flake8`` for this purpose. Flake8 checks for
"lint" and also enforces the standard Python coding style,
`PEP8 <https://www.python.org/dev/peps/pep-0008/?#introduction>`_. Enforcing
consistent style helps projects stay easy to read and maintain as they grow.

.. code-block:: bash

    flake8

This will list linting or stylistic errors. If there is no output, all is well.
See the `flake8 documentation <http://flake8.pycqa.org/en/latest/>`_ for more.
