#===== classe =======#
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

#===== Método =======#
    def mostrarAluno(self):
        print(f"Nome do aluno: {self.nome}\nCurso: {self.curso}\n")

#===== Instânciação de classe e criação de objeto =======#
aluno1 = Aluno("Thiago","Sistemas de informação")
print("Classe I")
aluno1.mostrarAluno()


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def mostrarLivro(self):
        print(f"Titulo: {self.titulo}znAutor: {self.autor}\n")

livro1 = Livro("The witcher","Andrzej Sapkowski")
print("Classe II")
livro1.mostrarLivro()

class Celular:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
    
    def mostrarCelular(self):
        print(f"Modelo: {self.modelo}\nFabricante: {self.fabricante}\n")

celular1 = Celular("A54", "Samsung")
print("Classe III")
celular1.mostrarCelular()

class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def mostrarCachorro(self):
        print(f"Nome:{self.nome}\nRaça: {self.raca}\n")

cao = Cachorro("Chase","Spitz alemão")
print("Classe IV")
cao.mostrarCachorro()

class Computador:
    def __init__(self, processador, memoria):
        self.processador = processador
        self.memoria = memoria
    
    def mostrarPC(self):
        print(f"Processador: {self.processador}\nMemória: {self.memoria}\n")

pc = Computador("Ryzen 5", "16GB RAM")
print("Classe V")
pc.mostrarPC()

class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def mostrarFuncionario(self):
        print(f"Nome: {self.nome}\nCargo: {self.cargo}\n")
    
f = Funcionario("Thiago", "Desenvovledor Backend")
print("classe VI")
f.mostrarFuncionario()

class Bicicleta:
    def __init__(self, tipo, aro):
        self.tipo = tipo
        self.aro = aro

    def MostrarBicicleta(self):
        print(f"Tipo: {self.tipo}\nAro: {self.aro}\n")

bike = Bicicleta("Trilha", "32")
print("classe VII")
bike.MostrarBicicleta()

class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    
    def mostrarFilme(self):
        print(f"Título: {self.titulo}\nDiretor: {self.diretor}\n")

filme = Filme("Liga da Justiça","Zack Snyder")
print("classe VIII")
filme.mostrarFilme()

class Restaurante:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def mostrarRestaurante(self):
        print(f"Nome: {self.nome}\nTipo de culinária: {self.tipo}\n")

rest = Restaurante("Pai D'égua","Paraense")
print("classe IX")
rest.mostrarRestaurante()

class Aviao:
    def __init__(self, companhia, modelo):
        self.companhia = companhia
        self.modelo = modelo
    
    def mostrarAviao(self):
        print(f"Companhia aérea: {self.companhia}\nModelo: {self.modelo}\n")

aviao = Aviao("Lockhead Martin","F-35C")
print("classse X")
aviao.mostrarAviao()