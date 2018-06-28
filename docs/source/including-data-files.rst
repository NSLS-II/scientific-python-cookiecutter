====================
Including Data Files
====================

Consider Alternatives
---------------------

**Never include large binary files in your Python package or git repository.**
Once committed, the file lives in git history forever. Git will become
sluggish, because it is not designed to operate on large binary files, and your
package will become an annoyingly large download.

Removing accidentally-committed files after the fact is *possible* but
destructive, so it's important to avoid committing large files.

Alternatives:

* Can you generate the file using code instead? This is a good approach for
  test data: generate the test data files as part of the test. Of course it's
  important to test against *real* data from time to time, but for automated
  tests, simulated data is just fine. If you don't understand your data well
  enough to simulate it accurately, you don't know enough to write useful tests
  against it.
* Can you write a Python function that fetches the data on demand from some
  public URL? This is the approach used by projects such as scikit-beam that
  need to download large datasets for their examples and tests.

Packaging Data Files
--------------------

If the file in question is a text file and not very large (~100 kB) than it's
OK to just bundle it with the package.

Unfortunately, Python does not make this very straightforward, though future
releases of Python will streamline the process.


TO DO
