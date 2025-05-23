class Personagem:
    def __init__(self, nome, altura, peso):
        self.nome = nome 
        self.altura = altura
        self.peso = peso 
    
    def informacoes(self):
        print(f"Nome: {self.nome}.")
        print(f"Altura: {float (self.altura)} metros.")
        print(f"Peso: {float (self.peso)} kg.")

    def atacar(self):
        print("\nAtacar")
        print("Começa uma disputa entre treinadores e seus pokemons.")

    def defender(self):
        print("\nDefender:")
        print("Tentar derrotar o inimigo e se proteger.")

class Treinador(Personagem):
    def pegar_pokebola(self):
        print("\nPegar Pokebola")
        print("Pegar pokebolapara usar o pokemon desejado para a baltalha.")
    def defender(self):
        print("\nEscolher melhor pokemon para a batalha.")
        print("Tentar derrotar o inimigo e se proteger.")

class Pokemon(Personagem):
    def defender(self):
        fora_da_pokebola = True 
        if fora_da_pokebola:
            print("\nObedecer comandos do treinador.")
        else: 
            print("\nEsperar o treinador escolher")
        print("Tentar derrotar o inimigo e se proteger")

pikachu = Pokemon("pikachu", 6, 7)

pikachu.informacoes()
pikachu.defender()