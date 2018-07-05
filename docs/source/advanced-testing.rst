=========================
Common Patterns for Tests
=========================

In this section you will learn some useful features of pytest that can make
your tests succinct and easy to maintain.

Parametrized Tests
------------------

Tests that apply the same general test logic to a collection of different
parameters can use parametrized tests. For example, this:

.. code-block:: python

   import numpy as np
   from ..refraction import snell


   def test_perpendicular():
       # For any indexes, a ray normal to the surface should not bend.
       # We'll try a couple different combinations of indexes....

       actual = snell(0, 2.00, 3.00)
       expected = 0
       assert actual == expected

       actual = snell(0, 3.00, 2.00)
       expected = 0
       assert actual == expected

can be rewritten as:

.. code-block:: python

   import numpy as np
   import pytest
   from ..refraction import snell


   @pytest.mark.parametrize('n1, n2',
                            [(2.00, 3.00),
                             (3.00, 2.00),
                            ])
   def test_perpendicular(n1, n2):
       # For any indexes, a ray normal to the surface should not bend.
       # We'll try a couple different combinations of indexes....

       actual = snell(0, n1, n2)
       expected = 0
       assert actual == expected

The string ``'n1, n2'`` specifies which parameters this decorator will fill in.
Pytest will run ``test_perpendicular`` twice, one for each entry in the
list ``[(2.00, 3.00), (3.00, 2.00)]``, passing in the respective values ``n1``
and ``n2`` as arguments.

From here we refer you to the
`pytest parametrize documentation <https://docs.pytest.org/en/latest/parametrize.html>`_.

Fixtures
--------

Tests that have different logic but share the same setup code can use pytest
fixtures. For example, this:

.. code-block:: python

   import numpy as np


   def test_height():
       # Construct a 1-dimensional Gaussian peak.
       x = np.linspace(-10, 10, num=21)
       sigma = 3.0
       peak = np.exp(-(x / sigma)**2 / 2) / (sigma * np.sqrt(2 * np.pi))
       expected = 1 / (sigma * np.sqrt(2 * np.pi))
       # Test that the peak height is correct.
       actual = np.max(peak)
       assert np.allclose(actual, expected)


   def test_nonnegative():
       # Construct a 1-dimensional Gaussian peak.
       x = np.linspace(-10, 10, num=20)
       sigma = 3.0
       peak = np.exp(-(x / sigma)**2 / 2) / (sigma * np.sqrt(2 * np.pi))
       # Test that there are no negative values.
       assert np.all(peak >= 0)

can be written as:

.. code-block:: python

   import pytest
   import numpy as np


   @pytest.fixture
   def peak():
       # Construct a 1-dimensional Gaussian peak.
       x = np.linspace(-10, 10, num=21)
       sigma = 3.0
       peak = np.exp(-(x / sigma)**2 / 2) / (sigma * np.sqrt(2 * np.pi))
       return peak


   def test_height(peak):
       expected = 1 / (sigma * np.sqrt(2 * np.pi))
       # Test that the peak height is correct.
       actual = np.max(peak)
       assert np.allclose(actual, expected)


   def test_nonnegative(peak):
       # Test that there are no negative values.
       assert np.all(peak >= 0)

To reuse a fixture in multiple files, add it to ``conftest.py`` located in the
``tests/`` directory. It will automatically be imported by pytest into each
test module.

From here we refer you to the
`pytest fixtures documentation <https://docs.pytest.org/en/latest/fixture.html>`_.

Skipping Tests
--------------

Sometimes it is useful to skip specific tests under certain conditions.
Examples:

.. code-block:: python

   import pytest
   import sys


   @pytest.mark.skipif(sys.version_info < (3, 7),
                       reason="requires python3.7 or higher")
   def test_something():
       ...


   @pytest.mark.skipif(sys.platform == 'win32',
                       reason="does not run on windows")
   def test_something_that_does_not_work_on_windows():
       ...


   def test_something_that_needs_a_special_dependency():
       some_library = pytest.importorskip("some_library")
       ...

From here we refer you to the
`pytest skipping documentation <https://docs.pytest.org/en/latest/skipping.html>`_.
