[![codecov](https://codecov.io/gh/jonathanabila/venturahr/branch/main/graph/badge.svg?token=R88631ZWER)](https://codecov.io/gh/jonathanabila/venturahr)
![build](https://github.com/jonathanabila/venturahr/actions/workflows/ci.yml/badge.svg)

<p align="center">
    <img src="./docs/logo.jpg" align="center" alt="INFNET logo" title="INFNET" width="200">
</p>

<br>

<div align="center">
    <h3>ESCOLA SUPERIOR DE TECNOLOGIA DA INFORMAÇÃO</h3>
    <h3>GRADUAÇÃO EM ENGENHARIA DE SOFTWARE</h3>
    <br>
    <h3>Instituto INFNET - INFNET</h3>
    <br>
    <h4>TESTE DE PERFORMANCE - TP1</h4>
    <h4>ENGENHARIA DISCIPLINADA DE SOFTWARE</h4>
    <h4>ALUNO: JONATHAN TOLENTINO ABILA</h4>
    <h4>PROFESSOR: ARMÊNIO TORRES</h4>
    <br>
</div>

# Índice
- [Índice](#índice)
- [Introdução](#introdução)
  - [Propósito do documento](#propósito-do-documento)
  - [Escopo do projeto](#escopo-do-projeto)
  - [Definições](#definições)
  - [Referências](#referências)
- [Atores](#atores)
- [Requisitos](#requisitos)
  - [Casos de uso](#casos-de-uso)
- [Diagrama de Classes](#diagrama-de-classes)
  - [Introdução](#introdução)
  - [Objetivo](#diagrama-de-classes-objetivo)
  - [Diagrama](#diagrama)

# Introdução

## Propósito do documento

O objetivo desse relatório é esboçar e desenvolver um MVP para a VenturaSoft focado na recolocação de profissionais de TI,
tal sistema possui o diferencial de focar no perfil mínimo desejado, ao invés de buscar diversas stacks _stacks_ em um único,
exigindo conhecimentos que são muitas vezes impraticáveis.

## Escopo do projeto

O escopo do projeto está ao redor do sistema VenturaHR, brevemente descrito acima, que permitira com que candidatos busquem
vagas de empregos e apliquem o seu perfil para tal, e ao mesmo tempo permitirá as empresas realizar publicações em busca de candidatos
que possuam o PMD (Perfil Mínimo Desejado) para a vaga.

Para descrever o PMD a empresa poderá utilizar um rank indo de 1 (desejável) até 5 (obrigatório), além do peso atribuido para o critério -
a partir do qual será possível calcular o perfil da oportunidade e seus candidatos, sendo que quanto maior o perfil do candidato com a vaga,
maior é a sua compabilitibidade com os requisitos listados.

Um mapa mental com os requisitos descritos em alto nível do projeto pode ser visualizado nessa imagem:

<p align="center">
    <img src="./docs/mind_map_requirements.jpeg" align="center" alt="mapa mental dos requisitos" title="Mapa mental dos requisitos" height="1000px">
</p>

Também há o documento [Documento de Visão ](./docs/vision_venturasoft.pdf) que possui uma visão mais detalhada sobre a solução
desejado de uma maneira geral do ponto de vista de negócios.


## Definições

- Requisitos funcionais: Descrevem quais as funcionalidades devem estar presentes no sistema da perspectiva do usuário.
- Requisitos não funcionais: Descrevem características qualitativas do sistema, isto é, recursos do qual o sistema precisa
ter para cumprir os seus objetivos.
- Casos de Uso: Descrevem o comportamento do sistema do ponto de vista do usuário, fornecendo uma descrição funcional do sistema.
- Atores: Descrevem agentes que interagem com o sistema, representando uma regra, não um usuário individual do sistema.

## Referências
- [Disciplined Agile Delivery: A Practitioner’s Guide to Agile Software Delivery in the Enterprise by](https://www.oreilly.com/library/view/disciplined-agile-delivery/9780132810098/)

# Requisitos

## Casos de uso

### UC-01

# Atores

A lista de atores para o sistema descrito acima, assim como os seus papéis, brevemente descritos, são:

- Tempo: Agente responsável por realizar acionamento do sistema para funções que são programadas.
- Sistema de agregamento: Responsável por realizar o agregamento e elaboração do relatório ao final do período de publicação
da vaga, além de disponibilizar um relatório sobre o andamento dos processos.
- Sistema de autenticação: Responsável por realizar a autenticação e autorização dos usuários na plataforma.


- Candidato: Profissional de TI que está buscando uma vaga.
- Profissional de RH: Responsável por realizar a publicação da vaga e manutenção das vagas.
- Gerente: Responsável por criar e delegar acessos a plataforma de publicação de vagas, além das
ações disponíveis para o profissional de RH.

# Diagrama de classes

### Introdução
UML, “Unified Modeling Language” ou Linguagem de Modelagem Unificada, é uma linguagem que busca padronizar a modelagem
e estruturação de projetos de softwares. O objetivo mais simples da UML é representar sistemas de formas padronizadas,
reduzindo possíveis erros e interpretações incorretas de documentações ou até mesmo o código.

Diferente de “frameworks” ou metodologias que buscam te apresentar uma receita de bolo de como e quando realizar
determinadas tarefas, a UML busca lhe auxiliar provendo ferramentas para visualizar e entender a comunicação entre os
seus objetos.

Um estudo conduzido por Sebastian Baltes com 394 pessoas envolvidas na indústria de softwares e com uma média de 10 anos
de experiência, mostrou que majoritariamente o uso de interfaces analógicas para a criação de diagramas, desses 58%
analógicos somente 38% era arquivado e sobrevivia por alguns dias, já no meio digital 94% do conteúdo era arquivo e
sobrevivia por meses.

Entres os diagramas, 47% mostraram que ajudavam a entender o código que foi criado por outras pessoas. Os principais
objetivos dos diagramas eram: realizar o design do software, explicar e entender o que foi feito – mostrando que a
utilização do diagrama e o correto arquivamento das evidências geradas ajuda o time seja relembrando conceitos,
explicando para novos desenvolvedores ou para pessoas envolvidas com as regras de negócio.

<h3 id="diagrama-de-classes-objetivo">Objetivo</h2>

Com base nos requisitos acima, casos de uso e diagrama de classes esboçaremos um  sistema para a empresa VenturaSoft
focado na recolocação de profssionais de TI.

O diagrama de classes abaixo é uma representação do sistema, não contendo os possíveis metódos e atributos nesse momento,
de tal forma que o foco é o nome das classes, relacionamentos e multiplicidade.


### Diagrama

[//]: # (<p align="center">)
[//]: # (    <img src="./docs/ClassDiagram.jpg" align="center" alt="Digrama de classes" title="Digrama de classes">)
[//]: # (</p>)
