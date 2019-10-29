## Descrição:

Implementação do modelo clássico de sistema de buscas, o modelo Booleano. Dividido em 3 etapas.

### Etapa 1:

Criação de uma base de documentos (arquivo criador_base_de_arquivos.py), nesse caso, foi feito um script em Python para a criação desses arquivos (a.txt ; b.txt ; c.txt) e cada um desses arquivos contém um conteúdo. 
Nesse mesmo script também foi criado um arquivo consulta.txt que será usado para realização de uma consulta com operadores Booleanos [OR, AND E NOT (|, & e !)].

### Etapa 2:

Ler a base de documentos, colocar tudo em minúsculo, fazer a tokenização do meu arquivo que está sendo lido, ou seja, quando leio um arquivo ele me retorna strings, o que vou fazer é colocá-las em uma lista (vetor) em que cada string lida é um elemento da lista. 
Após a tokenização, é preciso fazer a retirada das stopwords do documento, ou seja, palavras que não vão ser relevantes em uma consulta do usuário.

Lista de stopwords que serão desconsideradas na hora de fazer a indexação:
['de', 'a', 'o', 'que', 'e', 'é', 'do', 'da', 'em', 'um', 'para', 'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']

Após retirar todas as stopwords, eu preciso tirar o radical das palavras que sobraram e aí sim eu começo com a criação do índice invertido, neste trabalho vamos utilizar um dicionário de dicionários em python, ou seja, um dicionário fará referência a outro dicionário.
#### O que ocorre na prática:

{termo_com_apenas_o_radical : {arquivosX_que_contem_o_termo : quantidade_de_vezes_que_o_termo_aparece_no_arquivoX}}

### Etapa 3:

Após ler os arquivos da base, realizar a indexação, agora vamos fazer a leitura da consulta, tirar seus radicais, verificar se a palavra está no índice invertido e depois disso criar um arquivo que mostra quais documentos atendem a consulta solicitada e quais são eles.




Este foi um breve resumo sobre o que os arquivos py estão realizando, no código, cada linha foi comentada com sua função.
