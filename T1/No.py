class No:
    pai = None
    esquerdo = None
    direito = None
    cor = 0 #0 significa rubro e 1 negro
    def __init__(self, n, c, *args):
        self.nome = n 
        self.cor = c
    def __str__(self):
        return self.nome
