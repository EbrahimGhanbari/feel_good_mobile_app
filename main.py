from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"

class SignUpScreen(Screen):
    def add_user(self, username, password):
        print(username, password)

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    # build is a method of app
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
