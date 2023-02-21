from tabela import tabela
from token_class import token

# str1 -> cabeçalho
# str2 -> variáveis temporárias
# str3 -> corpo do código

str1 = "#include <stdio.h>\ntypedef char literal[256];\nint main(){\n"
str2 = "/*-------Variaveis temporarias---------*/\n"
str3 = ""


token_aux = token(None,None,None)
oprd1 = None
oprd2 = None
ld = token(None,None,None)
expr = token(None,None,None)
cont = 1
flag = True

def semantico(t,a:list,tab: tabela, lin, col, flag1):
    global str1
    global str2
    global str3
    global token_aux
    global oprd1
    global oprd2
    global ld
    global cont
    global flag
    
    if flag1 == False:
        flag = flag1
    
    if t == 6:
        str3 = str3 + ";\n"
    
    if t == 7:
        tab.update(a[0].getlex(),token_aux.tipo)
        str3 = str3 + f",{a[0].getlex()}"
        return a[1:]
        
    if t == 8:
        tab.update(a[0].getlex(),token_aux.tipo)
        str3 = str3 + f"{a[0].getlex()}"
        return a[1:]
    
    if t == 9:
        token_aux.tipo = "inteiro"
        str3 = str3 + "int "
    
    if t == 10:
        token_aux.tipo = "real"
        str3 = str3 + "double "
        
    if t == 11:
        token_aux.tipo = "literal"
        str3 = str3 + "literal "

    if t == 13:
        tk = tab.isInTable(a[0].getlex())
        if tk == False:
            print(f"\nERRO SEMANTICO - VARIAVEL NÃO DECLARADA LINHA {lin + 1} COLUNA {col}\n")
            flag = False
            return a[1:]
        if tk.tipo == 'NULO':
            print(F"\nERRO SEMANTICO - VARIAVEL '{tk.lexema}' NÃO DECLARADA LINHA {lin + 1} COLUNA {col}\n")
            flag = False
        
        elif tk.tipo == 'inteiro':
            str3 = str3 + f'scanf("%d", &{a[0].getlex()});\n'
        elif tk.tipo == 'real':
            str3 = str3 + f'scanf("%lf", &{a[0].getlex()});\n'
        elif tk.tipo == 'literal':
            str3 = str3 + f'scanf("%s", &{a[0].getlex()});\n'
        
        return a[1:]

    if t == 14:
        if token_aux.getClass() != 'ID':
            str3 = str3 + f'printf("{token_aux.getlex()}");\n'
        
        elif token_aux.getTipo() == 'inteiro':
            str3 = str3 + f'printf("%d",{token_aux.getlex()});\n'

        elif token_aux.getTipo() == 'real':
            str3 = str3 + f'printf("%lf",{token_aux.getlex()});\n'
        
        elif token_aux.getTipo() == 'literal':
            str3 = str3 + f'printf("%s",{token_aux.getlex()});\n'
    
        
    if t == 15:
        token_aux.lexema = a[0].getlex().replace('"','')
        token_aux.tipo = a[0].tipo
        token_aux.classe = a[0].classe
        a.pop(0)
    
    
    if t == 16:
        token_aux.lexema = a[0].lexema
        token_aux.tipo = a[0].tipo
        token_aux.classe = a[0].classe
        a.pop(0)
    
        
    if t == 17:
        tk = tab.isInTable(a[0].getlex())
        if tk.tipo == 'NULO':
            print(f"\nERRO SEMANTICO - VARIÁVEL '{tk.lexema}' NÃO DECLARADA LINA {lin} COLUNA {col}\n")
        
        else:
            token_aux = tk

        
        a.pop(0)
    
    
    if t == 19:
        tk = tab.isInTable(a[0].getlex())
        
        if tk == False:
            print(f'\nERRO SEMANTICO - VARIAVEL NÃO DECLARADA LINHA {lin + 1} COLUNA {col}\n')
            flag = False
            a.pop(0)
            return a
        
        elif tk.tipo == ld.tipo:
            
            if tk.tipo == ld.tipo:
                str3 = str3 + f"{tk.lexema} = {ld.lexema};\n"
        
        else:
            print(f"\nERRO SEMANTICO: OPERANDOS {tk.lexema} e {ld.lexema} COM TIPOS INCOMPATIVEIS LINHA {lin + 1} COLUNA {col}\n")
            flag = False
            
        a.pop(0)
    
    
    if t == 20:
        if oprd1.tipo in ['inteiro','real'] and oprd2.tipo in ['inteiro', 'real'] and oprd1.tipo != 'literal':
            # ld token com lexema Tx e tipo do operando 1
            ld = token(None, f'T{cont}', oprd1.tipo)
            
            # linha Tx = oprd1 opa Oprd2
            str3 = str3 + f"T{cont} = {oprd1.getlex()} {a[1].getlex()} {oprd2.getlex()};\n"
            
            # verifica se declara a temporária como int ou double
            if oprd1.tipo == 'inteiro':
                declaraTemp('inteiro')
            else:
                declaraTemp('double')
        
        else:
            print(f"\nERRO SEMANTICO: OPERANDOS '{oprd1.lexema}' e '{oprd2.lexema}' COM TIPOS INCOMPATIVEIS LINHA {lin + 1} COLUNA {col}\n")
            flag = False
        
        oprd1 = None
        oprd2 = None
            
        cont += 1
        a.pop(1)
    
        
    if t == 21:
        ld = oprd1
        oprd1 = None
    
    
    if t == 22:
        # verifica se é uma operação relacional, aritimetica ou outra
        if a[1].classe == 'OPR':
            temp = a[0]
            a.pop(0)
            
        elif a[1].classe == 'OPA':
            temp = a[2]
            a.pop(2)
            
        else:
            temp = a[1]
            a.pop(1)
        
        # pega o token na tabela de simbolos    
        tk = tab.isInTable(temp.getlex())
        if tk == False:
            print(f"\nERRO SEMANTICO - VARIAVEL NÃO DECLARADA LINHA {lin + 1} COLUNA {col}\n")
            flag = False
            return a
        
        if tk.tipo == 'NULO':
            print(f"\nERRO SEMANTICO - VARIAVEL '{tk.lexema}' NÃO DECLARADA LINHA {lin + 1} COLUNA {col}\n")
            flag = False
            return a
        
        else:
            # se o oprd1 estiver vazio, salva no oprd2
            if oprd1 == None:
                oprd1 = tk
                
            else:
                oprd2 = tk

        
    if t == 23:
        if a[1].classe == 'OPR':
            temp = a[0]
            a.pop(0)
            
        elif a[1].classe == 'OPA':
            temp = a[2]
            a.pop(2)
            
        else:  
            temp = a[1]
            a.pop(1)
        
            
        if oprd1 == None:
            oprd1 = temp
        else:
            oprd2 = temp
            
    
      
    if t == 25:
        str3 += "}\n"
    
    
    if t == 26:
        str3 += f"if({expr.lexema})\n{{\n "
    
    
    if t == 27:
        # verifica se a operação é entre int-int, double-double, double-int
        if oprd1.tipo in ['inteiro','real'] and oprd2.tipo in ['inteiro', 'real']:
            #lexema da expr recebe Tx
            expr.lexema = f"T{cont}"
            
            #linha Tx = oprd1 opr oprd2
            str3 += f"T{cont} = {oprd1.getlex()} {a[0].getlex()} {oprd2.getlex()};\n"
            
            if oprd1.tipo == 'inteiro':
                declaraTemp('inteiro')
            else:
                declaraTemp('double')
            
        else:
            print(f"\nERRO SEMANTICO - OPERANDOS COM TIPOS INCOMPATIVEIS LINHA {lin + 1} COLUNA {col}\n")
            flag = False
        
        oprd1 = None
        oprd2 = None
        
        cont += 1
        a.pop(0)
    
    
    # tratamentos finais do código
    if t == 32:
        str3 += f'return 0;\n}}'
        str2 += '/*------------------------------*/\n'
        
    return a

def geraArq():
    if flag:
        arquivo = open("teste.c",'w')
        arquivo.write(str1 + str2 + str3)
    
    
def declaraTemp(tipo):
    global str2
    global cont
    
    if tipo == "inteiro":
        str2 += f"int T{cont};\n"
    if tipo == "double":
        str2 += f"double T{cont};\n"
    if tipo == "literal":
        str2 += f"literal T{cont};\n"