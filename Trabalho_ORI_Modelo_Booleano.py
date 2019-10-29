# UNIVERSIDADE FEDERAL DE UBERLÂNDIA - UFU
# Organização e Recuperação da informação - Professor Wendel Melo 
# Guilherme Henrique de Araújo Santos - 11721BSI220
# Gustavo Henrique Ferreira Reis Costa - 11721BSI222 
# ***************************************************************** #

# Baixando o Python e o Pip Windows e Linux:
# Baixe o Python 3 no Windows pelo site: https://www.python.org/downloads/
# Instale o Python 3 no Linux pelo comando: sudo apt install python3 
# Instale o pip Linux, para poder instalar o pacote nltk, digite o comando: sudo apt install python3-pip 
# O pip já vem junto com a instalação do Python no Windows

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# Após a instalação do Python e do pip, seguir alguns passos:
# Primeira coisa: Instalar o NLTK no seu computador, abra o CMD do Windows e digite o seguinte comando:
# py -m pip install -U nltk (Isso para Windows)
# python3 -m pip install -U nltk (Isso para Linux, feito pelo terminal)
# Depois de instalar o NLTK digite os seguintes comandos:
# (Abra o Python ou digite no CMD "py" / No Terminal Linux digite "Python3") e dê enter que você estará no terminal python
# Estando no Python digite os seguintes comandos:
# import nltk
# nltk.download() 
# O comando acima abrirá um monte extensões do pacote NLTK para fazer o download, você vai em Collections e baixar o "stopwords" na interface que aparece, como no Windows
# nltk.download('stopwords') -> Digite isso no terminal do Linux, porque ele não terá interface gráfica
# Esses comandos trouxeram as stopwords do NLTK
# No mesmo instalador do NLTK vá em Models e baixe dois pacotes na interface que aparece, como no Windows:
# nltk.download("punkt") -> Digite isso no terminal do Linux, porque ele não terá interface gráfica
# Para possibilitar a tokenização das palavras
# e o pacote:
# nltk.download( "rslp" ) -> Digite isso no terminal do Linux, porque ele não terá interface gráfica
# Para podermos extrair os radicais das palabras
# Após baixar isso, baixe também o pacote:
# nltk.download("mac_morpho") -> Digite isso no terminal do Linux, porque ele não terá interface gráfica
# Em Corpora na interface que aparece, como no Windows

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# Para rodar o documento, no Windows:
# Abra o CMD (Prompt de comando) e vá na pasta na qual encontra o trabalho
# É necessário que tenha 3 documentos para chamar o arquivo pelo prompt:
    # 1: O modelo booleano que está sendo criado aqui
    # 2: O arquivo que contém o nome dos arquivos que são as referências para minha base de dados
    # 3: O arquivo que contém a consulta que irá ser retornada no final 
# Como ficou a chamada dos argumentos:
# C:\Users\guilh\Desktop\ORI\Trabalho>py Trabalho_ORI_Modelo_Booleano.py base.txt consulta.txt
# py - Chamando o Python 3
# Trabalho_ORI_Modelo_Booleano.py - O código-fonte com o modelo booleano
# base.txt - O arquivo que contém as referências para a base de documentos
# consulta.txt - O arquivo que contém a consulta

# Para rodar o documento no Linux:
# Abra o terminal e vá na pasta na qual estão os arquivos, os pré requisitos são os mesmos do Windows
# Como ficou a chamada dos argumentos no Linux, cada argumento possui o mesmo significado do Windows:
# socrates@socrates-Lenovo-ideapad-330-15IKB:~/ORI$ python3 Trabalho_ORI_Modelo_Booleano.py base.txt consulta.txt 

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# REFERÊNCIA, BASE E CONSULTA utilizada, em forma de scripts em Python:
    # arquivobase = open("base.txt","w")
    # base = arquivobase.write("a.txt\nb.txt\nc.txt")
    # arquivobase.close()

    # arquivoconsulta = open("consulta.txt","w")
    # consulta = arquivoconsulta.write("casa & amor | casa & !mora")
    # arquivoconsulta.close()

    # arquivo1 = open("a.txt","w")
    # arq1 = arquivo1.write("Era uma CASA muito \nengracada. Não tinha teto, \nnão tinha nada.")
    # arquivo1.close()

    # arquivo2 = open("b.txt","w")
    # arq2 = arquivo2.write("quem casa quer casa. \nQUEM não mora em \ncasa, também quer casa!")
    # arquivo2.close()

    # arquivo3 = open("c.txt","w")
    # arq3 = arquivo3.write("quer casar comigo, amor? \nquer casar comigo, \nfaça o favor! \nmora na minha casa!")
    # arquivo3.close()

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# CÓDIGO FONTE - MODELO BOOLEANO:

