from kivy.app import App
from view.MainView import MainWindow
from view.LoginView import LoginView

class Main(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    Main().run()
