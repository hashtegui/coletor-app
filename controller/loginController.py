from dao.usuario import UsuarioDao

ud = UsuarioDao()

def login(user, matricula):
    usuario = ud.buscar_usuario_por_matricula(matricula)
    print(usuario)
    
    if  user == usuario['nome_guerra']:
        return True
    else:
        return False    
    

    # if user == 'gui' and matricula == '123':
    #     return True
    # else:
    #     return False