import nltk # Importando o pacote NLTK para poder usar seus recursos na aplicação.
import json # Importado o pacote JSON para converter dicionário em texto
import sys # Importando o pacote SYS para poder ler os argumentos por linha de comando

stopwords = nltk.corpus.stopwords.words # Lista de stopwords
stopwords = nltk.corpus.stopwords.words("portuguese") # Pegando as stopwords em português
stopwords.sort() # Ordenando as stopwords por ordem alfabética 

# Após ordenar as stopwords, executar a leitura do arquivo base (aquele que conterá o nome dos arquivos presentes na base de documentos)

with open(sys.argv[1],"r") as arquivobase: # Abertura do arquivo base.txt pelo argumento passado na linha de comando setado com a opção de leitura
    base = arquivobase.read() # Leitura dos dados do arquivo que mostrará a minha base de documentos disponíveis
    listarq = base.split("\n") # A função split me permite retirar todo o conteúdo especificado dentro do parênteses, no caso estamos tirando todos os enters "\n" e colocamos dentro de uma lista

dict_listarq = {} # Criação de um dicionário vazio que, futuramente, irá armazenar o índice de referência para o documento da minha base da minha base
contador = 1 # Contador para numerar o número dos documentos, funcionará como índice do meu dicionário declarado acima

dicionario_indice = {} # Criação de um dicionário que resultará no índice invertido posteriormente

# Criação de um laço para percorrer a lista que contém as "referências" para minha base de dados
for k in range (0, len(listarq)): 

    if contador not in dict_listarq: # Se contador não existir no dicionário
        dict_listarq[contador] = listarq[k] # Dicionário coloca o contador como sua chave e seu valor inicial é dado como o nome do arquivo no qual ele se encontra
    dict_listarq[contador] = listarq[k] # Se for encontrado também executará essa ação
    contador += 1 # Incremento o contador para armazenar o próximo arquivo posteriormente

    arqY = open(listarq[k], "r") # Criando uma variável de leitura para abrir o arquivo da posição "k"
    readY = arqY.read().lower() # A variável readY irá ler o arquivo da posição k e passar todas as suas letras para minúsculas.
    # A função replace abaixo pegará toda <origem> (Primeiro "caracter ou palavras") e trocar pelo <destino> (Sengundo "caracter ou palavra")
    readY = readY.replace("?","")
    readY = readY.replace(",", "")
    readY = readY.replace(".", "")
    readY = readY.replace("!", "")
    readY = readY.replace("...", "")
    readY = readY.replace("\n", "")

    # Realizar a tokenização do conteúdo readY, ou seja, separar cada caractere ou string por vírgulas dentro de uma lista
    palavras = nltk.word_tokenize(readY) # Palavras contém uma lista tokenizada
    
    palavras_not_stopwords = [] # Criação de uma lista para armazenar os documentos da base sem "stopwords"
    palavras_not_rad = [] # Criação de uma lista para armazenar os documentos da base com apenas os radicais

    # Criação de outro laço para percorrer a lista do conteúdo da base tokenizado
    for k in range(0, len(palavras)):
 
        if(palavras[k] not in stopwords): # Se a palavra ou caracter da posição k na lista palavras não for "stopwords" (variável criada)
            palavras_not_stopwords.append(palavras[k]) # Utilizo a função append para acrescentar a "palavra" dentro da minha lista de palavras sem stopwords

    # Criação de um laço para percorrer a minha lista de palavras do documento sem stopwords
    for k in range(0, len(palavras_not_stopwords)):
        stemmer = nltk.stem.RSLPStemmer() # Criação de uma variável que permite que eu possa tirar os radicais das palavras
        palavras_not_rad.append(stemmer.stem(palavras_not_stopwords[k])) # Colocando as palavras sem as stopwords e com seus radicais extraídos na lista palavras_not_rad
               
    # Este for percorre os índices do dicionário dict_listarq, onde temos que pegar os números de cada documentos, no caso que estão no índice
    for c in dict_listarq.keys():
        valores = c # Colocando uma variável para armazenar o valor dos índices que serão o número referente a cada documento

    # Laço percorrendo a lista com as palavras sem radicais e sem stopwords
    for c in range (0, len(palavras_not_rad)):
        if palavras_not_rad[c] not in dicionario_indice: # Se a palavras não estiver no índice invertido
            dicionario_indice[palavras_not_rad[c]] = 0 # Recebe 0
            dicionario_indice[palavras_not_rad[c]] = {} # Crio um dicionário vazio, que armazenará futuramente {"arquivo" : "quantidade de vezes que a palavra aparece"}
        
        if palavras_not_rad[c] in dicionario_indice: # Se a palavra estiver no índice invertido
            dicionario_indice[palavras_not_rad[c]][valores] = palavras_not_rad.count(palavras_not_rad[c]) # Coloco o arquivo que ela está que é a variável que foi criada logo acima (valores) e conto a quantidade de vezes que a palavra aparece no vetor com os radicais e sem stopwords  

    arqY.close() # Fechando arquivo com conteúdo informativo, ou seja, o arquivo da base que está sendo lido no momento

