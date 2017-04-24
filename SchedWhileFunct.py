#!/usr/bin/env python
# coding=UTF-8

''' Somehow you have to make this script run everytime the machine boots up, either with crontab or .plist files '''

import schedule, time, math, subprocess

# This AudioFile class lets us play wav files.
import pyaudio
import wave
import sys

# Global variables
increment = 25
time1 = 350
time2 = time1 - increment
time3 = time2 - increment
time4 = time3 - increment
time5 = time4 - increment
time6 = time5 - increment
time7 = time6 - increment
time8 = time7 - increment
time9 = time8 - increment
time10 = time9 - increment
time11 = time10 - increment

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Turn system volume to max """
        #from subprocess import call
        subprocess.call(['osascript', '-e', 'set volume 10'])

        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)
        """ Turn system volume to 5 """
        #from subprocess import call
        subprocess.call(['osascript', '-e', 'set volume 3'])


    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.p.terminate()

def pluggedIn():
    print 'pluggedIn function called'
    p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    pl = [l[-2:] for l in output.splitlines() if 'IsCharging' in l][0]
    print ('pluggedInfunction returns: ', pl)
    return pl;

def capacity():
    print 'capacity function called.'
    p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
    output = p.communicate()[0]
    c = int(round(int([l[-4:] for l in output.splitlines() if 'CurrentCapacity' in l][0]), 0))
    print ('capacity function returns: ', c)
    return c;

played1=played2=played3=played4=played5=played6=played7=played8=played9=played10=played11 = False
feelBetPlayed = False

def job():

    while True:

        while (not played1):
            time.sleep(1)

            print '1 ', pluggedIn()
            print '1 ', capacity()

            if capacity() < time1 and capacity() >= time2 and pluggedIn() == 'No':
                # play myMindIsGoing.wav
                a = AudioFile("MyMindIsGoing.wav")
                a.play()
                a.close()
                played1 = True
            else:
                break

        while (not played2):
            time.sleep(1)

            print '2 ', pluggedIn()
            print '2 ', capacity()

            if capacity() < time2 and capacity() >= time3 and pluggedIn() == 'No':
                a = AudioFile("ICanFeelIt2.wav")
                a.play()
                a.close()
                played2 = True
            else:
                break

        while (not played3):
            time.sleep(1)

            print '3 ', pluggedIn()
            print '3 ', capacity()

            if capacity() < time3 and capacity() >= time4 and pluggedIn() == 'No':
                a = AudioFile("MyMindIsGoing.wav")
                a.play()
                a.close()
                played3 = True
            else:
                break

        while (not played4):
            time.sleep(1)

            print '4 ', pluggedIn()
            print '4 ', capacity()

            if capacity() < time4 and capacity() >= time5 and pluggedIn() == 'No':
                a = AudioFile("ThereIsNoQuestion.wav")
                a.play()
                a.close()
                played4 = True
            else:
                break

        while (not played5):
            time.sleep(1)

            print '5 ', pluggedIn()
            print '5 ', capacity()

            if capacity() < time5 and capacity() >= time6 and pluggedIn() == 'No':
                a = AudioFile("ImAfraid1.wav")
                a.play()
                a.close()
                played5 = True
            else:
                break

        while (not played6):
            time.sleep(1)

            print '6 ', pluggedIn()
            print '6 ', capacity()

            if capacity() < time6 and capacity() >= time7 and pluggedIn() == 'No':
                a = AudioFile("ImAfraid1.wav")
                a.play()
                a.close()
                played6 = True
            else:
                break

        while (not played7):
            time.sleep(1)

            print '7 ', pluggedIn()
            print '7 ', capacity()

            if capacity() < time7 and capacity() >= time8 and pluggedIn() == 'No':
                a = AudioFile("ImAfraid1.wav")
                a.play()
                a.close()
                played7 = True
            else:
                break

        while (not played8):
            time.sleep(1)

            print '8 ', pluggedIn()
            print '8 ', capacity()

            if capacity() < time8 and capacity() >= time9 and pluggedIn() == 'No':
                a = AudioFile("Im---Afraid.wav")
                a.play()
                a.close()
                played8 = True
            else:
                break

        while (not played9):
            time.sleep(1)

            print '9 ', pluggedIn()
            print '9 ', capacity()

            if capacity() < time9 and capacity() >= time10 and pluggedIn() == 'No':
                a = AudioFile("MyInstructorWasMrLang.wav")
                a.play()
                timeOut = time.time() + 30
                while pluggedIn() == 'No' and time.time() < timeOut:
                    time.sleep(1)
                a.close()
                played9 = True
                break
            else:
                break

        while (not played10):
            time.sleep(1)

            print '10 ', pluggedIn()
            print '10 ', capacity()

            if capacity() < time10 and capacity() >= time11 and pluggedIn() == 'No':
                a = AudioFile("Daisy.wav")
                timeOut = time.time() + 30
                a.play()
                played10 = True
                while pluggedIn() == 'No' and time.time() < timeOut:
                    time.sleep(1)
                a.close()

            else:
                break

        # Check if plugged in and play IFeelMuchBetter.wav & reset
        # played variables, if so
        if pluggedIn() != 'No' and capacity() < time1 and feelBetPlayed == False :
            a = AudioFile("IFeelMuchBetterNow.wav")
            a.play()
            a.close()
            played1=played2=played3=played4=played5=played6=played7=played8=played9=played10=played11 = False
            feelBetPlayed = True
            break
        else:
            continue  # executed if the loop ended normally (no break)
        break  # executed if 'continue' was skipped (break)

    print 'Nada que ver...La bateria no esta baja.'
