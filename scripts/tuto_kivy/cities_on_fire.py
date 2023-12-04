from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class SignallingApp(App):
    def build(self):
        self.title = 'Feu de signalisation'

        # Sélection de la ville du feu
        city = BoxLayout(orientation='horizontal')
        city.add_widget(Label(text='Feu'))
        cities = ('Bruxelles', 'Gent', 'Namur')
        city.add_widget(Spinner(values=cities))

        # Activation ou non du feu
        activation = BoxLayout(orientation='horizontal')
        activation.add_widget(CheckBox())
        activation.add_widget(Label(text='Activer le feu'))

        # Choix de l'état du feu (rouge, orange ou vert)
        state = BoxLayout(orientation='horizontal')
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Rouge'))
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Orange'))
        state.add_widget(CheckBox(group='state'))
        state.add_widget(Label(text='Vert'))

        # Composant principal
        box = BoxLayout(orientation='vertical')
        box.add_widget(city)
        box.add_widget(activation)
        box.add_widget(state)
        return box


SignallingApp().run()
