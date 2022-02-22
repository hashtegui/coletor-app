from dao.usuario import UsuarioDao

ud = UsuarioDao()

def login(user, matricula):
    usuario = ud.buscar_usuario_por_matricula(matricula)
    if  user == usuario['nome_guerra']:
        return True
    else:
        return False    
    