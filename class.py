#!/usr/bin/python

class Human:
    def __init__(self):
        self.name = "Adriano"
        self.head = self.Head()

    def teste(self):
        return 'coisa'

    class Head:
        def talk(self):
            return "teste...."

# herança
class Programer(Human):
    def __init__(self, teste):
        self.name = teste;

objPessoa = Human()
print(objPessoa.name)
print(objPessoa.head.talk())

objProgramer = Programer("Coisa")
print(objPessoa.name)
print(objPessoa.head.talk())
