from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class FreePosApp(App):
    def build(self):
        self.title = 'Free Positioning'
        box = FloatLayout(size=(200, 150))
        box.add_widget(Button(text='A', size_hint=(0.3, 0.2), pos=(0, 0)))
        box.add_widget(Button(text='B', size_hint=(0.3, 0.2), pos=(50, 80)))
        return box


Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '150')

FreePosApp().run()
