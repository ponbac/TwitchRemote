import requests
from bs4 import BeautifulSoup
from twitch import TwitchClient
import os


class Stream:
    #client = TwitchClient(client_id='', oauth_token='')

    def __init__(self, streamer_name):
        #self.page = requests.get('http://www.twitch.tv/' + streamer_name)
        #self.soup = BeautifulSoup(self.page.content, "html.parser")

        #self.channel = Stream.client.channels.get_by_id(streamer_name)

        self.name = streamer_name
        self.url = 'twitch.tv/' + streamer_name
        self.title = 'title'
        self.viewers = '1337'

    def open(self):
        os.system('streamlink -p mpv twitch.tv/' + self.name + ' best')

    def get_viewers(self):
        return self.viewers

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url
