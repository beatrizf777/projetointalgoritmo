# Nome do Jogo

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Beatriz Carvalho
- Nome do integrante 2

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

O Real or AI? é um jogo digital educativo de investigação que simula situações de identificação de conteúdos produzidos por inteligência artificial ou por seres humanos.

O jogador assume o papel de um investigador digital e recebe diferentes textos e conteúdos para analisar, devendo identificar sua possível origem. A cada rodada, é apresentada uma situação e o jogador precisa escolher entre as opções "Humano" ou "Inteligência Artificial".

Após cada resposta, o jogo apresenta o resultado e uma explicação sobre o conteúdo analisado, incentivando o pensamento crítico sobre a utilização da IA e a confiabilidade das ferramentas de detecção.

O jogo também aborda os limites da identificação automatizada, demonstrando que ferramentas de detecção podem apresentar erros e que nem sempre é possível determinar a origem de um conteúdo com certeza.

## Objetivo do jogador

O objetivo é investigar os conteúdos apresentados ao longo das rodadas, identificar corretamente sua origem e acumular pontos antes que o tempo termine ou todas as vidas sejam perdidas.

Ao avançar, o jogador terá contato com diferentes exemplos e situações relacionadas ao uso da inteligência artificial no cotidiano, desenvolvendo uma postura mais crítica e consciente diante dos conteúdos digitais.

## Regras do jogo

O jogador inicia a partida com uma quantidade determinada de vidas e um cronômetro.

A cada rodada, um conteúdo é apresentado na tela para análise.

O jogador deve escolher entre as opções "Humano" ou "Inteligência Artificial".

Cada resposta correta aumenta a pontuação.

Cada resposta incorreta reduz a quantidade de vidas.

Após cada resposta, o jogo apresenta um feedback com a explicação correspondente.

Os desafios são selecionados a partir de um banco de conteúdos previamente cadastrado.

A partida termina quando o jogador perde todas as vidas, o tempo acaba ou todas as rodadas são concluídas.

A vitória acontece quando o jogador consegue completar todos os desafios mantendo pelo menos uma vida.

Ao final da partida, é exibido um resumo com a pontuação e o desempenho do jogador.

## Controles

Mouse: selecionar as respostas e interagir com os botões da interface.

ENTER: confirmar ações e avançar entre as telas.

ESC: retornar ao menu ou sair do jogo.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
