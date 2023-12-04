import sys

from kivy.app import App
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class QuitApp(App):
    def build(self):
        self.title = 'Quit me'
        box = AnchorLayout(anchor_x='center', anchor_y='center')
        quit = Button(text='Quitter', size_hint=(0.7,0.3))
        quit.bind(on_press=self._quit)
        box.add_widget(quit)
        return box

    def _quit(self, source):
        sys.exit(0)


Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

QuitApp().run()