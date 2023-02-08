import os
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger
from kivy.config import Config

kivy.require("1.9.1")

cwd = os.getcwd()
Config.set('kivy', 'log_dir', cwd + '/logs/')
Config.set('kivy', 'log_level', 'debug')
Config.write()


class Start(BoxLayout):
    def new_game(self):
        Logger.debug("Application: New Game Button pressed \n")
        self.clear_widgets()
        self.add_widget(NewGame()) 


    def load_game(self):
        Logger.debug("Application: Load Game Button pressed \n")


    def options(self):
        Logger.debug("Application: Options Button pressed \n")


class NewGame(BoxLayout):
    pass



class MainApp(App):
    def build(self):
        return Start()


if __name__=="__main__": 
    MainApp().run()
