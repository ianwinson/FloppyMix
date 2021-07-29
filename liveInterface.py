#------------------------------------------------------------------------
# Basic example of pylive usage: scan a Live set, trigger a clip,
# and modulate some device parameters.
#------------------------------------------------------------------------
import live
import random
import os
from pathlib import Path

#ADD IN FLOPPY
os.chdir(r"/mnt/c/Users/iankr/Documents/Reader/DiskData/")
file = Path("/mnt/c/Users/iankr/Documents/Reader/DiskData/drive1.txt")
if(file.exists()):
        f=open('drive1.txt', 'r')
        f.seek(0)
        num1 = f.read(1)
        print(num1)
file = Path("/mnt/c/Users/iankr/Documents/Reader/DiskData/drive2.txt")
if(file.exists()):
        f=open('drive2.txt', 'r')
        f.seek(0)
        num2 = f.read(1)
        print(num2)
file = Path("/mnt/c/Users/iankr/Documents/Reader/DiskData/drive3.txt")
if(file.exists()):
        f=open('drive3.txt', 'r')
        f.seek(0)
        num3 = f.read(1)
        print(num3)
file = Path("/mnt/c/Users/iankr/Documents/Reader/DiskData/drive4.txt")
if(file.exists()):
        f=open('drive4.txt', 'r')
        f.seek(0)
        num4 = f.read(1)
        print(num4)

#------------------------------------------------------------------------
# Scan the set's contents and set its tempo to 110bpm.
#------------------------------------------------------------------------
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
set.tempo = 120.0

#------------------------------------------------------------------------
# Each Set contains a list of Track objects.
#------------------------------------------------------------------------
print(set)
track = set.tracks[0]
track1 = set.tracks[1]
track2 = set.tracks[2]
track3 = set.tracks[3]
print("Track name %s" % track.name)
print("Track1 name %s" % track1.name)

#------------------------------------------------------------------------
# Each Track contains a list of Clip objects.
#------------------------------------------------------------------------

clip2 = track.clips[int(num1) - 1]
clip3 = track1.clips[int(num2) - 1]
clip4 = track2.clips[int(num3) - 1]
clip5 = track3.clips[int(num4) - 1]
clip2.play()
clip3.play()
clip4.play()
clip5.play()
# set.wait_for_next_beat()
# clip2.stop()

# clip = track.clips[0]
# print("Clip name %s, length %d beats" % (clip.name, clip.length))
# clip.play()

#------------------------------------------------------------------------
# We can determine our internal timing based on Live's timeline using
# Set.wait_for_next_beat(), and trigger clips accordingly.
#------------------------------------------------------------------------
# set.wait_for_next_beat()
# clip.get_next_clip().play()

#------------------------------------------------------------------------
# Now let's modulate the parameters of a Device object.
#------------------------------------------------------------------------
# device = track.devices[0]
# parameter = random.choice(device.parameters)
# parameter.value = random.uniform(parameter.minimum, parameter.maximum)