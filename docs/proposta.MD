# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na etapa inicial do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com **Python e Pygame** dentro do prazo disponível. Consulte o enunciado publicado no Canvas para conhecer o eixo temático e as orientações vigentes.

## 1. Nome provisório do jogo

Informe o nome provisório do jogo.

**Nome:**

> Real or Ai?

## 2. Integrantes do grupo

- Nome 1: Beatriz Carvalho
- Nome 2: Rafael Duarte

## 3. Tema escolhido

Indique qual tema específico o grupo escolheu **dentro do eixo temático definido no enunciado**.

**Tema:**

> Inteligência Artificial no cotidiano, com foco na identificação de conteúdos produzidos por inteligência artificial e por seres humanos, abordando os limites das ferramentas de detecção e a importância do pensamento crítico.

**Como esse tema se relaciona com o jogo?** Explique brevemente (2 a 4 linhas) como ele aparecerá nos objetivos, nas regras ou nos desafios, e não apenas nas imagens ou no cenário.

> O tema estará presente na mecânica principal, na qual o jogador deverá analisar diferentes textos e identificar se foram produzidos por uma pessoa ou por uma inteligência artificial. Os desafios e explicações apresentados ao longo das rodadas abordarão a confiabilidade dos conteúdos digitais, os possíveis erros de identificação e a importância de não confiar cegamente em resultados automatizados.

## 4. Tipo de jogo

Indique o estilo do jogo. Exemplos: desviar de obstáculos, coleta de itens, labirinto, perguntas e respostas, memória, Pong, Snake, Breakout, corrida ou sobrevivência simples.

**Tipo escolhido:**

> Jogo de perguntas e respostas com temática de investigação digital, classificação de conteúdos e dificuldade progressiva.

## 5. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará. O que aparece na tela? O que o jogador controla? O que ele precisa fazer e quais desafios encontrará?

**Descrição:**

> O Real or AI? é um jogo digital educativo no qual o jogador assume o papel de um investigador digital responsável por analisar conteúdos encontrados no ambiente virtual. A cada rodada, um texto será apresentado na tela, e o jogador deverá identificar se sua origem é humana ou artificial, selecionando uma das duas opções disponíveis.

O jogo contará com um sistema de pontuação, vidas e tempo, além de apresentar explicações após cada resposta. Os desafios serão organizados em rodadas com diferentes níveis de dificuldade, incentivando o jogador a desenvolver seu pensamento crítico sobre a presença da inteligência artificial no cotidiano.

## 6. Objetivo do jogador

Descreva o objetivo principal. Por exemplo: coletar itens, sobreviver por determinado tempo, chegar ao final de um percurso ou completar desafios.

**Objetivo:**

> Analisar os conteúdos apresentados durante a partida e identificar corretamente sua origem, acumulando pontos e completando todas as rodadas antes que o tempo termine ou as vidas sejam esgotada. Ao longo do jogo, o jogador também deverá compreender que a identificação de conteúdos gerados por IA possui limitações e não deve ser considerada totalmente confiável.

## 7. Regras principais

Liste até cinco regras que expliquem o funcionamento do jogo. Exemplos: o jogador começa com três vidas; acertos somam pontos; colisões retiram vidas.

- Regra 1: O jogador inicia a partida com três vidas e um tempo limite para concluir os desafios.
- Regra 2: A cada rodada, um texto é apresentado, e o jogador deve escolher entre as opções “Humano” ou “Inteligência Artificial”.
- Regra 3: Cada resposta correta adiciona pontos à pontuação, enquanto cada resposta incorreta reduz uma vida.
- Regra 4: Após cada resposta, o jogo apresenta um feedback explicativo sobre a origem do conteúdo e os aspectos relacionados à sua identificação.
- Regra 5: Os desafios são concluídos quando todas as rodadas são respondidas, quando o jogador perde todas as vidas ou quando o tempo se esgota.

## 8. Condição de vitória

