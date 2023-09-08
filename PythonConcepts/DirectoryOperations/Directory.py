import os

# # specify the path for the directory – make sure to surround it with quotation marks
# path = './projects'

# # The os.mkdir() method does not let you create a subdirectory. Instead, it lets you create a single directory.
# os.mkdir(path)

# # To create a nested directory structure (such as a directory inside another directory), use the os.makedirs() method.
# path = './projects/games/game01'

# os.makedirs(path)

# # when the directory  to create already exists a FileExistsError exception is raised
# # to handle this exception is to check if the file already exists or using try/catch 

# path = './projects'

# # check whether directory already exists
# if not os.path.exists(path):
#   os.mkdir(path)
#   print("Folder %s created!" % path)
# else:
#   print("Folder %s already exists" % path)
  
  
# try:
#     os.mkdir(path)
#     print("Folder %s created!" % path)
# except FileExistsError:
#     print("Folder %s already exists" % path)


# # listing directories
# print("The dir is: %s",os.listdir(os.getcwd()))

# # renaming directory ''tutorialsdir"
# os.rename("project","projects")

os.chdir("/home/asplap2314/Learnings/PythonConcepts")
os.rmdir( "test"  ) # it will delete directory if it is empty

# To Delete Non-Empty Directory
import shutil

shutil.rmtree('test')

#Note:

# By default, The shutil.rmtree() will fail to delete the directory containing any read-only files.

# It will throw a PermissionError if a folder contains any read-only files. Set the optional argument ignore_errors to True to remove the remaining folder contents.

#To Delete Non-Empty Directory 

import shutil

# remove old account directory
shutil.rmtree('Test')


# Note:

# By default, The shutil.rmtree() will fail to delete the directory containing any read-only files.

# It will throw a PermissionError if a folder contains any read-only files. Set the optional argument ignore_errors to True to remove the remaining folder contents.


# Todelete directory with read only files

# Use the onerror parameter of a shutil.rmtree() function to delete an entire directory that contains some read-only files.

# We need to write a custom function and assign it to the onerror parameter. This custom function uses the onerror callback to clear the read-only bit from a read-only file and again reattempt the remove.


import stat

# remove directory with read-only files
def rm_dir_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree("test", onerror=rm_dir_readonly)
