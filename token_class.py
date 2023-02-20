# classe token
class token:
    def __init__(self,classe,lexema,tipo) -> None:
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def getlex(self):
        return self.lexema
    
    def getClass(self):
        return self.classe
    
    def getTipo(self):
        return self.tipo
    
    def setlex(self, lexema):
        self.lexema = lexema
    
    def print(self):
        print(f'Classe: {self.classe}, Lexema: {self.lexema}, Tipo: {self.tipo}')