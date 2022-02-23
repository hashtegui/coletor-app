import requests
import pandas as pd


class UsuarioDao():
    def __init__(self) -> None:
        self._url = 'http://192.168.0.36:5000/funcionario'
        self._sql = ''''''

    @property
    def url(self):
        return self._url

    def listar_usuarios(self):
        try:
            req = requests.get(self.url)
            usuarios = req.json()
            return usuarios
        except ValueError:
            print('Erro ao fazer a requisição')

    def buscar_usuario_por_matricula(self, matricula: int):
        usuarios = self.listar_usuarios()
        for usuario in usuarios:
            if matricula == usuario['matricula']:
                return usuario

    def buscar_usuario(self, usuario: str):
        usuarios = self.listar_usuarios()
        for user in usuarios:
            if user['usuariobd'] == usuario:
                return user

    def decrypt(user):
        pass

    def logar(self, user, senha):
        
        try:
            print('tentando logar')
            #usuario = self.buscar_usuario_por_matricula(matricula)
            usuario = self.buscar_usuario(user)
            print(f'{usuario}, recuperado do banco')
            print(f'usuario da tela {user}')
            if user == usuario['nome_guerra']:
                return True
        except ValueError:
            print('Não foi possivel fazer o Login')
            return False
