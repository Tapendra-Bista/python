# section 30.1 File modes
###
# There are many modes  you can use open  a file with, specified by the  mode parameter 
#  'r'- reading mode , file must exit
from nt import read


with open('r.txt','r') as obj:
     result = obj.read()
     print("String from (r.txt) file:",result)
#  'w'- write mode , it will create new file if it does not exsit
with open('w.txt','w') as obj:
     my_string = "This is an example of w.text"
     obj.write(my_string)
#  'a'- append mode, it will write data to the end of the file.
with  open('w.txt','a') as obj:
    value = "\tThis is an append string ,for this  file must be already exist"
    obj.write(value)
# 'rb'- read mode in binary
#  'r+'- reading  mode pluse writing mode 
with open ('rplus.txt','r+') as obj :
          # read demo
     print(obj.read())
     obj.write("r plus write testing after read demo test 333333333334444444")

# in R+  must be read first and write 


    
# 'rb+'- reading mode pluse writing mode in binary
# 'wb'- writing mode in binary
# 'w+'- writing and reading mode 
#Example 
with open("wplus.txt",'w+') as obj :
     # writting at first 
     
     obj.write("This is an example of w+ where we first write after that we can read file simple.")
     # Reading now
     obj.seek(0)
     result = obj.read()
     print("Print : "+result)

# 'wb+'- Writing mode and reading mode in binary
#  'ab'- appednding in binary mode
#  'a+'- appending and reading mode
#Example 
with open('aplus.txt','a+')  as obj:

     # appending
     obj.write('Tapendra Bista from ktm.')

     # Reading
     obj.seek(0)
     result = obj.read()
     print("Print from aplus.txt file : "+result)

# 'ab+'- appending and reading mode in binary   ###


# Binary file modes demo: rb, wb, ab, rb+, wb+, ab+, xb

def hexdump(b: bytes, width=16):
    for i in range(0, len(b), width):
        chunk = b[i:i+width]
        print(f"{i:04x}: {chunk.hex(' ')}")

# 1) wb: write (create/truncate) binary file
with open("sample.bin", "wb") as f:
    data = bytes([0xDE, 0xAD, 0xBE, 0xEF]) + "Hello".encode("utf-8")
    f.write(data)
print("After wb -> sample.bin contents:")
with open("sample.bin", "rb") as f:
    content = f.read()
    hexdump(content)

# 2) ab: append to binary file (adds to end)
with open("sample.bin", "ab") as f:
    f.write(b"\x00\x01\x02\x03")
print("\nAfter ab -> sample.bin contents:")
with open("sample.bin", "rb") as f:
    content = f.read()
    hexdump(content)

# 3) rb+: read/write without truncation
with open("sample.bin", "rb+") as f:
    head4 = f.read(4)
    print("\nrb+ first 4 bytes:", head4.hex(" "))
    f.seek(0)           # overwrite header
    f.write(b"HEAD")    # 4 bytes
print("After rb+ overwrite -> sample.bin contents:")
with open("sample.bin", "rb") as f:
    content = f.read()
    hexdump(content)

# 4) wb+: write/read with truncate
with open("scratch.bin", "wb+") as f:
    f.write(b"ABCDEF")
    f.seek(0)           # move to start to read
    print("\nwb+ read:", f.read())

# 5) ab+: append/read combined
with open("scratch.bin", "ab+") as f:
    f.write(b"ZZ")
    f.seek(0)
    print("ab+ full read:", f.read())

# 6) xb: exclusive creation (fails if file exists)
try:
    with open("exclusive.bin", "xb") as f:
        f.write(b"created once")
    print("\nxb: exclusive.bin created")
except FileExistsError:
    print("\nxb: exclusive.bin already exists (exclusive create failed)")

# Notes:
# - Always use 'b' in mode when working with bytes.
# - On Windows, text mode may translate newlines; binary mode does not.
# - Use seek(0) before reading after writing in + modes.



