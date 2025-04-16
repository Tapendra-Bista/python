"""
IDLE is Python’s Integrated Development and Learning Environment and is an alternative to the command line. As
the name may imply, IDLE is very useful for developing new code or learning python. On Windows this comes with
the Python interpreter, but in other operating systems you may need to install it through your package manager.

The main purposes of IDLE are:
Multi-window text editor with syntax highlighting, autocompletion, and smart indent
Python shell with syntax highlighting
Integrated debugger with stepping, persistent breakpoints, and call stack visibility
Automatic indentation (useful for beginners learning about Python's indentation)
GoalKicker.com – Python® Notes for Professionals 20
Saving the Python program as .py files and run them and edit them later at any them using IDLE.
In IDLE, hit F5 or run Python Shell to launch an interpreter. Using IDLE can be a better learning experience for
new users because code is interpreted as the user writes.
Note that there are lots of alternatives, see for example this discussion or this list.

Troubleshooting
Windows
If you're on Windows, the default command is python. If you receive a "'python' is not recognized" error,
the most likely cause is that Python's location is not in your system's PATH environment variable. This can be
accessed by right-clicking on 'My Computer' and selecting 'Properties' or by navigating to 'System' through
'Control Panel'. Click on 'Advanced system settings' and then 'Environment Variables...'. Edit the PATH variable
to include the directory of your Python installation, as well as the Script folder (usually
C:\Python27;C:\Python27\Scripts). This requires administrative privileges and may require a restart.
When using multiple versions of Python on the same machine, a possible solution is to rename one of the
python.exe files. For example, naming one version python27.exe would cause python27 to become the
Python command for that version.
You can also use the Python Launcher for Windows, which is available through the installer and comes by
default. It allows you to select the version of Python to run by using py -[x.y] instead of python[x.y]. You
can use the latest version of Python 2 by running scripts with py -2 and the latest version of Python 3 by
running scripts with py -3.

Debian/Ubuntu/MacOS
This section assumes that the location of the python executable has been added to the PATH environment
variable.
If you're on Debian/Ubuntu/MacOS, open the terminal and type python for Python 2.x or python3 for Python
3.x.
Type which python to see which Python interpreter will be used.

Arch Linux
The default Python on Arch Linux (and descendants) is Python 3, so use python or python3 for Python 3.x and
python2 for Python 2.x.

Other systems
Python 3 is sometimes bound to python instead of python3. To use Python 2 on these systems where it is
installed, you can use python2






"""