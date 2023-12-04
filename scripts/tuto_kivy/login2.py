from kivy.app import App
from kivy.config import Config

class Login2App(App):
    pass


Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '50')

Login2App().run()
