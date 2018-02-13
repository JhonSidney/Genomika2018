import urllib.request
from datetime import date
import re
import zipfile
import os


url = 'http://compbio.charite.de/jenkins/job/hpo.annotations.monthly/lastStableBuild/artifact/annotation/ALL_SOURCES_ALL_FREQUENCIES_diseases_to_genes_to_phenotypes.txt'
date = date.today() #recebendo data de hoje
data = date.strftime('%Y%m%d') #Convertendo data em string

nome_arquivo_zip = 'hpo_'+data+'.zip' #criando string com nome :hpo_data.zip
nome_arquivo_txt = 'hpo_'+data+'.txt' #criando string com nome :hpo_data.txt

urllib.request.urlretrieve(url, nome_arquivo_txt) #realizando o download do arquivo

arquivo = zipfile.ZipFile(nome_arquivo_zip,'w') #Criando um arquivo .zip
arquivo.write(nome_arquivo_txt) #insere no arquivo .zip o arquivo baixado
arquivo.close()
os.remove(nome_arquivo_txt)# remove o arquivo txt após o download
