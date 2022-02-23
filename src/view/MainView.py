import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

from src.view.LoginView import LoginWindow



class MainWindow(ScreenManager):
    pass

LoginWindow()

Builder.load_file('./resources/templates/kv/loginScreen.kv')
