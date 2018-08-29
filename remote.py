from stream import Stream
import keyboard
import psutil
import subprocess
import time

MPV_PROCESS = 'mpv.exe'

s1 = Stream('twitchpresents')
s2 = Stream('tfblade')


def open_stream(stream):
    sbproc = subprocess.Popen(['streamlink -p mpv twitch.tv/' + stream.name + ' best'], shell=True)
    stream.showing = True


def close_stream(stream):
    for process in psutil.process_iter():
        # check whether the process name matches
        if process.name() == MPV_PROCESS:
            process.kill()
            stream.showing = False


def full_screen():
    keyboard.write(' f', delay=8)


open_stream(s2)
full_screen()
time.sleep(15)
close_stream(s2)
