from Scanner import scanner,getTable
from tabela import tabela

if __name__ == '__main__':
    
    arquivo = open("testeArquivo.txt",'r',encoding='utf-8')
    
    arquivo = arquivo.readlines()
    arquivo[-1] = arquivo[-1] + '\n'
    arquivo.append('$')
    lin = 0
    col = 0
    
    while lin <= len(arquivo):
        res = scanner(arquivo,lin,col)
        lin = res[1]
        col = res[2]
        
        if res[0].getClass() != 'ERRO':
            res[0].print()
        
        if res[0].getClass() == 'EOF':
            break
    
    tab = getTable()
    tab.printTab()
            