with open('indice.txt', 'w') as indice: # Cria o arquivo indice.txt para receber o dicionario de indice invertido
    indice.write('\n'.join(': '.join((key, json.dumps(dicionario_indice[key]))) for key in sorted(dicionario_indice, key=str)).replace('": ',',').replace('{','').replace('}','').replace('"','').replace(', ',' ')) # Escreve no arquivo cada chave do dicionário transformado em texto separado em linhas e substituindo caracteres indesejáveis por outros requeridos

with open(sys.argv[2], 'r') as queryreader: # Abre e lê o arquivo consulta.txt pelo argumento passado na linha de comando
    query_codificada = queryreader.read() # Recebe o conteudo do arquivo consulta.txt
query = query_codificada.replace('&','AND').replace('|','OR').replace('!','NOT ') # Armazena o conteúdo de query_codificada substituindo caracteres especiais pelos termos AND/OR/NOT

lista_consulta = query.split(" OR ") # Cirando uma lista que se comportaria como uma sublista da consulta original sem o OR

# Declarando quatro conjuntos vazios que serão usados posteriormente para realizar operações entre conjuntos, os nomes das variáveis, não possuem um significado específico, são apenas nomes:
arquivos_proibidos = set()
arquivos_permitidos = set()
arquivos_finais = set()
arqtemp = set()

