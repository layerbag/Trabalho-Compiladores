from token_class import token
from Scanner import scanner
import pandas as pd

#tabela de ações e transições como dataframe
ActionTable = pd.read_csv('tabela de acao e transicao.csv')

#tabela de regras da linguagem em dataframe, do tipo
# A | B
#___|____
# L | id
# onde A é a coluna dos não terminais e B a coluna das regras

regras = pd.read_csv('regras.csv')

def sintatico(arquivo):
    # linha, coluna, estado
    lin, col, s = 0
    pilha = [0]
    res = scanner(arquivo,lin,col)
    
    while lin <= len(arquivo):
        
        lin = res[1]
        col = res[2]
        
        a = res[0].getClass()
        
        rule = ActionTable[a].values[s]

        # caso comece com "S" é Shift
        if rule[0] == 'S':
            
            s = int(rule[1:])
            pilha.append(s)
            
            res = scanner(arquivo,lin,col)

        # caso seja Reduce Alfa -> Beta
        elif rule[0] == 'R':
            
            Beta = regras['B'].values[int(rule[1:]) - 1]
            Alfa = regras['A'].values[int(rule[1:]) - 1]
            
            BetaL = len(str.split(Beta,','))

            pilha = pilha[:len(pilha)-BetaL]

            s = int(ActionTable[Alfa].values[pilha[-1]])
            pilha.append(s)
            
            print(f'{Alfa} -> {Beta}')
            
        # caso seja aceitação
        elif rule == 'ACC':
            break
        
        # caso seja erro
        else:
            print("ERRO: esperava-se", str.split(rule[2:], '-'), "e foi Encontrado (", res[0].getlex(), ")", " - Linha:", lin+1, "/ Coluna:", col)

            #MODO PANICO
            if(a != 'PT_V'):
                res = scanner(arquivo,lin,col)