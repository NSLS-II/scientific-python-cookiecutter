=========================
Guiding Design Principles
=========================

In this section we summarize some guiding principles for designing and
organizing scientific Python code.

Collaborate
-----------

Software developed by several people is preferable to software developed by
one.

Talking through a design and the assumptions in it helps to clarify your
thinking. To quote the
`Zen of Python <https://www.python.org/dev/peps/pep-0020/#id3>`_,
"If the implementation is hard to explain, it's a bad idea. If the
implementation is easy to explain, it may be a good idea."

Collaboration takes trust. It is OK to be "wrong"; it is part of the process
of making things better.

Having more than one person understanding every part of the code prevents
systematic risks for the project and keeps you from being tied to that code.

If you can bring together contributors with diverse scientific backgrounds, it
becomes easier to identify functionality that should be generalized for reuse
by different fields.

Don't Be Afraid to Refactor
---------------------------

No code is ever right the first (or second) time.

Refactoring the code once you understand the problem and the design trade-offs
more fully helps keep the code maintainable.

Prefer "Wide" over "Deep"
-------------------------

It should be possible to reuse pieces of software in a way not anticipated by
the original author. That is, branching out from the initial use case should
enable unplanned functionality without a massive increase in complexity.

When building new things, work your way down to the lowest level, understand
than level and then build back up. Try to imagine what else you would want to
do with the capability you are implementing for other research groups, for
related scientific applications, and next year.

Take the time to understand how things need to work at the bottom. It is better
to slowly deploy a robust extensible solution than to quickly deploy a brittle
narrow solution.

Keep I/O Separate
-----------------

One of the biggest impediments to reuse of scientific code is when I/O code---
assuming certain file locations, names, formats, or layouts---is interspersed
with scientific logic.

I/O-related functions should *only* perform I/O. For example, they should take
in a filepath and return a numpy array, or a dictionary of arrays and metadata.
The valuable scientific logic should be encoded in function that take in
standard data types and return standard data types. This maximizes their
potential for reuse by other applications.

Duck Typing is a Good Idea
--------------------------

`Duck typing <https://en.wikipedia.org/wiki/Duck_typing>`_ treats objects based
on what they can *do* based on what type they *are*.

Python in general and scientific Python in particular leverage *interfaces* to
support reuse. For example, it is possible to pass a pandas DataFrame to the
:func:`numpy.sum` even though pandas was created long after :func:`numpy.sum`.
This is because :func:`numpy.sum` avoids assuming it will be passed specific
data types; it accepts any object that provides the right methods (interfaces).
Where possible, avoid ``isinstance`` checks in your code, and try to make your
functions work on the broadest possible range of input types.

"Stop Writing Classes"
----------------------

It is often tempting to invent special objects for a use case or workflow ---
an ``Image`` object or a ``DiffractionAnalysis`` object. This approach has
proven again and again to be difficult to extend and maintain. It is better to
prefer standard, simple data structures like Python dictionaries and numpy
arrays and use simple functions to operate on them.

A popular talk, "Stop Writing Classes," which you can
`watch on YouTube <https://www.youtube.com/watch?v=o9pEzgHorH0&t=193s>`_
illustrates how some situations that *seem* to lend themselves to
object-oriented programming are much more simply handled using plain, built-in
data structures and functions.

As another example, the widely-used scikit-image library initially experimented
with using an ``Image`` class, but ultimately decided that it was better to use
plain old numpy arrays. All scientific Python libraries understand numpy
arrays, but they don't understand custom classes, so it is better to pass
application-specific metadata *alongside* a standard array than to try to
encapsulate all of that information in a new, bespoke object.
