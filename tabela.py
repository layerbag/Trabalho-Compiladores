from token_class import token

class tabela:
    def __init__(self) -> None:
        self.tabela = []
        
        self.tabela.append(token("inicio","inicio","inicio"))
        self.tabela.append(token("varinicio","varinicio","varinicio"))
        self.tabela.append(token("varfim","varfim","varfim"))
        self.tabela.append(token("escreva","escreva","escreva"))
        self.tabela.append(token("leia","leia","leia"))
        self.tabela.append(token("se","se","se"))
        self.tabela.append(token("entao","entao","entao"))
        self.tabela.append(token("fimse","fimse","fimse"))
        self.tabela.append(token("fim","fim","fim"))
        self.tabela.append(token("inteiro","inteiro","inteiro"))
        self.tabela.append(token("literal","literal","literal"))
        self.tabela.append(token("real","real","real"))
    
    def getTable(self):
        return self.tabela

    def appendTable(self,tk: token):
        self.tabela.append(tk)
    
    def isInTable(self,lexema):
        
        for tk in self.tabela:
            if tk.getlex() == lexema:
                return tk
        
        return False
    
    def printTab(self):
        print('\n\n-------------TABELA ---------------------------------------   ')
        for x in self.tabela:
            x.print()
        print('-------------------------------------------------------')
        
    def update(self, lexema, tipo):
        
        for i,tk in enumerate(self.tabela):
            if tk.getlex() == lexema:
                tk_aux = token(tk.getClass(),lexema,tipo)
                self.tabela.pop(i)
                self.tabela.insert(i,tk_aux)
                break