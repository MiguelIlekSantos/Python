# copyfile() = copies content of a file
# copy() = copyfile()  + permission mode + destination can be a directory
#copy2 = copy() + copies metadata(file's creation and modification times)

import shutil

shutil .copyfile('hello','hello1')
shutil .copy('hello','hello1')
shutil .copy2('hello','hello1')