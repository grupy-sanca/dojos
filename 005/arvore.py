"""
Árvore Binária de Busca
-----------------------


>>> arvore = Arvore()
>>> arvore.insere(10)
>>> arvore.raiz
10
>>> arvore.raiz.esquerda is None
True
>>> arvore.raiz.direita is None
True
>>> arvore.insere(5)
>>> arvore.raiz.esquerda
5
>>> arvore.raiz.insere(No(15))
>>> arvore.raiz.direita
15
>>> arvore.insere(20)
>>> arvore.insere(14)
>>> arvore.raiz.direita.direita
20
>>> arvore.raiz.direita.esquerda
14
>>> arvore.insere(50)
>>> arvore.raiz.direita.direita.direita
50
>>> arvore.buscar(10)
True
>>> arvore.buscar(15)
True
>>> arvore.buscar(13)
False
>>> arvore.buscar(50)
True
>>> arvore.buscar(100)
False
>>> arvore.buscar(20)
True
>>> arvore.buscar(5)
True
>>> arvore.buscar(8)
False
>>> arvore.buscar(14)
True
>>> arvore.pre_ordem()
10
5
15
14
20
50
>>> arvore.em_ordem()
5
10
14
15
20
50
>>> arvore.pos_ordem()
5
14
50
20
15
10
"""


class No:
    esquerda = None
    direita = None

    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return str(self.valor)

    def insere(self, no):
        if no.valor > self.valor:
            if self.direita:
                self.direita.insere(no)
            else:
                self.direita = no
        else:
            if self.esquerda:
                self.esquerda.insere(no)
            else:
                self.esquerda = no

    def pre_ordem(self):
        print(self.valor)
        if self.esquerda:
            self.esquerda.pre_ordem()
        if self.direita:
            self.direita.pre_ordem()

    def em_ordem(self):
        if self.esquerda:
            self.esquerda.em_ordem()
        print(self.valor)
        if self.direita:
            self.direita.em_ordem()

    def pos_ordem(self):
        if self.esquerda:
            self.esquerda.pos_ordem()
        if self.direita:
            self.direita.pos_ordem()
        print(self.valor)


class Arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, elem):
        no = No(elem)
        if self.raiz:
            self.raiz.insere(no)
        else:
            self.raiz = no

    def pre_ordem(self):
        if self.raiz:
            self.raiz.pre_ordem()

    def em_ordem(self):
        if self.raiz:
            self.raiz.em_ordem()

    def pos_ordem(self):
        if self.raiz:
            self.raiz.pos_ordem()

    def buscar(self, valor, inicio=None):
        if inicio is None:
            inicio = self.raiz

        if valor == inicio.valor:
            return True

        if valor < inicio.valor:
            if inicio.esquerda:
                return self.buscar(valor, inicio.esquerda)
            else:
                return False
        else:
            if inicio.direita:
                return self.buscar(valor, inicio.direita)
            else:
                return False
