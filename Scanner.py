from token_class import token
from tabela import tabela

tab = tabela()

def getTable():
    return tab

def erro(lin,col,palavra,state,linE,colE):
    lexema = "".join(palavra)
    
    tk = token('ERRO',lexema,'NULO')
    tk.print()

    if state == 2:
        print(f'ERRO, "{lexema}" espera-se um digito após o ".", linha: {lin + 1}, coluna: {col}')
    elif state == 4:
        print(f'ERRO, "{lexema}" espera-se um digito após o "E ou e", linha: {lin + 1}, coluna: {col}')
    elif state == 5:
        print(f'ERRO, "{lexema}" espera-se um digito após o "+ ou -", linha: {lin + 1}, coluna: {col}')
    elif state == 9:
        print(f'ERRO, "{lexema}" espera-se um fecha aspas na linha: {linE + 1}, coluna: {colE}')
    else:
        print(f'ERRO, "{lexema}" inválido na linguagem, linha: {lin + 1}, coluna: {col}')
    
    return [tk,lin,col]


def aceita(lin,col,state,palavra):
    
    lexema = "".join(palavra)
    tipo = 'NULO'
    
    if state == 1 or state == 3 or state == 6:
        classe = "NUM"
        if "." in palavra or "-" in palavra:
            tipo = "real"
        else:
            tipo = "inteiro"
            
    if state == 7:
        classe = "ID"
        tipo = "NULO"

        tk = tab.isInTable(lexema)
        if tk != False:
            return [tk,lin,col]
        
        tab.appendTable(token(classe,lexema,'NULO'))
        
    if state == 8:
        classe = "EOF"
    if state == 10:
        classe = "LIT"
        tipo = "literal"
    if state == 12 or state == 13 or state == 14 or state == 15 or state == 16 or state == 17:
        classe = "OPR"
    if state == 18:
        classe = "ATR"
    if state == 19:
        classe = "OPA"
    if state == 20:
        classe = "AB_P"
    if state == 21:
        classe = "FC_P"
    if state == 22:
        classe = "PT_V"    
    if state == 23:
        classe = "VIR"
    
    
    return [token(classe,lexema,tipo),lin,col]


def scanner(file,lin,col):
    
    palavra = []
    state = 0
    letras = list("ABCDEFGHIJKLMNOPKRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    digitos = list("0123456789")
    linE = -1
    colE = -1
    outros = list(",;:.!?\*+-/(){}[]<>='\"") 

    c = file[lin][col]

    while True:
        
        # estado 0
        if state == 0:
            linE = lin
            colE = col

            if c in digitos:
                state = 1
                palavra.append(c)

            elif c in letras:
                state = 7
                palavra.append(c)

            elif c == '$' and file[lin] == file[-1]:
                palavra.append('EOF')
                return aceita(lin,col,8,palavra)
            
            elif c == '"':
                state = 9
                palavra.append(c)
            
            elif c == '{':
                state = 11
            
            elif c == '<':
                state = 12
                palavra.append(c)
            
            elif c == '=':
                state = 13
                palavra.append(c)
            
            elif c == '>':
                state = 14
                palavra.append(c)
                
            elif c in ['+','-','*','/']:
                state = 19
                palavra.append(c)
            
            elif c == '(':
                state = 20
                palavra.append(c)
            
            elif c == ')':
                state = 21
                palavra.append(c)
            
            elif c == ';':
                state = 22
                palavra.append(c)
            
            elif c == ',':
                state = 23
                palavra.append(c)
            
            elif c == '\n':
                state = 0
                lin = lin + 1
                col = -1
            
            elif c == ' ' or c == '\t':
                state = 0
                
            else:
                state = 0
                palavra.append(c)
                col = col + 1
                return erro(lin,col,palavra,state,linE,colE)
        
        # ESTADO 1
        elif state == 1:
            if c in digitos:
                palavra.append(c)
                
            elif c == '.':
                state = 2
                palavra.append(c)
                
            elif c == 'E' or c == 'e':
                state = 4
                palavra.append(c)
                
            else:
                return aceita(lin,col,state,palavra)
            
        # ESTADO 2
        elif state == 2:
            if c in digitos:
                state = 3
                palavra.append(c)
                
            else:
                return erro(lin,col,palavra,state,linE,colE)
        
        # ESTADO 3
        elif state == 3:
            if c in digitos:
                palavra.append(c)
                
            elif c == 'E' or c == 'e':
                state = 4
                palavra.append(c)
                
            else:
                return aceita(lin,col,state,palavra)
        
        # ESTADO 4
        elif state == 4:
            if c in digitos:
                state = 6
                palavra.append(c)
            elif c == '+' or c == '-':
                state = 5
                palavra.append(c)
            else:
                return erro(lin,col,palavra,state,linE,colE) 
        
        # ESTADO 5
        elif state == 5:        
            if c in digitos:
                state = 6
                palavra.append(c)
            else:
                return erro(lin,col,palavra,state,linE,colE)
            
        # ESTADO 6
        elif state == 6:       
            if c in digitos:
                palavra.append(c)
            else:
                return aceita(lin,col,state,palavra)
                
        # ESTADO 7
        elif state == 7:  
            if c in letras or c in digitos or c == '_':
                palavra.append(c)
            else:
                return aceita(lin,col,state,palavra)
        
        
        # ESTADO 9
        elif state == 9:
            if c == '"':
                state = 10
                palavra.append(c)
            elif c != '\n':
                palavra.append(c)
            else:
                return erro(lin,col,palavra,state,linE,colE) 
            
        # ESTADO 10
        elif state == 10:
            return aceita(lin,col,state,palavra)
        
        # ESTADO 11
        elif state == 11:
            if c == '}' :
                state = 0
            elif c == '$' and file[lin] == file[-1]:
                print(f"Comentário da linha {linE + 1} coluna {colE} não fechado")
                palavra.append('EOF')
                return aceita(lin,col,8,palavra)
            elif c == '\n':
                lin = lin + 1
                col = -1
                
                
        
        # ESTADO 12
        elif state == 12:
            if c == '=':
                state = 13
                palavra.append(c)
            elif c == '>':
                state = 14
                palavra.append(c)
            elif c == '-':
                state = 18
                palavra.append(c)
            else:
                return aceita(lin,col,state,palavra)
        
        # ESTADO 13
        elif state == 13:
            return aceita(lin,col,state,palavra)
        
        # ESTADO 14
        elif state == 14:
            if c == '=':
                state = 17
                palavra.append(c)
            else:
                return aceita(lin,col,state,palavra)
        
        # ESTADO 17
        elif state == 17: 
            return aceita(lin,col,state,palavra)
        
        # ESTADO 18
        elif state == 18:
            return aceita(lin,col,state,palavra)

        # ESTADO 19 a 23
        elif state in [19,20,21,22,23]:
            return aceita(lin,col,state,palavra)
        
        
        col = col + 1
        c = file[lin][col]
            
