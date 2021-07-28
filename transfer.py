import os
from pathlib import Path
#This class transfers data from the floppy disks to several files on disk
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
