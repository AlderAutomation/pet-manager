import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import logging 

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
mylog = logging.getLogger()

kivy.require("1.9.1")
win_bg_color = 1,1,1,1


class Start(BoxLayout):
    def new_game(self):
        self.clear_widgets()
        self.add_widget(NewGame()) 


    def load_game(self):
        print("continue")


    def options(self):
        print("options")


class NewGame(BoxLayout):
    print("New Game Button Pushed")



class MainApp(App):
    def build(self):
        return Start()


if __name__=="__main__": 
    MainApp().run()
