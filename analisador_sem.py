import os
from tabela import tabela
from token_class import token

str1 = "#include <stdio.h>\nint main(){\n"
str2 = ""
str3 = ""

token_aux = token(None,None,None)
def semantico(t,a,tab):
    global str1
    global str2
    global str3
    global token_aux
    
    if t == 5:
        str3 = str3 + "\n\n\n"
    
    if t == 6:
        a[0].tipo = token_aux.tipo
        str3 = str3 + ";\n"
    
    if t == 7:
        
        tab.update(a[2].getlex(),token_aux.tipo)
        str3 = str3 + f",{a[2].getlex()}"
        
    if t == 8:
        tab.update(a[2].getlex(),token_aux.tipo)
        str3 = str3 + f"{a[2].getlex()}"
        return a[:1]
    
    if t == 9:
        token_aux.tipo = "int"
        str3 = str3 + "int "
        return a[:1]
    
    if t == 10:
        token_aux.tipo = "float"
        str3 = str3 + "float "
        return a[:1]
        
    if t == 11:
        token_aux.tipo = "string"
        str3 = str3 + "string "
        return a[:1]

    return a
def geraArq():
    arquivo = open("teste.c",'w')
    arquivo.write(str1 + str2 + str3 + '\nreturn 0;\n}')