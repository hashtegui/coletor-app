

class Produto():
    def __init__(self, **kwargs) -> None:
        self.codbar: int = kwargs.get('codbar')
        self.codprod: int = kwargs.get('codprod')

    def __str__(self):

        return f'{self.codbar}, {self.codprod}'


class Usuario():
    def __init__(self, **kwargs) -> None:
        self.user: str = kwargs.get('user')
        self.senha: str = kwargs.get('senha')
        self.nome_guera: str = kwargs.get('nome_guerra')
        self.matricula: int = kwargs.get('matricula')
