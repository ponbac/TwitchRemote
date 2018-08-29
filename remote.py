from stream import Stream
import keyboard
import psutil
import subprocess

MPV_PROCESS = 'mpv.exe'

current_stream = Stream('twitchpresents')


def new_stream(twitch_name):
    global current_stream
    close_stream()
    current_stream = Stream(twitch_name)


def open_stream():
    global current_stream
    subprocess.Popen(['streamlink -p mpv twitch.tv/' + current_stream.name + ' best'], shell=True)
    current_stream.showing = True
    full_screen()


def close_stream():
    global current_stream

    if current_stream.showing:
        for process in psutil.process_iter():
            # check whether the process name matches
            if process.name() == MPV_PROCESS or process.name() == MPV_PROCESS[:3]:
                process.parent().kill()
                current_stream.showing = False
                print('Stream CLOSED!')
    else:
        print('No stream to close!')


def full_screen():
    keyboard.write(' f', delay=8)
