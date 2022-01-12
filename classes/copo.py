from classes.recipiente import Recipiente
# Desenvolva sua classe Copo aqui.


class Copo(Recipiente):
    def __init__ (self, tamanho:float, conteudo:int = 0, limpo:bool = True):
        super().__init__(tamanho,conteudo, limpo)
        

    def __repr__(self) -> str:
        if self.conteudo <=0:
            return f"Um copo vazio de {self.tamanho}ml"
        return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

        
    def __str__(self) -> str:
            if self.conteudo <=0:
                return f"Um copo vazio de {self.tamanho}ml"
            return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"




    def encher(self,bebida:str='água'):
        if self.limpo == False:
            
            return "Não se pode encher um copo sujo"

        else:
            self.limpo = False
            self.conteudo = self.tamanho
            self.bebida = bebida


    def beber(self, quantidade:float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"

        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        
        else:
            self.conteudo = self.conteudo - quantidade


    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True