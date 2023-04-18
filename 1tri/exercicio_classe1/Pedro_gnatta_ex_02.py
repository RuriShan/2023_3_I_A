class disc:
    def __init__(self, matricula, nome, prova1, prova2, trabalho1):
        self.matricula = matricula
        self.nome = nome
        self.prova1 = prova1
        self.prova2 = prova2
        self.trabalho1 = trabalho1

    def matricula(self):
        print(f'{self.nome} é do {self.matricula}')

    def nome(self):
        pass

    def prova1(self):
        pass
    
    def prova2(self):
        pass

    def trabalho1(self):
        pass
    
if __name__ == "__main__":
    matematica = disc("3ia", "sua mae", 2 , 2.5 , 1)
    matematica.matricula()