from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AgeCalculatorForm(BoxLayout):
    birthyear_input = ObjectProperty()
    age_label = ObjectProperty()

    def _compute(self, source):
        age = 2016 - int(self.birthyear_input.text)
        self.age_label.text = 'Vous avez {} ans.'.format(age)


class AgeCalculatorApp(App):
    pass


Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '75')

AgeCalculatorApp().run()
