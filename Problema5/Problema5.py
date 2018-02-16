import sys
import hashlib
import os
import shutil
import gzip
import _md5
import codecs




def getHash(arquivo):

    nome = ''+arquivo
    hash = hashlib.md5(nome.encode()).hexdigest()
    return hash



parametro1 = sys.argv[1]
parametro2   = sys.argv[2]

if  os.path.exists(parametro1)  and os.path.exists(parametro2) == False: #caso tenha a pasta
    parametro_entrada = parametro1
    os.mkdir(parametro2)
    parametro_saida = parametro2

    list = os.listdir(parametro_entrada)
    list2 = os.listdir(parametro_saida)
    list_hash1 = []
    list_hash2 = []
    i = 0

    while i < len(list):
        file = i
        for file in list:
            hash1 = getHash(list[i])
            print(hash1)
            list_hash1.append(hash1)
            nome_arquivo = '%s'%list[i]
            print (nome_arquivo)
            print (parametro_saida)
            shutil.move(nome_arquivo, parametro_saida)

        for file in list2:
            hash2 = getHash(list2[i])
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

