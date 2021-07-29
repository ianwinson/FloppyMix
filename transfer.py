import os
from pathlib import Path
#This class transfers data from the floppy disks to several files on disk

import win32api 
def testDrive( currentLetter ):
    """
    Tests a given drive letter to see if the drive is question is ready for 
    access. This is to handle things like floppy drives and USB card readers
    which have to have physical media inserted in order to be accessed.
    Returns true if the drive is ready, false if not.
    """
    returnValue = False
    #This prevents Windows from showing an error to the user, and allows python 
    #to handle the exception on its own.
    oldError = win32api.SetErrorMode( 1 ) #note that SEM_FAILCRITICALERRORS = 1
    try:
        freeSpace = win32file.GetDiskFreeSpaceEx( letter )
    except:
        returnValue = False
    else:
        returnValue = True
    #restore the Windows error handling state to whatever it was before we
    #started messing with it:
    win32api.SetErrorMode( oldError )
    return returnValue


os.chdir(r"A:\\")
file = Path("A:\\track.txt")
num = -1
f=open('track.txt', 'r')
f.seek(0)
num = f.read(1)
if(file.exists()):
        f=open('track.txt', 'r')
        f.seek(0)
        num = f.read(1)

if(num == -1):
    0

print(str(int(num)))


dtf = open("C:\\Users\\iankr\\Documents\\Reader\\DiskData\\drive1.txt","w")
dtf.write(str(int(num)))
dtf.close()

os.chdir(r"B:\\")
file = Path("B:\\track.txt")
num = -1
f=open('track.txt', 'r')
f.seek(0)
num = f.read(1)
if(file.exists()):
        f=open('track.txt', 'r')
        f.seek(0)
        num = f.read(1)

if(num == -1):
    0

print(str(int(num)))


dtf = open("C:\\Users\\iankr\\Documents\\Reader\\DiskData\\drive2.txt","w")
dtf.write(str(int(num)))
dtf.close()

os.chdir(r"E:\\")
file = Path("E:\\track.txt")
num = -1
f=open('track.txt', 'r')
f.seek(0)
num = f.read(1)
if(file.exists()):
        f=open('track.txt', 'r')
        f.seek(0)
        num = f.read(1)

if(num == -1):
    0

print(str(int(num)))


dtf = open("C:\\Users\\iankr\\Documents\\Reader\\DiskData\\drive3.txt","w")
dtf.write(str(int(num)))
dtf.close()

os.chdir(r"F:\\")
file = Path("F:\\track.txt")
num = -1
f=open('track.txt', 'r')
f.seek(0)
num = f.read(1)
if(file.exists()):
        f=open('track.txt', 'r')
        f.seek(0)
        num = f.read(1)

if(num == -1):
    0

print(str(int(num)))


dtf = open("C:\\Users\\iankr\\Documents\\Reader\\DiskData\\drive4.txt","w")
dtf.write(str(int(num)))
dtf.close()





