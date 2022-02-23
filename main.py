from kivy.app import App
from src.view.MainView import MainWindow

class Main(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    Main().run()
