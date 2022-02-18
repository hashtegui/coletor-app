from model.models import Produto
class ProdutoDao():
    lista_produtos = []
    def cadastrar(self,produto):
        self.lista_produtos.append(produto)
        
    def listar(self):
        return self.lista_produtos