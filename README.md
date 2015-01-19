# Schython
Python interpreter implementation in scheme

This project is valuable for several reasons:

*  It will make you more familiar with the structure of the
   metacircular evaluator, because you will have to understand which
   procedure to modify in order to change some aspect of its
   operation.
*  Working with another language may help overcome some of the
   confusion that students often have about working in two different
   versions of Scheme at once.  In this project, it will be quite
   obvious when you are talking to Scheme and when you are talking to
   Python.
*  This project will encourage you to think about the design of a
   programming language.  Why did Scheme's designers and Python's
   designers make different choices?
*  We hope that this project will encourage you to create your own
   language with its own syntax!  One of the beautiful aspects of
   computer science is that if there isn't a tool or a language that
   satisfies your requirements, you can make your own!
   
   The version of Python most widely used is written in C, but there are
other popular versions written in Java, in C#, in Chinese (!), and
yes, in Python itself.  Our version will be written in a language that
you already know (and maybe love): Scheme.

Getting Started:

You should have the following files to run and code Schython:

     obj.scm
     parser.scm
     py-meta.scm
     py-primitives.scm
     primitives.py
     start.scm

A note about the syntax of this specification: all capitalized words
are either new terms or Scheme procedures and all words between
single-quotes are to be typed in Python.  Assume correct syntax; you
are welcome to throw errors using the PY-ERROR procedure if you would
like, but it is not required.

To start Schython, you would load the "start" Scheme file into the
STk interpreter:
(If you're using emacs, make sure to read the comments inside start.scm to
get it working when running the file from within emacs).

     STk> (load "start")
     >>>

The Python interpreter prompt should show up.  The INITIALIZE-PYTHON
procedure sets up the global environment and the primitives necessary
for a basic version of Schython to run.  You should be able to perform
basic arithmetic and simple assignments.

At the top of the "py-meta" Scheme file, we have included a
**DEBUGGING** flag.  If it is set to true, then all errors will dump
you back into Scheme; if it is set to false, then all errors will be
hidden, but PY-ERROR invocations will still print an error message and
return you back to Python.  The error-handling in Schython has a few
rough edges: though we have tried to catch most errors in your
Schython instructions and print appropriate Python-like errors, some
errors could potentially dump you back into Scheme.  If this happens,
type

     STk> (driver-loop)

to return to Schython.  You should only use (initialize-python) once,
or else you will lose any Schython variables or procedures you have
defined.

>>> NOTE TO MACINTOSH GAMBIT USERS: Before running this project you
must tell Gambit to read a line, not a Scheme expression, in response
to the ENTER key.  To do this, look in the Edit menu and select Window
Styles.  Near the bottom right corner of the window that will appear
are three check boxes; the middle one is labelled "Enter = Send Line".
Check that box (so that you see an X in the box), then click OK.

>>> NOTE TO WINDOWS USERS: If the INITIALIZE-PYTHON procedure causes
an infinite loop, then your computer does not understand
UNIX-based newline characters.  We don't see any workaround for
this problem, so we suggest that you work on the lab computers,
such as either STAR or NOVA.

