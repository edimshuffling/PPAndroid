import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from plyer import notification, sms

sUsername = 'Abc'
sPassword = '123'

def switch(Light):
        if Light:
            return False
        if Light == False:
            return True

class Connected(Screen):
    recipient = '1234567890'

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def open(self, recipient):
        sms.send(recipient=recipient, message='Open door.')
        notification.notify(title='Door open', message='You have sent a command to open the door.', app_name='', app_icon='', timeout=5)
        print("Door open")

    def lOn(self, recipient):
        sms.send(recipient=recipient, message='Turn on light.')
        notification.notify(title='Light on', message='You have sent a command to turn on the light.', app_name='', app_icon='', timeout=5)
        print("Light on")

    def lOff(self,recipient):
        sms.send(recipient=recipient, message='Turn off light.')
        notification.notify(title='Light off', message='You have sent a command to turn off the light.', app_name='', app_icon='', timeout=5)
        print("Light off")

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()
        app.username = loginText
        app.password = passwordText
        if loginText == sUsername and passwordText == sPassword:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'
            app.config.read(app.get_application_config())
            app.config.write()
        elif loginText != sUsername or passwordText != sPassword:
            print("Wrong username or password")
            color = (1, 0, 0, 1)
            self.ids['login'].background_color = color
            self.ids['password'].background_color = color

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
        color = (1, 1, 1, 1)
        self.ids['login'].background_color = color
        self.ids['password'].background_color = color

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory))

if __name__ == '__main__':
    LoginApp().run()