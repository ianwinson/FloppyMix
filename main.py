import os
from pathlib import Path
from playsound import playsound
from pygame import mixer
import sys, time, msvcrt

timeout = 15

os.chdir(r"A:\\")
file = Path("A:\\track.txt")
mixer.init()

while(1):
    input("Press Enter to Play Sound")
    if(file.exists()):
        f=open('track.txt', 'r')
        f.seek(0)
        num = f.read(1)
        a = "E:\\music\\music"
        c = ".mp3"
        path = a + str(int(num)) + c 
        path2 = "music" + str(int(num)) + ".mp3"
        print("Playing Sample #" + str(int(num)))
        # playsound(path)
        mixer.music.load(path)
        mixer.music.play()

        startTime = time.time()
        inp = None
        
        # input("Playing sound. Press enter to stop")
        # mixer.music.pause() 
        while True:
            if msvcrt.kbhit():
                inp = msvcrt.getch()
                break
            elif time.time() - startTime > timeout:
                break

        if inp:
            print("Music stopped by user")
        else:
            print("Music auto-stopped after 15 sec")
      
        mixer.music.pause() 
        # playsound(r'C:\Users\PROGRAMING\Documents\Floppy\one.mp3')
        # print("Sound 1")



print("test")
