import requests



class UsuarioDao():
    def __init__(self) -> None:
        self._url = 'http://192.168.0.36:5000/funcionario'
    
    @property
    def url(self):
        return self._url
    
    def listar_usuarios(self):
        req = requests.get(self.url)
        usuarios = req.json()
        return usuarios

    def buscar_usuario_por_matricula(self,matricula: int):
        usuarios = self.listar_usuarios()
        for usuario in usuarios:
            if matricula == usuario['matricula']:
                return usuario
            
