from kivy.app import App
#from view.LoginView import KV
from view.MainView import MainWindow

class Main(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    Main().run()
