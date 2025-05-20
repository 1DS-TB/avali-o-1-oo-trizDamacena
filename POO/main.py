class Pokemon:
    def __init__ (self, nome, altura, peso ,geracao):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.geracao = geracao

    def info (self):
        return f"Nome: {self.nome}, Geração {self.geracao}"

    def mostrar_informacoes(Pokemon):
        def status(self):
            return f"{self.nome} está dormindo"

pokemo1 = Pokemon("Squirtle", 0.5, 0.9, "Primeira" )
print(pokemo1.info())
print(pokemo1.status)