from flask import Flask, render_template, make_response
import remote
import socket

'''---FLASK PART---'''
app = Flask(__name__)  # create Flask-object


# Index
@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    return resp


# Open the inputted twitch stream
@app.route('/open/<twitch_id>')
def open_stream(twitch_id):
    remote.new_stream(twitch_id)
    remote.open_stream()
    print('Trying to open ' + twitch_id + ' stream!')
    return "cray shit " + str(twitch_id)


# Exit, close all streams f
@app.route('/close/')
def close_stream ():
    remote.close_stream()
    return 'stopping all cray shit'


# main
if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()))
