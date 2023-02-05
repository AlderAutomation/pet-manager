import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import logging 

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log.log", level=logging.DEBUG, format = LOG_FORMAT)
mylog = logging.getLogger()



class Start(Widget):
    def new_game(self):
        self.clear_widgets()
        self.add_widget(NewGame())


    def load_game(self):
        print("continue")


    def options(self):
        print("options")


class NewGame(Widget):
    print("New Game Button Pushed")



class MainApp(App):
    def build(self):
        return Start()


if __name__=="__main__": 
    MainApp().run()
