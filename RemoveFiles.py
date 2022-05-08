import os
import shutil

time = os.system("time")
date = os.system("days")

path = ""
isExist = os.path.exists(path)
print(isExist)

listOfFiles = os.listdir(path)

ctime = os.stat(path).st_ctime
return ctime