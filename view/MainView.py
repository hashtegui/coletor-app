import kivy
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder



class MainWindow(ScreenManager):
    pass


Builder.load_file('./view/kv/loginScreen.kv')
