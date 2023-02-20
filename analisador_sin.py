from token_class import token
from Scanner import scanner,tab
import analisador_sem
import pandas as pd

#tabela de ações e transições como dataframe
ActionTable = pd.read_csv('tabela de acao e transicao1.csv')

#tabela de regras da linguagem em dataframe, do tipo
# A | B
#___|____
# L | id
# onde A é a coluna dos não terminais e B a coluna das regras

regras = pd.read_csv('regras.csv')

def sintatico(arquivo):
    # linha, coluna, estado
    lin = 0
    col = 0
    s = 0
    pilha = [0]
    pilha_s = []
    res = scanner(arquivo,lin,col)

    while lin+1 < len(arquivo):
        
        pilha_s.append(res[0])    
        a = res[0].getClass()
        
        rule = ActionTable[a].values[s]

        # caso comece com "S" é Shift
        if rule[0] == 'S':
            
            s = int(rule[1:])
            pilha.append(s)
            
            lin = res[1]
            col = res[2]
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
            
            pilha_s = analisador_sem.semantico(int(rule[1:]),pilha_s,tab)
            
            
        # caso seja aceitação
        elif rule == 'ACC':
            break
        
        # caso seja erro
        else:
            # esp = tokens esperados
            esp = str.split(rule[2:],sep='-')
            print("<<< ERRO SINTÁTICO >>>")
            print("<< ERRO: esperava-se", esp, '-', "e foi Encontrado (", res[0].getlex(), ")", "- Linha:", lin+1, "/ Coluna:", col, ">>")     
            
            flag = PhraseLevel(esp,lin,col,a)
            
            if flag == -1:
                lin = res[1]
                col = res[2]
                res = Panico(arquivo,lin,col,esp)
            else:
                res = flag
    
    analisador_sem.geraArq()

# FUNÇÃO PANICO
def Panico(arquivo,lin,col,esp):

    res = scanner(arquivo,lin,col)
    lin = res[1]
    col = res[2]
    
    a = res[0].getClass()
  
    # procura um token esperado
    while (a != 'PT_V' and a !='EOF'):  
        
        if a in esp:
            return res
        else:
            res = scanner(arquivo,lin,col)
            lin = res[1]
            col = res[2]
            a = res[0].getClass()
    
    return res


# RECUPERAÇÃO LOCAL        
def PhraseLevel(esp,lin,col,a):
    
    if 'PT_V' in esp:
        tk = token('PT_V',';','NULO')
        return [tk,lin,col]
    
    elif 'VIR' in esp:
        tk = token('PT_V',',','NULO')
        return [tk,lin,col]
    
    elif 'inicio' in esp:
        tk = token('inicio','inicio','inicio')
        return [tk,lin,col]
    
    elif 'fim' in esp and a == 'EOF':
        tk = token("fim","fim","fim")
        return [tk,lin,col]
    
    return -1
