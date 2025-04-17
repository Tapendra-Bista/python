"""Note: Following instructions are written for Python 2.7 (unless specified): instructions for Python 3.x are
similar.
Windows
First, download the latest version of Python 2.7 from the official Website (https://www.python.org/downloads/).
Version is provided as an MSI package. To install it manually, just double-click the file.
By default, Python installs to a directory:
 C:\Python27\
Warning: installation does not automatically modify the PATH environment variable.
Assuming that your Python installation is in C:\Python27, add this to your PATH:
GoalKicker.com – Python® Notes for Professionals 27
C:\Python27\;C:\Python27\Scripts\
Now to check if Python installation is valid write in cmd:
python --version
Python 2.x and 3.x Side-By-Side
To install and use both Python 2.x and 3.x side-by-side on a Windows machine:
Install Python 2.x using the MSI installer.1.
Ensure Python is installed for all users.
Optional: add Python to PATH to make Python 2.x callable from the command-line using python.
Install Python 3.x using its respective installer.2.
Again, ensure Python is installed for all users.
Optional: add Python to PATH to make Python 3.x callable from the command-line using python. This
may override Python 2.x PATH settings, so double-check your PATH and ensure it's configured to your
preferences.
Make sure to install the py launcher for all users.
Python 3 will install the Python launcher which can be used to launch Python 2.x and Python 3.x interchangeably
from the command-line:
P:\>py -3
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
C:\>py -2
Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
To use the corresponding version of pip for a specific Python version, use:
C:\>py -3 -m pip -V
pip 9.0.1 from C:\Python36\lib\site-packages (python 3.6)
C:\>py -2 -m pip -V
pip 9.0.1 from C:\Python27\lib\site-packages (python 2.7)
Linux
The latest versions of CentOS, Fedora, Red Hat Enterprise (RHEL) and Ubuntu come with Python 2.7.
To install Python 2.7 on linux manually, just do the following in terminal:
wget --no-check-certificate https://www.python.org/ftp/python/2.7.X/Python-2.7.X.tgz
tar -xzf Python-2.7.X.tgz  
cd Python-2.7.X
./configure  
make  
GoalKicker.com – Python® Notes for Professionals 28
sudo make install
Also add the path of new python in PATH environment variable. If new python is in /root/python-2.7.X then run
export PATH = $PATH:/root/python-2.7.X
Now to check if Python installation is valid write in terminal:
python --version
Ubuntu (From Source)
If you need Python 3.6 you can install it from source as shown below (Ubuntu 16.10 and 17.04 have 3.6 version in
the universal repository). Below steps have to be followed for Ubuntu 16.04 and lower versions:
sudo apt install build-essential checkinstall
sudo apt install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-
dev libc6-dev libbz2-dev
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
tar xvf Python-3.6.1.tar.xz
cd Python-3.6.1/
./configure --enable-optimizations
sudo make altinstall
macOS
As we speak, macOS comes installed with Python 2.7.10, but this version is outdated and slightly modified from the
regular Python.
The version of Python that ships with OS X is great for learning but it’s not good for development. The
version shipped with OS X may be out of date from the official current Python release, which is
considered the stable production version. (source)
Install Homebrew:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Install Python 2.7:
brew install python
For Python 3.x, use the command brew install python3 instead"""