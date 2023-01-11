from Scanner import scanner,getTable
from tabela import tabela
import analisador_sin

if __name__ == '__main__':
    
    arquivo = open("testeArquivo.txt",'r')
    
    arquivo = arquivo.readlines()
    arquivo[-1] = arquivo[-1] + '\n'
    arquivo.append('$')
    
    analisador_sin.sintatico(arquivo)