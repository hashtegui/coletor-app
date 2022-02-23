from src.dao.usuario import UsuarioDao

ud = UsuarioDao()

def login(user, matricula):
    try:
        usuario = ud.buscar_usuario_por_matricula(matricula)
        if  user == usuario['nome_guerra']:
            return True   
    except ValueError:
        print('Não foi possivel fazer o Login')
        return False