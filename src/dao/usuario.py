import requests



class UsuarioDao():
    def __init__(self) -> None:
        self._url = 'http://192.168.0.36:5000/funcionario'
    
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
            

    def buscar_usuario_por_matricula(self,matricula: int):
        usuarios = self.listar_usuarios()
        for usuario in usuarios:
            if matricula == usuario['matricula']:
                return usuario
            
    
    def logar(self,user, matricula):
        try:
            print('tentando logar')
            usuario = self.buscar_usuario_por_matricula(matricula)
            print(f'{usuario}, recuperado do banco')
            print(f'usuario da tela {user}')
            if  user == usuario['nome_guerra']:
                return True   
        except ValueError:
            print('Não foi possivel fazer o Login')
            return False
            
