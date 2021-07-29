import os
import subprocess
from pathlib import Path

##detect removal of floppy
while(1):
    try:
        print("testing")
        os.chdir(r"A:\\")
        os.chdir(r"B:\\")
        os.chdir(r"E:\\")
        os.chdir(r"F:\\")
    except PermissionError:
        break

##wait for insertion of new floppy before running batch     
while(1):
     try:
        os.chdir(r"A:\\")
        os.chdir(r"B:\\")
        os.chdir(r"E:\\")
        os.chdir(r"F:\\")
        break
     except PermissionError:
        print("waiting for new floppy")

subprocess.call([r"C:\\Users\\iankr\Documents\\Reader\\FloppyMix\\initial.bat"])
