# Chapter 31: os.path

# join
# used to join two or more path components 
import os
result = os.path.join('x.txt', 'y.txt', 'z.txt')

print("path combine :",result)


# Section 31.2: Path Component Manipulation
p = os.path.join(os.getcwd(),"content.txt")
print("current working directory :",os.getcwd())
print("full path :",p)
print("base name :", os.path.basename(p))
print("dir name :",os.path.dirname(p))
print("split :", os.path.split(p))

#Section 31.4: If the given path exists
example_path = "Users\lenovo\Documents\python\content.txt"
result = os.path.exists(example_path)
if result:
    print(f"The path {example_path} exists.")

else :
    print(f"The path {example_path} does not exists.")


# Section 31.5: check if the given path is a directory, file,
#symbolic link, mount point etc

path  = "Home/john/Documents"

# check if the given path is a directory  or not
if os.path.isdir(path):
    print(f"The paht {path} is a direcyory.")
else:
        print(f"The path {path} is not a directory.")

        # check if the given path is a file or not
if os.path.isfile(path+"/31.py"):
    print(f"The path {path} is a file>")
else:
    print(f"The path {path} is not a file.")

# check if the given path is a symbolic link or not
if os.path.islink(path+"https://www.geeksforgeeks.org/"):
    print(f"The path {path} is a symbolic link.")
else:
    print(f"The path {path } is not a symbolic link.")    

# Section 31.6: Absolute Path from Relative Path     
# directory of the current 
directory = os.getcwd()
print("Current working directory :",directory)

if os.path.isabs(directory+"/31.py"):
    print("The given path is absolute path.")
else:
    print("The given path is not absolute path.")
    print("Absolute path :",os.path.abspath("31.py"))