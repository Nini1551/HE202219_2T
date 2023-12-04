import sys

from kivy.app import App
from kivy.config import Config


class Quit2App(App):
    def _quit(self, source):
        print(source)
        sys.exit(0)


Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

Quit2App().run()
