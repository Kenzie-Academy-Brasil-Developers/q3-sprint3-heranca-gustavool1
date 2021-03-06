# Desenvolva sua classe Recipiente aqui.
class Recipiente:

    def __init__ (self, tamanho:float,  conteudo: int = 0, limpo:bool = True) -> None:

        self.tamanho = float(0 if tamanho <= 0 else tamanho )
        self.conteudo = float(conteudo)
        self.limpo = limpo 

    def __str__(self) -> str:
        state = "limpo" if self.limpo else "sujo"
        return f"Um recipiente {state} não especificado"


    def __repr__(self) -> str:
        state = "limpo" if self.limpo else "sujo"
        return f"Um recipiente {state} não especificado"


    def esvaziar (self):
        self.conteudo = 0
    

    def esta_vazio (self):
        if self.conteudo <= 0:
            return True
        return False


    def lavar (self):
        self.esvaziar()
        self.limpo = True


    def esta_limpo (self):
        if self.limpo == True:
            return True
        return False


    def estado (self):
        if self.limpo == True:
            return "limpo"
        return "sujo"



    def sujar (self):
        self.limpo = False