# Este laço vai percorrer a lista com as palavras da consulta sem o OR, que foi "splitado" acima
for z in range (0, len(lista_consulta)):
    if 'AND' in lista_consulta[z]: # Se encontrar a palavra " AND " na minha subconsulta, então
        sublista_consulta = lista_consulta[z].split(" AND ") # Vou dividir a consulta em outras sublistas  
        # Este laço irá percorrer as minhas sublistas
        for ww in range (0, len(sublista_consulta)):
            if 'NOT' not in sublista_consulta[ww]: # Se a palavra NOT não estiver na sublista feita, significa que tem-se que
                sublista_consulta[ww] = stemmer.stem(sublista_consulta[ww]) # Retirar o radical da palavra que não possui o NOT
                if sublista_consulta[ww] in dicionario_indice: # Se a palavra consultada se encontra no índice invertido
                    # Crio um laço que irá percorre meu dicionário índice (que é meu índice invertido)
                    for k in dicionario_indice: 
                        if k == sublista_consulta[ww]: # Se a chave for igual a palavra buscada
                            # Crio outro laço que irá acessar a palavra que eu quero, dentro dela, tenho um dicionário que, me fala em qual arquivo ela se encontra e quantas vezes ela aparece, eu vou percorrer esse dicionário da palavra então 
                            for r in dicionario_indice[k].keys(): 
                                arqtemp.add(r) # Adiciona a um conjunto o número dos arquivos que possuem tal palavra a um conjunto que será considerado como temporário
                            if arquivos_permitidos == set(): # Na primeira interação a lista de arquivos de um AND é vazia, então
                                arquivos_permitidos = arqtemp # Vou colocar os valores do meu "conjunto temporário" dentro de um conjunto que será meus arquivos oficiais
                            else: # Caso meu arquivo permitido (nome de variável meramente ilustrativo, pode-se colocar outros nomes) não seja vazio, como:
                                arquivos_permitidos = arquivos_permitidos.intersection(arqtemp) # Nas outras interações, ele recebe a interseção entre os arquivos das palavras anteriores com a palavra atual

                            arqtemp = set() # O conjunto com os arquivos temporários é zerado para a próxima palavra do AND
                            
            else:  # Se encontrar uma palavra que contenha NOT
                sublista_consulta[ww] = sublista_consulta[ww].replace('NOT ', '') # Vamos trocar o NOT por nada, ou seja, vamos retirá-lo
                sublista_consulta[ww] = stemmer.stem(sublista_consulta[ww]) # Após retirar a palavra NOT, vamos tirar o radical do que sobrou
                if sublista_consulta[ww] in dicionario_indice: # Se a palavra que sobrou estiver no índice invertido
                    for o in dicionario_indice: # Vamos percorrer o dicionário do índice invertido
                        if o == sublista_consulta[ww]: # E quando a chave deste dicionário for igual a palavra buscada
                            # Crio um laço que, irá percorrer o valor da chave do índice invertido, que no caso é, um outro dicionário, nesse dicionário referente a essa palavra ele busca entre as chaves que indicam os arquivos onde uma palavra é presente
                            for r2 in dicionario_indice[o].keys(): 
                                arqtemp.add(r2) # Adiciona a um conjunto os arquivos que possuem tal palavra a um conjunto temporário
                            if arquivos_proibidos == set(): # Na primeira interação a lista de arquivos de um AND é vazia porém
                                arquivos_proibidos = arqtemp # Ele recebe os arquivos do conjunto temporário, como na outra interação
                            else:
                                arquivos_proibidos = arqtemp.intersection(arquivos_proibidos) # Nas outras interações ele recebe a intersessão entre os arquivos das palavras anteriores com a palavra atual

                            arqtemp = set() # O conjunto com os arquivos temporários é zerado para a próxima palavra do AND
                           
                arquivos_permitidos = arquivos_permitidos.difference(arquivos_proibidos) # Os arquivos permitidos passam a ser a diferença entre os já permitidos menos os proibidos

    arquivos_finais = arquivos_finais.union(arquivos_permitidos) # Os arquivos finais são a união entre os arquivos finais e os já permitidos após um OR
    # Resetando os conjuntos de arquivos permitidos e proibidos para o próximo elemento da consulta
    arquivos_proibidos = set()
    arquivos_permitidos = set()       

with open('resposta.txt', 'w') as resposta: # Crio um arquivo com o nome resposta.txt 
    resposta.write(str(len(arquivos_finais))+"\n") # Escreve no arquivo resposta.txt a quantidade de arquivos que atendem à consulta
    arquivos_finais = list(arquivos_finais) # Transformando o conjunto de arquivos finais em uma lista
    for n in range(0, len(arquivos_finais)): # Percorrendo a lista de arquivos finais
        if arquivos_finais[n] in dict_listarq: # Se o número do arquivo existente em arquivos finais, for, equivalente a chave do dicionário que contém os arquivos
            for j in dict_listarq: # Percorro o dicionário com o número do documento e o nome dos documentos
                if arquivos_finais[n] == j: # Se a chave do dicionário for igual à algum valor da lista
                    resposta.write(dict_listarq[j] + "\n") # Escreva no arquivo resposta.txt o nome do arquivo