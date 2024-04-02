# Python - Teste com API SWAPI

**Link:** [SWAPI](https://swapi.dev/)

![Badge API](http://img.shields.io/static/v1?label=API&message=SWAPI&color=GREEN&style=for-the-badge)
![Badge Python](http://img.shields.io/static/v1?label=PYTHON&message=V.3&color=blue&style=for-the-badge)
![Badge Docker](http://img.shields.io/static/v1?label=DOCKER&message=Container&color=blue&style=for-the-badge)

![image](https://github.com/gustcoder/python_sw/assets/52874054/ab12af76-766d-4069-8902-7facd845c96e)

# Descrição

A SWAPI é uma API bem simples e interessante que traz diversas informações sobre os filmes, personagens, planetas e demais dados sobre o clássico Star Wars!
E serve muito bem para o aprendizado sobre REST API, requests etc.

Este projeto tem como objetivo apenas fazer algumas requisições para esta API utilizando Python e alguns recursos do Pandas.

# Pré-requisitos

* Docker versão 20 ou superior

<h1> Buildando o container </h1>
Após clonar o projeto, dentro do diretório principal, por favor execute o seguinte comando:

```docker build -t api_starwars .```

<h1> Executando script </h1>
Após ter buildado o container, vamos rodá-lo!

```docker run -it --rm -v "$(pwd)":/app api_starwars python get_dados_api.py```


<h1> Saída Esperada </h1>
O retorno esperado é gerar um arquivo .csv de personagens ordenado pela altura de forma decrescente.

<b>Materiais de apoio</b>:

https://swapi.dev/documentation

https://pandas.pydata.org/docs/user_guide/index.html

https://hub.docker.com/_/python
