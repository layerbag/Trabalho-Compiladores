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
    
    def print(self):
        print(f'Classe: {self.classe}, Lexema: {self.lexema}, Tipo: {self.tipo}')