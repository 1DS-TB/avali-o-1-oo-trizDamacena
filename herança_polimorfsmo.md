# Pesquisa de Herança e Polimorfimos
Pesquisa feita com o intuito de aprendizagem sobre herança e polimorfismo, conceitos de POO (Programação Orientada a Objeto).

## Herança 
Quando criamos uma class, definimos dentro da função '__init__' as variavéis que desejamos guardar em nossa memória, assim podemos manipular da forma que precisarmos, e posteriormento criar nossas propriedades, que auxiliam durante o código. Quando temos um grande projeto, onde a maioria dele está separado em classe, é provavél que em algum momento iremos precisar reutilizar algumas dessas propridades já ciradas. Para facilitar essa reutilização usamos o método de herança.
Como o próprio nome sugere, herança é quando herdamos algo posterior à nós. Na programção, usamos herança para herdar propriedades de outras partes que são independentes, servindo como uma base para a que está sendo criada. Para exemplificar melhor, vamos imaginar que criamos a nossa primeira classe no nosso código, na qual vai receber todos as informações que irão ser colocadas pelo usuário, podemos chamar ela de classe Pai já que é a originária de tudo. Suponhamos que mais para frente no mesmo projeto precisamos usar algumas informações daquela classe criada anteriormente, e ao invés de criar uma nova classe e definir todas as informações novamente, criamos uma classe filha que irá receber como parâmetro a classe pai e herdar todas as prorpriedades que existem dentro dela. Um pequeno resumo: 

1. Classe Base (Classe Pai): Classe que concede propriedades para outra classe herdar;
2. Classe Derivada (Classe Filha): Classe que herda as propriedades da classe Pai;

Para exemplo de um código em que herança é usada, deesenvolvi o seguinte código:

### Código:

Vamos imaginar que estamos desenvolvendo um sistema de cadastro, no qual foi informado que existem dois tipos: Um cadastro simples, o que recebe mais informações, e um mais com mais informações. Pensando no primeiro tipo, criamos uma classe que irá receber os dados básico de todos os clientes como: Nome, Idade e Alrura:

class Dados:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

        
    def dados(self):
        print("======Dados da matrícula======")
        print(f"Nome: {self.nome}\nIdade: {self.idade} anos \nAltura: {self.altura}")

### Explicando:
1. Começamos criando a classe Dados;
2. Criamos uma função, dentro da classe, na qual inicia as nossas variáveis(nome,idade, altura);
3. Depois disso, criamos uma nova função apenas para mostrar os dados quando socilitado; 

---

Agora, pensando em cadastros mais requerem mais informações, criamos uma segunda classe que irá receber a Classe Pai (Dados) como base:

class DadosExtras(Dados):
    def __init__(self, nome, idade, altura, nomepai, nomemae):
        super().__init__(nome,idade,altura)
        self.nomepai = nomepai
        self.nomemae = nomemae

    def resumo(self):
        print("\n======Dados completos da matrícula======")
        print(f"Nome {self.nome}\nIdade: {self.idade} anos\nAltura: {self.altura}\nNome da mãe: {self.nomemae}\nNome do pai: {self.nomepai}")

### Explicando:
1. Criamos a classe DadosExtras e colocamos a classe Dados como parâmetro, informando que esta classe que está sendo criada é uma classe filha que irá herdar as propriedades da classe pai;
2. Novamente criamos a função para iniciarmos as variáveis;
    1. Para utilizamos as variáveis criadas na classe anterior precisamos chamá-las utilizando super()._init_
    2. Agora criamos as variáveis locais da nossa classe filha;
3. Por fim, criamos uma outra função para exibir, só que desta ve os dados mais complexos;

Por completo temos o código desta maneira, acrestado com as linhas para inserir os dados e exibi-los: 

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

Repare que mesmo criando o objeto e informando que ele é da classe Dados extras é possível acessar a função que está em Dados (Classe Pai), já que a DadosExtras (Classe Filha) herdou todas as propriedade da anterior. 

### Resumo:
Como vimos no exemplo, a utilização de herança torna o código mais limpo e linear. No exemplo mostrado, poderiamos ter feito um If Else perguntando se o cadastro iria conter mais informações além de Nome, Idade e Altura, e que seria preciso escrever praticamente a mesma coisa nas duas condições. Usando Orientação a objeto e herança conseguimos tornar o código menor, de mais fácil para manutenção, de melhor entendimento e limpo.
Lembrando que quando estamos utilizando POO é de extrema importância o clean code, nomeando classe e propriedade de forma clara, para facilitar a manutenção do código.
