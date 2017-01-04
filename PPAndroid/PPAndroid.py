import seccure
import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Username:', font_size=50))
        self.username = TextInput(multiline=False, font_size=50, height=25)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password:', font_size=50))
        self.password = TextInput(password=True, multiline=False, font_size=50, height=25)
        self.add_widget(self.password)



class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
