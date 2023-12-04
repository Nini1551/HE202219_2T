from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GridGameApp(App):
    def build(self):
        self.title = 'Grid Game'
        grid = GridLayout(rows=3, cols=4)
        for i in range(12):
            grid.add_widget(Button(text=str(i + 1)))
        return grid


Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '150')

GridGameApp().run()
