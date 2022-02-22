import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from view.LoginView import LoginView



class MainWindow(ScreenManager):
    pass


Builder.load_file('./view/kv/loginScreen.kv')
