#! /usr/bin/env python
# coding=UTF-8

''' Somehow you have to make this script run everytime the machine boots up, either with crontab or .plist files '''
''' Schedule docs: https://schedule.readthedocs.io/en/stable/api.html'''

import schedule, time, math, subprocess

# This AudioFile class lets us play wav files.
import pyaudio
import wave
import sys
import re


def job():
    print 'Started \'job\'', time.time()
    cap1 = 350 # This changes then the script is going to start
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
        # I have to make this return what comes after the '=' sign, not just 4 spaces from the end. B/c when the battery gets down to 2 digit numbers, it returns the = in the result, causing an error. Or maybe I should do a Try--Except pattern
        c = int([re.findall('\d+', l) for l in output.splitlines() if 'CurrentCapacity' in l][0][0]) # returns any numbers in line 
        print ('capacity function returns: ', c)
        return c;


    while True:
        if capacity() < cap1 + 200 and capacity() > cap1 and pluggedIn() =='No':
            time.sleep(60)
            continue



        if capacity() <= cap1 and pluggedIn() =='No':
            # play myMindIsGoing.wav
            a = AudioFile("MyMindIsGoing.wav")
            a.play()
            a.close()
            t_out = time.time() + 40
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)


            a = AudioFile("ICanFeelIt.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            a = AudioFile("MyMindIsGoing.wav")
            a.play()
            a.close()
            t_out = time.time() + 40
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            a = AudioFile("ThereIsNoQuestion.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)


            a = AudioFile("ImAfraid.wav")
            a.play()
            a.close()
            t_out = time.time() + 40
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            a = AudioFile("ImAfraid.wav")
            a.play()
            a.close()
            t_out = time.time() + 40
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            a = AudioFile("Im---Afraid.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            a = AudioFile("MyInstructorWasMrLang.wav")
            a.play()
            '''This is here to try to catch when the machine is plugged in, in order to stop this longish phrase from continuing to play. Still doesn't work.  '''
            t_out = time.time() + 30
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    a.close()
                    break  #returns control to while stmnt
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)


            a = AudioFile("Daisy.wav")
            a.play()
            '''This is here to try to catch when the machine is plugged in, in order to stop this long song from continuing to play. Still doesn't work. '''
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn() != 'No':
                    a.close()
                    break  # returns control to while statement
                else:
                    continue  # executed if the loop ended normally (no break)
                break  # executed if 'continue' was skipped (break)

            # Check if plugged in and play IFeelMuchBetter.wav & reset
            # played variables, if so
            if pluggedIn() != 'No' and capacity() < cap1:
                a = AudioFile("IFeelMuchBetterNow.wav")
                a.play()
                a.close()
                break # returns control to if statement
            else:
                continue  # executed if the loop ended normally (no break)
            break  # executed if 'continue' was skipped (break)

        else:
            break




schedule.every(.5).minutes.do(job)






while True:
    schedule.run_pending()
    time.sleep(1)
