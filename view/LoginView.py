from kivy.lang import Builder
from controller import loginController
import os

# dir = os.getcwd()
# files = os.listdir(dir)
# print(f"dir:  {dir},  arquivos {files}")

KV = Builder.load_file("./view/kv/loginScreen.kv")

login = loginController.login

