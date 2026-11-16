# Do que se trata:
Este repositório foi criado para um projeto da faculdade durante a matéria de Linguagem de Programação. O trabalho apresenta uma pequena história de um cliente, e com técnicas de Engenharia de Software é feito o Analise de Requisitos, planejamento e por fim a realização. 

# O que é:
Este é um pequeno software de gerenciamento de estoque, e funciona em três camadas

### 1. Visual com Tkinter
O programa utiliza uma interface com a biblioteca do TKinter do Python. Foi a parte mais complicada, já estava habituado com a clareza de HTML, enquanto o TKinter tem uma estrutura totalmente diferente que não me agradou muito. A parte mais legal foi poder trabalhar com as janelas utilizando o conceito de classes, que funciona da seguinte forma:

- O programa principal roda em uma classe APP
- São criadas as Janelas do programa como classes (semelhante a componentes WEB) que executam dentro da APP
- As Janelas então conseguem chamar um método do APP que alterna as Janelas

### 2. POO
A segunda camada envolve lógica orientada a objetos, utilizando Classes e Controller para maneja-los, eles tem End-Points claros que são chamados pela interface do Tkinter. POO já é um tópico do meu conhecimento por conta das APIs feitas anteriormente em minha carreira.

### 3. Arquivo JSON
A terceira camada conversa diretamente com o controller e utiliza da biblioteca OS para manipulação de arquivos. A parte fundamental é a biblioteca JSON, ela faz as conversões dos objetos do programa para JSON e vice e versa, para que assim sejam salvas no computador como um Banco de Dados simulado.
