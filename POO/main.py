class DadosImportantes:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"
    
class InformacoesExtras(DadosImportantes):
    def __init__(self, endereco, dataNascimento):
         self.endereco = endereco
         self.dataNascimento = dataNascimento
    def exibir2(self):
        return f"Endereço: {self.endereco}"
    
pessoa1 = InformacoesExtras(1,2)
pessoa1.exibir()