cd /d "C:\Users\iankr\Documents\Reader\FloppyMix"
python transfer.py
wsl.exe python3 liveInterface.py 
echo DONE - waiting for changes 
python scanForChange.py
