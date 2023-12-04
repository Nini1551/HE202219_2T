from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


class LoginApp(App):
    def build(self):
        self.title = 'Se connecter'
        box = BoxLayout(orientation='horizontal')
        box.add_widget(Label(text='Pin code'))
        box.add_widget(TextInput(multiline=False))
        box.add_widget(Button(text='Entrer'))
        return box


# Config.set('graphics', 'resizable', '0')
Window.size = (350, 50)

LoginApp().run()