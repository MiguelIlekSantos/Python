import os
import shutil

try:
    path = "ola2"
    #os.remove(path) # Only removes file not a directory
    #os.rmdir(path) # Only removes directory if there is no file inside
    shutil.rmtree(path) #Removes a directory with everthing inside || Harmful to use sometime
except FileNotFoundError:
    print("That file Was not found")
except PermissionError:
    print("You dont have permission to do this")
except OSError:
    print("you cannot delete this file using this Function")
else:
    print(path + "was Deleted")