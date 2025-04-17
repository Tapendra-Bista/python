"""pip is your friend when you need to install any package from the plethora of choices available at the python
package index (PyPI). pip is already installed if you're using Python 2 >= 2.7.9 or Python 3 >= 3.4 downloaded from
python.org. For computers running Linux or another *nix with a native package manager, pip must often be
manually installed.
GoalKicker.com – Python® Notes for Professionals 30
On instances with both Python 2 and Python 3 installed, pip often refers to Python 2 and pip3 to Python 3. Using
pip will only install packages for Python 2 and pip3 will only install packages for Python 3.
Finding / installing a package
Searching for a package is as simple as typing
$ pip search <query>
# Searches for packages whose name or summary contains <query>
Installing a package is as simple as typing (in a terminal / command-prompt, not in the Python interpreter)
$ pip install [package_name]           # latest version of the package
$ pip install [package_name]==x.x.x    # specific version of the package
$ pip install '[package_name]>=x.x.x'  # minimum version of the package
where x.x.x is the version number of the package you want to install.
When your server is behind proxy, you can install package by using below command:
$ pip --proxy http://<server address>:<port> install
Upgrading installed packages
When new versions of installed packages appear they are not automatically installed to your system. To get an
overview of which of your installed packages have become outdated, run:
$ pip list --outdated
To upgrade a specific package use
$ pip install [package_name] --upgrade
Updating all outdated packages is not a standard functionality of pip.
Upgrading pip
You can upgrade your existing pip installation by using the following commands
On Linux or macOS X:
$ pip install -U pip
You may need to use sudo with pip on some Linux Systems
On Windows:
py -m pip install -U pip
or
python -m pip install -U pip
"""

# pip install package_name

from PIL import Image
from rembg import remove

input_image = Image.open("spider.jpg")
output = remove(input_image)

output.save("output.jpg")
output.show()
