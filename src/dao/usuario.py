import requests
from src.model.models import Usuario

class UsuarioDao():
    #user= Usuario()
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
            return False

    def buscar_usuario_por_matricula(self, matricula: int):
        usuarios = self.listar_usuarios()
        print(usuarios)
        
        if usuario:
            for usuario in usuarios:
                if matricula == usuario['matricula']:
                    return usuario
        else:
            print('Erro na requisição')
            return None

    def buscar_usuario(self, usuario: str):
        usuarios = self.listar_usuarios()
        for user in usuarios:
            if user['usuariobd'] == usuario:
                return user

    def decrypt(user):
        pass

    def logar(self, user, senha):
        
        try:
            # usuario = self.retorna_usuarios()
            # print(usuario)
            
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
    
    def retorna_usuarios(self) -> list:
        print('retorna usuarios 1')
        usuarios = self.listar_usuarios()
        print('imprimindo usuarios ', usuarios)
        lista_usuarios = []
        user = Usuario()
        for usuario in usuarios:
            print( 'a ser atribuido', usuario)
            user.user = usuario['nome_guerra']
            user.matricula = usuario['matricula']
            user.nome_guera=['nome']
            user.senha = usuario['senhabd']
            lista_usuarios.append(user.__dict__)
            
        return lista_usuarios