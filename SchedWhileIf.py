#!/usr/bin/env python
# coding=UTF-8

''' Somehow you have to make this script run everytime the machine boots up, either with crontab or .plist files '''
''' Schedule docs: https://schedule.readthedocs.io/en/stable/api.html'''

import schedule, time, math, subprocess

# This AudioFile class lets us play wav files.
import pyaudio
import wave
import sys


def job():
    print 'Started \'job\''
    cap1 = 6420
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
        c = int(round(int([l[-4:] for l in output.splitlines() if 'CurrentCapacity' in l][0]), -1))
        print ('capacity function returns: ', c)
        return c;


    while True:
        if capacity() < cap1 and pluggedIn() =='No':
            # play myMindIsGoing.wav
            a = AudioFile("MyMindIsGoing.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement


            a = AudioFile("ICanFeelIt2.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement

            a = AudioFile("MyMindIsGoing.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement

            a = AudioFile("ThereIsNoQuestion.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break # returns control to while statement

            a = AudioFile("ImAfraid1.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement

            a = AudioFile("ImAfraid1.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    break  # returns control to while statement

            a = AudioFile("Im---Afraid.wav")
            a.play()
            a.close()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    a.close()
                    break  # returns control to while statement

            a = AudioFile("MyInstructorWasMrLang.wav")
            a.play()
                time.sleep(1)
            a.close()
            break

            a = AudioFile("MyInstructorWasMrLang.wav")
            a.play()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    a.close()
                    break  # returns control to while statement
            a.close()


            a = AudioFile("Daisy.wav")
            a.play()
            t_out = time.time() + 60
            while time.time() < t_out:
                time.sleep(1)
                if pluggedIn()!= 'No':
                    a.close()
                    break  # returns control to while statement
                a.close()

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

# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)




while True:
    schedule.run_pending()
    time.sleep(1)
