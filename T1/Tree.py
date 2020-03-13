from No import No

class Tree:
    raiz = None
    nil = No('nil',1)
    def __init__(self,r):
        self.raiz = r
    def rotacao_esq(self,x):
        y = x.direito
        x.direito = y.esquerdo
        if y.esquerdo != self.nil:
            y.esquerdo.pai = x
        y.pai = x.pai
        if x.pai == self.nil:
            self.raiz = y
        elif x == x.pai.esquerdo:
            x.pai.esquerdo = y
        else:
            x.pai.direito = y
        y.esquerdo = x
        x.pai = y
