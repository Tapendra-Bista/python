# A module is an importable file containing definitions and statements
# A modules can be created by creating a .py file
import module
import module as m

from module import sayHello
module.sayHello()
m.sayHello()


# we can also import only funtion only to
sayHello()

# we can also make this file as module for another file

# For modules that you have made, they will need to be in the same directory as the file that you are importing them
#into

# If the module is inside a directory and
#  needs to be detected by python, the
#  directory should contain a file named
#__init__.py
from guessNumber import display
