"""Python has several functions built into the interpreter. If you want to get information of keywords, built-in
functions, modules or topics open a Python console and enter:
>>> help()
You will receive information by entering keywords directly:
>>> help(help)
or within the utility:
help> help
which will show an explanation:
Help on _Helper in module _sitebuiltins object:
class _Helper(builtins.object)
| Define the builtin 'help'.
|
| This is a wrapper around pydoc.help that provides a helpful message
| when 'help' is typed at the Python interactive prompt.
|
| Calling help() at the Python prompt starts an interactive help session.
| Calling help(thing) prints help for the python object 'thing'.
|
| Methods defined here:
|
| __call__(self, *args, **kwds)
|
| __repr__(self)
|
| ----------------------------------------------------------------------
| Data descriptors defined here:
|
| __dict__
| dictionary for instance variables (if defined)
|
| __weakref__
| list of weak references to the object (if defined)
You can also request subclasses of modules:
help(pymysql.connections)
You can use help to access the docstrings of the different modules you have imported, e.g., try the following:
>>> help(math)
and you'll get an error
>>> import math
GoalKicker.com – Python® Notes for Professionals 32
>>> help(math)
And now you will get a list of the available methods in the module, but only AFTER you have imported it.
Close the helper with quit"""

import math as m
print(help(m))
print(help(pow(2,3)))
# this give brifly information of math modules