import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

from src.view.LoginView import LoginWindow

class DashScreen(Screen):
    def on_touch_down(self, touch):
        print('to mexendo aqui')
        return super().on_touch_down(touch)

class MainWindow(ScreenManager):
    pass

LoginWindow()

Builder.load_file('./resources/templates/kv/loginScreen.kv')
