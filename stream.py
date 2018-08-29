#import requests
#from bs4 import BeautifulSoup
#from twitch import TwitchClient
import os
import psutil
import keyboard


class Stream:
    # client = TwitchClient(client_id='', oauth_token='')

    def __init__(self, streamer_name):
        #self.page = requests.get('http://www.twitch.tv/' + streamer_name)
        #self.soup = BeautifulSoup(self.page.content, "html.parser")

        #self.channel = Stream.client.channels.get_by_id(streamer_name)

        self.name = streamer_name
        self.url = 'twitch.tv/' + streamer_name
        self.title = 'title'
        self.viewers = '1337'
        self.showing = False

    def get_viewers(self):
        return self.viewers

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url
