# Genomika2018

Jhon Sidney

Antes de executarmos os codigos, iremos verificar a versão do python e caso necessário iremos fazer
a instalação do python3 no ubuntu.Desde já informo, que os códigos serão executado no ambiente lin-
ux/ubuntu.

1 - VERIFICANDO A VERSÃO PYTHON NO UBUNTU:

    Para verificar se o python3 está instalado em seu ubuntu, Por favor siga as instruções abaixo:
    I  - Abra o terminal do ubuntu (ou as teclas Ctrl+Alt+T).
    II - Digite o comando : python3 --version
        1. Exemplo de mensagem esperada pelo terminal: " python 3.6.3 "
        2. Caso não esteja instalado, siga os passos abaixo.
        3. Para sair do 'root@...' escreva o comando: exit
        4. Para sair do terminal escreva o comando: exit

2 - INSTAÇÃO DO PYTHON3:

    Caso você não tenha a versão do python3, então iremos fazer a instalacão no ubuntu.
    Por favor siga as instruções abaixo:

    I   - Abra o terminal do ubuntu (ou as teclas Ctrl+Alt+T).
    II  - Digite o comando : sudo su
    III - Logo após insira sua senha
    IV  - Insira o comando : apt-get install python3
    V   - Depois é somente ir seguindo as instruções do próprio terminal
    VI  - Após a instação,para sair do 'root@...' escreva o comando: exit
    VII - Para sair do terminal escreva o comando: exit



RESOLUÇÃO DAS QUESTÕES:

    I - PROBLEMA 1:

        Respondido em arquivo chamado  resposta.txt

    II - PROBLEMA 2:

        Para executar a ferramenta que retorna a lista de arquivos, que são iguais entre dois diretorios,
         por favor siga as instruções abaixo:

        1- Acesse o url https://github.com/JhonSidney/Genomika2018, caso esteja no link siga ao passo II.
        2- Faça o download do projeto "Genomika2018-master.zip".
        3- Logo após acesse o diretório: /home/user/Downloads pelo ubuntu.
        4- Faça a extração da pasta 'Genomika2018-master' para a pasta /home/user/Downloads.
        5- Após a extração da pasta, faça a abertura do terminal do seu Ubuntu(ou as teclas Ctrl+Alt+T).
        6- Após abrir o terminal, para visualizar as pastas digite do comando: "ls"
        7- Para acessar as pasta você digita os comando "cd" e logo após o nome do diretório. ":$ cd Downloads/
        8- Digite: cd Genomika2018-master/
        9- Digite: ls
        10-Digite: cd Problema2
        11-Posição esperada do terminal :~/Downloads/Genomika2018-master/Problema2:$
        12-Após acessar o diretório /Problema 2, execute o Problema2.py
        13-Para executar digite: python3 Problema2.py ./pasta1 ./pasta2
        14-Resultado esperado: ['lista.txt', 'modulo.py']



     III - PROBLEMA 3:

           Para executar o problema3.py, onde será baixado dados de uma fonte de dados online,
           que está no formato TXT de forma tabulada e será compactada em um arquivo .zip como
           no exemplo: hpo_20180101.
           com base no tutorial anterior do problema 2, iremos seguir apartir do passo 4.

        4- Faça a extração da pasta 'Genomika2018-master' para a pasta /home/user/Downloads.
        5- Após a extração da pasta, faça a abertura do terminal do seu Ubuntu(ou as teclas Ctrl+Alt+T).
        6- Após abrir o terminal, para visualizar as pastas digite do comando: "ls"
        7- Para acessar as pasta você digita os comando "cd" e logo após o nome do diretório. ":$ cd Downloads/
        8- Digite: cd Genomika2018-master/
        9- Digite: ls
        10-Digite: cd Problema3
        11-Posição esperada do terminal :~/Downloads/Genomika2018-master/Problema3$
        12-Digite o comando: ls (mensagem esperada: Problema.py)
        13-Para executar digite: python3 Problema3.py

        Aguarde o download do arquivo completo e logo após o download ele criará o arquivo.zip
        na pasta do problema3.



    V - PROBLEMA 5:

        Para executar o script python, onde fará a cópia dos arquivos do diretório de entrada
        para o diretório de saída, onde fará um check de integridade no diretório de saída


        1-Abra o terminal e acesse o diretório especificado abaixo no passo 2:
        2-Posição esperada do terminal :/Downloads/Genomika2018-master/Problema5
        3-Digite o comando: ls (mensagem esperada: Problema.py)
        4-Para executar digite: python3 Problema5.py ./desafio5  ./desafio6
        5-resultado esperado será a copia dos arquivos na pasta ./desafio6 e
          imprimir se foi feito com sucesso ou não a cópia.


