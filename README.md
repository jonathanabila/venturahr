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
  - [Matriz_de_Requisitos](#matriz-de-requisitos)
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
O usuário acesso o site e não está logado. Dessa forma, seleciona a opção para realizar o login para acessar a rede social.

### UC-02.01
O usuário acessa o site, porém não possui um perfil, para tal ele seleciona a opção de criar um perfil para visualizar e possivelmente
se candidatar as vagas.

### UC-02.02
O usuário após acessar o site, deve ser capaz de atualizar as suas informações pessoais, tais como meios de contato.

### UC-03
O usuário acessa o site, porém não possui um acesso para publicar as vagas, nesse caso o profissional precisa entrar em contato com o
administrador da conta para providenciar o acesso para ele.

### UC-04.01
Um profissional de RH deseja publicar um nova vaga, para tal, ele acessa o sistema com o seu login e realiza o processo de publicação da
vaga. Após o processo, ele visualiza a vaga publicada.

### UC-04.02
Durante o processo de cadastro de uma vaga ele não adiciona o PMD para um critério, ao tentar salvar a vaga o sistema bloqueia e
mostra um erro na tela explicando que todos os critérios precisam de um PMD.

### UC-04.03
Durante o processo de cadastro de uma vaga ele não adiciona o pesoa para um critério, ao tentar salvar a vaga o sistema bloqueia e
mostra um erro na tela explicando que todos os critérios precisam de um peso.

### UC-04.04
Durante o processo de cadastro de uma vaga o usuário não adiciona nenhum critério, ao tentar salvar a vaga o sistema bloqueia e mostra
um erro na tela explicando que o usuário deve adicionar um número minímo de critérios.

### UC-04.05
Durante o processo de cadastro de uma vaga o usuário não adiciona nenhuma descrição para o critério, com isso o sistema não permite
que a vaga seja salva mostrando que é necessário incluir as descrições para todos os critérios.

### UC-05.01
O candidato deseja se inscrever em um vaga, para isso ele acessa a página da vaga e seleciona a opção para preencher o formulário de
acordo com o seu perfil, após finalizar o preenchimento ele salva e vê que sua candidatura foi concluida.

### UC-05.02
O candidato deseja se inscrever em um vaga, para isso ele acessa a página da vaga e seleciona a opção para preencher o formulário,
porém não concluir a selecão da sua experiência em todos os critérios, e ao tentar salvar sua aplicação visualiza um erro dizendo que é
necessário que ele preencha todos os critérios.

### UC-05.03
O candidato abre a vaga para se inscrever, porém desiste de prosseguir com o processo de candidatura, com isso fecha o site. O sistema não pesiste
o seu progresso, tendo que reiniciar o processo.

### UC-05.03
O candidato abre a vaga para se inscrever, porém desiste de prosseguir com o processo de candidatura, com isso fecha o site e seleciona a opção
para salvar o seu progresso, com isso na próxima vez que abrir a vaga poderá prosseguir com o preenchimento da sua candidatura.

### UC-06.01
O candidato tenta acessar uma vaga por meio da sua url, porém o período para captação de profissionais já encerrou, com isso ele vê uma página
explicando que o processo já foi finalizado.

### UC-06.02
O candidato acessa suas vagas que estão salvas sem finalizar e tentar prosseguir com o cadastro de suas experiências, porém o prazo já se encerrou
e ele é direcionado para uma página explicando que o processo já foi finalizado.

### UC-07.01
Ao final do período que a vaga fica disponível para a captação de profissionais o sistema envia um email para o responsável pela vaga com um link com
o resultado para a captação.

### UC-07.02
Ao final, o usuário responsável pela vaga acessa o seu painel para a vaga e seleciona o opção para extender o tempo que a vaga ficará disponível por
mais um mês.

### UC-07.03
Ao final, o usuário responsável pela vaga acessa o seu painel para a vaga e seleciona o opção finalizar de fato o processo de captação de profissionais.

### UC-07.04
Ao final, o usuário responsável não extende ou fecha a vaga, com isso o sistema fecha a vaga após dois dias como comportamento padrão.

### UC-08.01
O usuário responsável pela vaga deseja acessar o sistema para visualizar mais informações sobre o perfil dos usuários que tiveram uma nota maior ou
iqual ao perfil da vaga.

### UC-08.02
O usuário seleciona o perfil de um usuário com a nota maior que o perfil da vaga e consegue visualizar informações de contato com o profissional.

## Matriz de Requisitos

| ID    | Nome     | Descrição                                                                                                              | Prioridade | Complexidade | Observações                                                                                                                                                                                                                           |
|-------|----------|------------------------------------------------------------------------------------------------------------------------|------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RF-01 | UC-01    | O usuário deve ser capaz de realizar o login na plataforma, sendo uma empresa ou candidato.                            | Essencial  | Médio        | A complexidade do login depende do sistema que estiver sendo utilizado e do framework que irá lidar com todo o processo de autenticação.                                                                                              |
| RF-02 | UC-02.01 | O usuário deve ser capaz de criar a sua conta de candidato de forma autônoma.                                          | Essencial  | Médio        | A complexidade por trás dessa funcionalidade é devido ao processo como um todo, e não a característica do tipo da conta.                                                                                                              |
| RF-03 | UC-02.02 | O usuário deve ser capaz de alterar os dados pessoais.                                                                 | Importante | Fácil        | Após a implementação do perfil do usuário, realizar a atualização dos seus dados cadastrais não é complicado. Porém, não é uma feature essencial para o MVP, dado que o sistema não depende dessa característica para entregar valor. |
| RF-04 | UC-03    | O usuário da empresa deve ser capaz de realizar o login utilizando seus dados de acesso.                               | Essencial  | Médio        | A diferenciação dos perfis não é algo complexo, após implementado o login pode ser realizado por meio de páginas diferentes que passam paramêtros diferentes para especificar o usuário.                                              |
| RF-05 | UC-04.01 | O usuário da empresa deve ser capaz de criar uma nova vaga.                                                            | Essencial  | Médio        | A criação da vaga também não apresenta complexidade, porém é um passo pequeno no processo de construção de todo o sistema.                                                                                                            |
| RF-06 | UC-05.01 | O candidato deve conseguir se inscrever em uma vaga publicada por uma empresa.                                         | Essencial  | Médio        | A complexidade está no fato que devemos criar o relacionamento entre as entidades para persistir o candidato que se inscreveu.                                                                                                        |
| RF-07 | UC-06.01 | O candidato deve ser capaz de acessar uma vaga por meio da url.                                                        | Desejável  | Fácil        | Compor a url com uma chave primária é suficiente para que o usuário possa acessar a vaga por meio da url.                                                                                                                             |
| RF-08 | UC-07.01 | O sistema deve enviar um e-mail para o responsável pela vaga após o período de publicação da vaga.                     | Importante | Fácil        | Um sistema de job/cron é suficiente para iniciar o processo que envia o email.                                                                                                                                                        |
| RF-09 | UC-07.02 | O responsável pela vaga deve ser capaz de extender a publicação da vaga após a 30 dias.                                | Importante | Fácil        | A alteracã́o deve ser realizada na tabela do banco de dados para que a data final seja alterada.                                                                                                                                     |
| RF-10 | UC-07.03 | O responsável deve ser capaz de visualizar um compilado dos usuários que aplicaram a vaga e suas notas.                | Desejável  | Fácil        | Precisamos alimentar uma tabela com uma query simples sobre os usuários que aplicaram para a vaga.                                                                                                                                    |
| RF-11 | UC-08.01 | O responsável pela vaga deve ser capaz de visualizar os dados de contato de um candidato após ele aplicar para a vaga. | Importante | Fácil        | Por meio das chaves primárias devemos disponibilizar as informações do candidato.                                                                                                                                                     |


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

O diagrama de classe abaixo aprenseta o nome das classes, relacionamento e multiplicidade:


<p align="center">
    <img src="./docs/ClassDiagram.jpg" align="center" alt="Digrama de classes" title="Digrama de classes">
</p>
