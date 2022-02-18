from kivy.app import App
from kivy.lang import Builder

KV = Builder.load_file('./view/principal.kv')

class Main(App):
    def build(self):
        return KV

if __name__ == '__main__':
    Main().run()
