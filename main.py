from kivy.app import App
from view.LoginView import KV

class Main(App):
    def build(self):
        return KV

if __name__ == '__main__':
    Main().run()
