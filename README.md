# Sistema de Gerenciamento de Concessionária
Este é um projeto desenvolvido em Python que simula um sistema de gerenciamento de carros de uma concessionária.

A ideia do projeto é permitir o cadastro e organização de veículos dentro de uma pequena aplicação feita em terminal. Os dados dos carros são armazenados em um arquivo JSON, funcionando como um banco de dados simples.

Esse projeto foi desenvolvido como prática de programação em Python, organização de código em módulos e uso de Git e GitHub para versionamento.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de carros
- Listagem de carros cadastrados
- Busca de carros por marca ou modelo
- Remoção de carros do sistema
- Atualização dos dados de um carro
- Ordenação de carros por marca
- Ordenação de carros por preço
- Estatísticas sobre os veículos cadastrados
- Relatório geral da concessionária

## Tecnologias utilizadas

Este projeto foi desenvolvido utilizando:

- Python
- JSON para armazenamento de dados
- Git para controle de versão
- GitHub para hospedagem do repositório

## Estrutura do projeto

O projeto está organizado nos seguintes arquivos:

- main.py  
Arquivo principal responsável por executar o sistema e apresentar o menu ao usuário.

- carros.py  
Contém as funções responsáveis pelo gerenciamento dos carros, como cadastro, busca, remoção, atualização, ordenação e geração de relatórios.

- database.py  
Responsável por salvar e carregar os dados dos carros no arquivo JSON.

- utils.py  
Arquivo com funções auxiliares utilizadas para melhorar a organização e a exibição das informações no terminal.

- carros.json  
Arquivo que funciona como um banco de dados simples onde os carros cadastrados são armazenados.

## Como executar o projeto

1. Clone o repositório:

git clone https://github.com/seuusuario/seurepositorio.git

2. Acesse a pasta do projeto:

cd SistemaDeConcessionaria-Python

3. Execute o programa:

python main.py

