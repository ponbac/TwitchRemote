from stream import Stream
import keyboard
import psutil
import subprocess

MPV_PROCESS = 'mpv.exe'

current_stream = Stream('twitchpresents')


def new_stream(twitch_name):
    global current_stream
    close_stream(current_stream)
    current_stream = Stream(twitch_name)


def open_stream():
    global current_stream
    subprocess.Popen(['streamlink -p mpv twitch.tv/' + current_stream.name + ' best'], shell=True)
    current_stream.showing = True


def close_stream():
    global current_stream
    for process in psutil.process_iter():
        # check whether the process name matches
        if process.name() == MPV_PROCESS:
            process.kill()
            current_stream.showing = False


def full_screen():
    keyboard.write(' f', delay=8)
