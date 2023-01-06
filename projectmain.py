import time
from playsound import playsound

def PlayS(a):
    playsound(a)

while(True):
    time.sleep(600)
    PlayS('sound.mp3')
    

# code to remind to take a break every 10 minutes.