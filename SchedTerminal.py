#!/usr/bin/env python
# coding=UTF-8

''' Somehow you have to make this script run everytime the machine boots up, either with crontab or .plist files.
Eventually I should try to make a 'play' function that I would call with each sound file. '''
''' Schedule docs: https://schedule.readthedocs.io/en/stable/api.html'''

import schedule, time, math, subprocess, os

# This AudioFile class lets us play wav files.
import pyaudio
import wave
import sys



print 'Started \'job\''
cap1 = 350 # This changes when the script is going to start

def play(self):
    #Turn system volume to max
    subprocess.call(['osascript', '-e', 'set volume 100'])

    # Pause Itunes audio
    subprocess.call(['osascript', '-e', 'tell application "iTunes"', '-e', 'pause', 'end tell'])

    # Pause Spotify
    subprocess.call(['osascript', '-e', 'tell application "Spotify"', '-e', 'pause', 'end tell'])




    # Play entire file
    subprocess.call(["afplay", self])

    # Unpause vlc, chrome

    #Unpause Spotify
    subprocess.call(['osascript', '-e', 'tell application "Spotify"', '-e', 'play', 'end tell'])

    # Unpause Itunes
    subprocess.call(['osascript', '-e', 'tell application "iTunes" to play', 'end tell'])
    # Turn system volume to 5
    subprocess.call(['osascript', '-e', 'set volume 30'])


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
    c = int(round(int([l[-4:] for l in output.splitlines() if 'CurrentCapacity' in l][0]), -1)) # returns 4 digit number
    print ('capacity function returns: ', c)
    return c;


while True:
    if capacity() < cap1 and pluggedIn() =='No':
        # play myMindIsGoing.wav
        myMindIsGoingPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/myMindIsGoing.wav")
        play(myMindIsGoingPath)
        t_out = time.time() + 40
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break  # returns control to while statement

        iCanFeelItPath =
        os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ICanFeelIt.wav")
        play(iCanFeelItPath)
        t_out = time.time() + 60
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break # returns control to while statement

        myMindIsGoingPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/myMindIsGoing.wav")
        play(myMindIsGoingPath)
        t_out = time.time() + 40
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break # returns control to while statement

        thereIsNoQuestionPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ThereIsNoQuestion.wav")
        play(thereIsNoQuestionPath)
        t_out = time.time() + 60
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break # returns control to while statement

        imAfraidPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ImAfraid.wav")
        play(imAfraidPath)
        t_out = time.time() + 40
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break  # returns control to while statement

        imAfraidPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/ImAfraid.wav")
        play(imAfraidPath)
        t_out = time.time() + 40
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break  # returns control to while statement

        im---AfraidPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/Im---Afraid.wav")
        play(im---AfraidPath)
        t_out = time.time() + 60
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn()!= 'No':
                break  # returns control to while statement

        myInstructorWasMrLangPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/MyInstructorWasMrLang.wav")
        play(myInstructorWasMrLangPath)
        '''This is here to try to catch when the machine is plugged in, in order to stop this longish phrase from continuing to play. Still doesn't work.  '''
        t_out = time.time() + 30
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn() != 'No':
                break  # returns control to while statement

        daisyPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/Daisy.wav")
        play(daisyPath)
        '''This is here to try to catch when the machine is plugged in, in order to stop this long song from continuing to play. Still doesn't work. '''
        t_out = time.time() + 60
        while time.time() < t_out:
            time.sleep(1)
            if pluggedIn() != 'No':
                break  # returns control to while statement

        # Check if plugged in and play IFeelMuchBetter.wav & reset
        # played variables, if so
        if pluggedIn() != 'No' and capacity() < cap1:
            IFeelMuchBetterPath = os.path.abspath("/Users/evanhendrix1/Google Drive/programming/python/Sched_Proj/IFeelMuchBetter.wav")
            play(IFeelMuchBetterPath)
            break # returns control to if statement
        else:
            continue  # executed if the loop ended normally (no break)
        break  # executed if 'continue' was skipped (break)

    else:
        time.sleep(120) # If script gets to here, pause 2 mins before continuing with while loop.
        break