##                       r        r+      w        w+     a      a+
# Read                  ✓         ✓      ✕        ✓     ✕     ✓
# Write                 ✕         ✓      ✓        ✓     ✓     ✓
# Creates file          ✕         ✕     ✓         ✓    ✓      ✓
# Erases file           ✕        ✕     ✓          ✓    ✕     ✕
# Initial position       S        S      S        S       E      E      
# ##


####
# Python 3 added a new mode for exclusive creation so that you will not accidentally truncate or overwrite and
# existing file.
# 'x' - open for exclusive creation, will raise FileExistsError if the file already exists
# 'xb' - open for exclusive creation writing mode in binary. The same as x except the data is in binary.
# 'x+' - reading and writing mode. Similar to w+ as it will create a new file if the file does not exist. Otherwise,
# will raise FileExistsError.
# 'xb+' - writing and reading mode. The exact same as x+ but the data is binary
# x x+
# Read ✘ ✔
# Write ✔ ✔
# Creates file ✔ ✔
# Erases file ✘ ✘
# Initial position Start Start
####

# Section 30.2: Reading a file line-by-line
# There are several ways to read a file line-by-line in Python. Here are some common methods:
# Method 1: Using a for loop
with open('r.txt','r') as obj :
     for line in obj:
          print("From r.text file : "+ line.strip())

# Method 2: Using readline()
with open('r.txt','r') as obj :
     while True:
          line = obj.readline()
          if not line:
               break
          print("From r.text file : "+ line.strip())


 # Method 3: Using readlines()
with open('r.txt','r') as obj :
     lines = obj.readlines()
     for line in lines:
          print("From r.text file : "+ line.strip())


# Section 30.4: Getting the full contents of a file
with open('content.txt','r') as obj :
     content = obj.read()
     print("\n\n\nFull content of content.text file : \n\n"+ content,end="\n\n")



# Section 30.5: Writing to a file
with open("newfile.txt", 'w') as file:
     file.write("Line one ")
     file.write(" Line two")
     file.write(" Line three")
     # Print be like Line one Line two Line three
     # for new line use \n
     file.write("\nLine four\n")
     file.write("Line five\n")
     file.write("Line six'\n")
     # print be like
     # Line one Line two Line three
     # Line four
     # Line five
     # Line six

# Section 30.6: Check whether a file or path exists
import os
import pathlib as pathlib

if os.path.exists("newfile.txt"):
     print("File exists")
else:
     print("File does not exist")


path = pathlib.Path("newfilex.txt")

if path.is_file():
     print("File exists")
else:
     print("File does not exist")


#Section 30.7: Random File Access Using mmap     
import mmap
with open("mmap.txt",'r') as file :
     # map  whole file 
     mmapped_file = mmap.mmap(file.fileno(),0,access=mmap.ACCESS_READ)
     mmapped_file.seek(0)
     print(mmapped_file[0:30],end="\n\n")
     print(mmapped_file.readline(),end="\n\n")
     mmapped_file.close()

# Section 30.8: Replacing text in a file
import fileinput
with fileinput.FileInput('replace.txt',inplace=True,backup='.bak') as file :
     for line in file :
          print(line.replace('tapendra',"Tapendra Bista new line"))   


# Section 30.9: Checking if a file is empty
# Method 1: Using os.path.getsize()
import os
if os.path.getsize("replace.txt") == 0:
     print("File is empty")
else :
     print("File is not empty")


# Method 2: Using pathlib.Path.stat()
if os.stat("r.txt").st_size == 0:
     print("File is empty")
else :
     print("File is not empty")


#Section 30.10: Read a file between a range of lines
import itertools
with open('content.txt','r') as file :
     for line in itertools.islice(file,4,5):
          print(line,end="")


# Section 30.12: Copying contents of one file to a dierent file
with open("in_file.txt",'r') as infile , open("out_file.txt",'w') as outfile :
     for line in infile :
          outfile.write(line)
          print("File copy completed")

# using shutil
import shutil
shutil.copyfile("src.txt","dst.txt")