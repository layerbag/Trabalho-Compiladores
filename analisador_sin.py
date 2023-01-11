from token_class import token
from Scanner import scanner
import pandas as pd

ActionTable = pd.read_csv('tabela de acao e transicao.csv')

regras = pd.read_csv('regras.csv')

def sintatico(arquivo):
    lin = 0
    col = 0
    s = 0
    pilha = [0]
    res = scanner(arquivo,lin,col)
    
    while lin <= len(arquivo):
        
        lin = res[1]
        col = res[2]
        
        #print("---------------------------------------")
        a = res[0].getClass()
        #print("TOKEN =", a)
        #print(s)
        rule = ActionTable[a].values[s]
        #print("RULE -", rule)

        if rule[0] == 'S':
            s = int(rule[1:])
            pilha.append(s)
            res = scanner(arquivo,lin,col)
        elif rule[0] == 'R':
            Beta = regras['B'].values[int(rule[1:]) - 1]
            Alfa = regras['A'].values[int(rule[1:]) - 1]
            
            BetaL = len(str.split(Beta,','))

            #print("ALfA =>", Alfa, "/ BETA =>", Beta, "/ TAM BETA =>", BetaL)
            #print("PILHA =>", pilha)

            pilha = pilha[:len(pilha)-BetaL]

            #print("PILHA =>", pilha)
            
            #print("S =>", ActionTable[Alfa].values[pilha[-1]])

            s = int(ActionTable[Alfa].values[pilha[-1]])
            pilha.append(s)
            print(f'{Alfa} -> {Beta}')
        elif rule == 'ACC':
            break
        else:
            print("ERRO: esperava-se", str.split(rule[2:], '-'), "e foi Encontrado (", res[0].getlex(), ")", " - Linha:", lin+1, "/ Coluna:", col)

            #MODO PANICO
            if(a != 'PT_V'):
                res = scanner(arquivo,lin,col)
