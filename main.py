from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from pathlib import Path
import json
import glob
import random

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "signup_screen"

    def login(self, username, password):
        with open("users.json", 'r') as file:
            users = json.load(file)
        if username in users.keys() and users[username]['password'] == password:
            self.manager.transition.direction = 'right'
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username and password combination!"


class SignUpScreen(Screen):
    def add_user(self, username, password):
        with open("users.json") as file:
            users = json.load(file)

        users[username] = {'username': username, 'password': password,
        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def redirect_login_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction: "right"
        self.manager.current = "login_screen"
    def get_quote(self, feeling):
        feeling = feeling.lower()
        available_feeling = glob.glob("quotes/*txt")
        # Path command extract the name of the file
        available_feeling = [Path(filename).stem for filename in available_feeling]
        
        if feeling in available_feeling:
            with open(f"quotes/{feeling}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling!"
            
        

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    # build is a method of app
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
