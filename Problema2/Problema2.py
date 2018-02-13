import os
import glob
import sys
found = False

pasta1= sys.argv[1] #recebendo primeiro argumento
pasta2 = sys.argv[2] #recebendo segundo argumento

if not os.path.isdir(pasta1) and os.path.isdir(pasta2): #verificando se os diretorios existem
    exit()
else:
    found = True
    list1 = os.listdir(pasta1)  # recebendo lista de arquivos pasta1
    list2 = os.listdir(pasta2)#recebendo lista de arquivos pasta2
    arquivos=[]
    for file in list1:
        for file2 in list2:
            if file == file2:
                arquivos.append(file)

arq_ordenado = sorted(arquivos)
if arq_ordenado == []:
    print('nenhum arquivo igual')
else:
    print(arq_ordenado)




