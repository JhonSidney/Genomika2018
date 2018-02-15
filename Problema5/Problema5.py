import sys
import hashlib
import os
import shutil
import zipfile
import gzip


def getHash(arquivo):



def descompactar(caminho):
    caminho = ''+caminho
    zipado = zipfile.ZipFile(caminho)
    zipado.extract()




parametro1 = sys.argv[1]
parametro2   = sys.argv[2]

if  os.path.exists(parametro1)  and os.path.exists(parametro2) == False:
    parametro_entrada = parametro1
    parametro_saida = os.mkdir(parametro2)

    list = os.listdir(parametro_entrada)
    list2 = os.listdir(parametro_saida)
    list_hash1 = []
    list_hash2 = []
    i = 0

    while i < len(list):
        file = i
        for file in list:
            descompactar(parametro_entrada)
            hash1 = getHash(list[i])
            print(hash1)
            list_hash1.append(hash1)
            shutil.move(list[file], parametro_saida)

        for file in list2:
            hash2 = getHash(list[i])
            print(hash2)
            list_hash2.append(hash2)

        if list_hash1[i] == list_hash2[i]:
            print('{%s}', list[i], ' foi transferido com sucesso')
        else:
            print('{%s}', list[i], ' não foi transferido com sucesso')





else:
    print('passou pelo else!!!')
    parametro_entrada = parametro1
    parametro_saida = parametro2



    list = os.listdir(parametro_entrada)
    list2 = os.listdir(parametro_saida)
    list_hash1=[]
    list_hash2=[]
    i = 0

    while i < len(list):
        file = i
        for file in list:
            hash1 = getHash(file)
            print(hash1)
            list_hash1.append(hash1)
            shutil.move(file,parametro_saida)

        for file in list2:
            hash2 = getHash(file)
            print(hash2)
            list_hash2.append(hash2)


        if list_hash1[i] == list_hash2[i]:
            print('{%s}',list[i],' foi transferido com sucesso')
        else:
            print('{%s}',list[i],' não foi transferido com sucesso')
























