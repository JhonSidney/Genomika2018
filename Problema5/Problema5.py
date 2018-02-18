import sys
import hashlib
import os
import shutil
import gzip
import _md5
import codecs

def getHash(arquivo):     #------> funcao gera o hash
    nome = ''+arquivo
    hash = hashlib.md5(nome.encode()).hexdigest()
    return hash

parametro1 = sys.argv[1]  # -----> recebendo diretorio de entrada
parametro2 = sys.argv[2]  # -----> recebendo diretorio de saida

if  os.path.exists(parametro1)  and os.path.exists(parametro2) == False:
    # -----> verificando se a pasta de saida existe, caso nao exista sera cria o diretorio.
    parametro_entrada = parametro1 #-----> guardando parametro de entrada
    os.mkdir(parametro2) #----->Criando diretorio
    parametro_saida = parametro2 #----->Guardando diretorio de saida
    list = os.listdir(parametro_entrada)  #----->lista recebendo arquivos do diretorio de entrada
    list2 = os.listdir(parametro_saida) #----->lista recebendo arquivos do segundo diretorio
    list_hash1 = [] #----->lista guarda as hash's antes da transferencia
    list_hash2 = []#-----> lista guarda as hash's depois da transferencia

    tamanho = len(list) #----->recebendo o numero da quantidade de arquivos
    i = 0
    while i < tamanho: #-----> o laço só irá acabar após verificar todos os arquivos
        for indice,file1 in enumerate(list):
            indice = list[i] #----->recebendo indice do arquivo com base no valor 'i'
            index = list.index(indice) #recebendo arquivo na posicao do indice
            hash1 = getHash(list[index]) #passando arquivo e recebendo a hash do arquivo passado antes da transferencia
            list_hash1.append(hash1)#guardando hash recebida na lista de hash's
            nome_arquivo = '%s'%list[index] #-----> recebendo o nome do arquivo
            destino_antigo = os.getcwd()+'/'+parametro_entrada+'/'+nome_arquivo #-----> caminho dos arquivos
            destino_novo = os.getcwd()+'/'+parametro_saida+'/'+nome_arquivo #-----> caminho onde será transferido
            shutil.copy2(destino_antigo, destino_novo) #-----> funcao que move os arquivos
            break

        destino_novo = os.getcwd() + '/' + parametro_saida
        list2 = os.listdir(destino_novo) #-----> atualizando a lista de destino

        for indice,file2 in enumerate(list2):
            indice = list2[i]
            index = list2.index(indice)              #-----> fazendo o mesmo processo do escopo anterior com a lista2
            hash2 = getHash(list2[index])
            list_hash2.append(hash2)
            break

        contador=i #-----> variavel contador recebe a posicao do while
        # -----> verificando se as hash's sao iguais
        if list_hash1[contador] == list_hash2[contador]:
            print('', list2[contador], ' foi transferido com sucesso')
        else:
            print('', list2[contador], ' não foi transferido com sucesso')

        i = i+1 #-----> icrementando o 'i' do laço

else:
    # -----> verificando se a pasta de saida existe, caso nao exista sera cria o diretorio.
    parametro_entrada = parametro1  # -----> guardando parametro de entrada
    parametro_saida = parametro2  # ----->Guardando diretorio de saida
    list = os.listdir(parametro_entrada)  # ----->lista recebendo arquivos do diretorio de entrada
    list2 = os.listdir(parametro_saida)  # ----->lista recebendo arquivos do segundo diretorio
    list_hash1 = []  # ----->lista guarda as hash's antes da transferencia
    list_hash2 = []  # -----> lista guarda as hash's depois da transferencia

    tamanho = len(list)  # ----->recebendo o numero da quantidade de arquivos
    i = 0
    while i < tamanho:  # -----> o laço só irá acabar após verificar todos os arquivos
        for indice, file1 in enumerate(list):
            indice = list[i]  # ----->recebendo indice do arquivo com base no valor 'i'
            index = list.index(indice)  # recebendo arquivo na posicao do indice
            hash1 = getHash(
                list[index])  # passando arquivo e recebendo a hash do arquivo passado antes da transferencia
            list_hash1.append(hash1)  # guardando hash recebida na lista de hash's
            nome_arquivo = '%s' % list[index]  # -----> recebendo o nome do arquivo
            destino_antigo = os.getcwd() + '/' + parametro_entrada + '/' + nome_arquivo  # -----> caminho dos arquivos
            destino_novo = os.getcwd() + '/' + parametro_saida + '/' + nome_arquivo  # -----> caminho onde será transferido
            shutil.move(destino_antigo, destino_novo)  # -----> funcao que move os arquivos
            break

        destino_novo = os.getcwd() + '/' + parametro_saida
        list2 = os.listdir(destino_novo)  # -----> atualizando a lista de destino

        for indice, file2 in enumerate(list2):
            indice = list2[i]
            index = list2.index(indice)  # -----> fazendo o mesmo processo do escopo anterior com a lista2
            hash2 = getHash(list2[index])
            list_hash2.append(hash2)
            break

        contador = i  # -----> variavel contador recebe a posicao do while
        # -----> verificando se as hash's sao iguais
        if list_hash1[contador] == list_hash2[contador]:
            print('', list2[contador], ' foi transferido com sucesso')
        else:
            print('', list2[contador], ' não foi transferido com sucesso')

        i = i + 1  # -----> icrementando o 'i' do laço