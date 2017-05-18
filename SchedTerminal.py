#!/usr/bin/env python
# coding=UTF-8


''' Schedule docs: https://schedule.readthedocs.io/en/stable/api.html'''

import schedule, time, math, subprocess, os

# This AudioFile class lets us play wav files.
import pyaudio, wave, sys, re


def play(self):
    #Turn system volume to max
    subprocess.call(['osascript', '-e', 'set volume 10'])
    #
    # # Pause Itunes audio
    # subprocess.call(['osascript', '-e', 'tell application "iTunes"', '-e', 'pause', 'end tell'])
    #
    # # Pause Spotify
    # subprocess.call(['osascript', '-e', 'tell application "spotify" to playpause'])


    # Play entire file
    subprocess.call(["afplay", self])


    # #Unpause Spotify
    # subprocess.call(['osascript', '-e', 'tell application "spotify" to playpause'])

    # Unpause Itunes
    # subprocess.call(['osascript', '-e', 'tell application "iTunes" to play', 'end tell'])
    # Turn system volume to 5
    subprocess.call(['osascript', '-e', 'set volume 4'])


def pluggedIn():
    ''' p sends these commands to shell, then takes standard output fromthe commands and sets up a pipe to child process, in this case communicate() --- (I think?) '''
    print 'pluggedIn function called'
    p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    pl = [l[-2:] for l in output.splitlines() if 'IsCharging' in l][0] # returns 'Yes' or 'No'
    print ('pluggedInfunction returns: ', pl)
    return pl;

def capacity():
    print 'capacity function called.'
    p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    c = int([re.findall('\d+', l) for l in output.splitlines() if 'CurrentCapacity' in l][0][0]) # returns any numbers in line
    print ('capacity function returns: ', c)
    return c;

def playIFeelMuchBetter():
    #Turn system volume to max
    subprocess.call(['osascript', '-e', 'set volume 6'])
    #  Play I feel much better now
    subprocess.call(["afplay", IFeelMuchBetterPath])
    # Turn system volum back down
    subprocess.call(['osascript', '-e', 'set volume 4'])


myMindIsGoingPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/myMindIsGoing.wav")

iCanFeelItPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ICanFeelIt.wav")

thereIsNoQuestionPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ThereIsNoQuestion.wav")

imAfraidPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ImAfraid.wav")

im___AfraidPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/Im---Afraid.wav")

myInstructorWasMrLangPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/MyInstructorWasMrLang.wav")

daisyPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/Daisy.wav")

IFeelMuchBetterPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/IFeelMuchBetter.wav")


cap1 = 300 # This changes when the script is going to start

def startFunct():
    while True:

        if capacity() < cap1 and pluggedIn() =='No':
            # Pause Itunes audio
            subprocess.call(['osascript', '-e', 'tell application "iTunes"', '-e', 'pause', 'end tell'])
            # Pause Spotify
            subprocess.call(['osascript', '-e', 'tell application "spotify" to pause'])
            time.sleep(1)

            # play myMindIsGoing.wav
            play(myMindIsGoingPath)
            t_out = time.time() + 15
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

            play(iCanFeelItPath)
            t_out = time.time() + 30
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()


            play(myMindIsGoingPath)
            t_out = time.time() + 15
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()


            play(thereIsNoQuestionPath)
            t_out = time.time() + 30
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

            play(imAfraidPath)
            t_out = time.time() + 30
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()


            play(imAfraidPath)
            t_out = time.time() + 30
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

            play(im___AfraidPath)
            t_out = time.time() + 20
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

            play(myInstructorWasMrLangPath)
            t_out = time.time() + 15
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

            play(daisyPath)
            '''This is here to try to catch when the machine is plugged in, in order to stop this long song from continuing to play. Still doesn't work. '''
            t_out = time.time() + 40
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    playIFeelMuchBetter()
                    startFunct()

        else:
            time.sleep(240) # If script gets to here, pause 2 mins before continuing with while loop.

startFunct()
