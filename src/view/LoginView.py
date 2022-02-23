from kivy.lang import Builder
from src.controller import loginController


#KV = Builder.load_file("./view/kv/loginScreen.kv")

class LoginView():
    login = loginController.login