Explique como o jogador vence ou conclui a partida. Exemplos: alcançar uma pontuação, finalizar uma fase ou completar todas as tarefas.

**Condição de vitória:**

> O jogador vence ao completar todas as rodadas propostas, mantendo pelo menos uma vida e respeitando o limite de tempo estabelecido. Ao final, será apresentada uma tela com a pontuação total, a quantidade de acertos e o desempenho obtido durante a investigação.

## 9. Condição de derrota ou encerramento

Explique quando a partida termina ou como o jogador perde. Exemplos: esgotar as vidas, acabar o tempo ou atingir o limite de erros.

**Condição de derrota ou encerramento:**

> A partida será encerrada quando o jogador perder todas as três vidas ou quando o tempo limite terminar antes da conclusão dos desafios. Em ambos os casos, será exibida uma tela de resultado com a pontuação alcançada e o desempenho do jogador.

## 10. Elementos previstos no jogo

Descreva brevemente os elementos mais importantes, sem precisar detalhar a implementação.

- **Personagem ou elemento principal:** O investigador digital, representado pela interface de investigação e pelos elementos visuais que simulam a análise de conteúdos.
- **Obstáculos ou desafios:** Textos de diferentes características e níveis de dificuldade, cuja origem deverá ser identificada pelo jogador.
- **Itens ou objetos de interação (se houver):** Botões de seleção das respostas e elementos de interação com os desafios.
- **Pontuação, vidas, tempo ou progresso:** Sistema de pontos por acertos, três vidas iniciais e cronômetro para limitar a partida.

## 11. Controles previstos

Informe como o jogador vai interagir com o jogo (por exemplo, setas para movimentar, espaço para agir ou mouse para selecionar).

**Controles:**

> Mouse: selecionar as respostas e interagir com os botões da interface.
ENTER: confirmar ações e avançar entre as telas.
ESC: retornar ao menu ou encerrar o jogo.

## 12. Principais dificuldades esperadas

Cite até três dificuldades que o grupo espera enfrentar. Exemplos: movimentação, colisões, controle de tempo, testes ou uso do GitHub.

- Dificuldade 1: Desenvolver uma interface visual organizada e funcional utilizando a biblioteca Pygame.
- Dificuldade 2: Implementar corretamente a lógica das rodadas, incluindo pontuação, vidas, cronômetro e apresentação dos feedbacks.
- Dificuldade 3: Organizar o banco de conteúdos, modularizar o código e realizar testes para garantir o funcionamento adequado do jogo.

## 13. Escopo mínimo para a entrega final

Descreva a **versão mais simples que já seria jogável**, com as interações e regras essenciais. Evite planejar funcionalidades demais.

**Escopo mínimo:**

> A versão mínima do Real or AI? contará com um menu inicial, uma modalidade principal de investigação de textos e pelo menos dez desafios previamente cadastrados. O jogador deverá analisar cada conteúdo e selecionar uma das opções disponíveis para identificar sua origem. O jogo deverá possuir sistema de pontuação, três vidas, cronômetro, feedback após as respostas e telas de vitória e derrota. Também deverá apresentar um resumo do desempenho ao final da partida e permitir o armazenamento das melhores pontuações em arquivo.

## 14. Possíveis melhorias, caso haja tempo

Liste até três funcionalidades extras para implementar somente depois que a versão mínima estiver funcionando. Exemplos: sons, fases, ranking, animações ou menu inicial.

- Melhoria 1: Implementação de uma funcionalidade na qual o jogador poderá inserir um texto próprio para receber uma análise experimental de características da escrita, sem afirmar que é possível determinar sua autoria com precisão.
- Melhoria 2: Criação de novas categorias de desafios, incluindo situações relacionadas a imagens manipuladas, notícias falsas, golpes digitais e privacidade.
- Melhoria 3: Implementação de recursos visuais adicionais, como animações, efeitos sonoros, níveis de dificuldade e aprimoramento do ranking.
