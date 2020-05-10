"""
os module provides us many useful methods to work with directories
1. Get Current Working Directory
2.Change directory
3. Listing Directories and Files
"""

import os

print(os.getcwd())

os.chdir("/home/hrushikesh/python_notes/numpy")
print(os.getcwd())

print(os.listdir(os.getcwd()))

os.mkdir(os.getcwd()+'test')
os.mkdir(os.getcwd()+'del_later')
print(os.listdir(os.getcwd()))

os.rename(os.getcwd()+'test',os.getcwd()+'new_name')
os.removedirs(os.getcwd()+'del_later')
print(os.listdir(os.getcwd()))
#In order to remove a non-empty directory we can use the rmtree() method inside the shutil module.import shutil
#shutil.rmtree('test')









