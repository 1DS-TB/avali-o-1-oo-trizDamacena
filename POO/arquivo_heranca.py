class Dados:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

        
    def dados(self):
        print("======Dados da matrícula======")
        print(f"Nome: {self.nome}\nIdade: {self.idade} anos \nAltura: {self.altura}")

class DadosExtras(Dados):
    def __init__(self, nome, idade, altura, nomepai, nomemae):
        super().__init__(nome,idade,altura)
        self.nomepai = nomepai
        self.nomemae = nomemae

    def resumo(self):
        print("\n======Dados completos da matrícula======")
        print(f"Nome {self.nome}\nIdade: {self.idade} anos\nAltura: {self.altura}\nNome da mãe: {self.nomemae}\nNome do pai: {self.nomepai}")


pessoa1 = DadosExtras("Beatriz", 18, 160, "Bernardete", "Eracilio")

pessoa1.dados()
pessoa1.resumo()
