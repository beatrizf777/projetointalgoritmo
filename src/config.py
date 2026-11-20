import pygame

LARGURA, ALTURA = 900, 600
VIDAS_INICIAIS = 3
PONTOS_POR_ACERTO = 10

# Cores
FUNDO = (18, 22, 34)
BRANCO = (240, 240, 240)
CINZA = (120, 128, 145)
AZUL = (70, 120, 220)
ROXO = (140, 90, 220)
VERDE = (60, 180, 100)
VERMELHO = (210, 70, 70)

# Estados
MENU = "menu"
JOGANDO = "jogando"
FEEDBACK = "feedback"
FIM = "fim"

# Botões de resposta (Humano / IA)
BTN_HUMANO = pygame.Rect(150, 400, 280, 80)
BTN_IA = pygame.Rect(470, 400, 280, 80)

# Dificuldade
ORDEM_DIFICULDADE = {"facil": 0, "medio": 1, "dificil": 2}
NOME_DIFICULDADE = {"facil": "Fácil", "medio": "Médio", "dificil": "Difícil"}

MSG_DIFICIL_TITULO = "Nem sempre é possível distinguir!"
MSG_DIFICIL_TEXTO = "Um texto bem escrito não é necessariamente produzido por IA, assim como um texto informal não é necessariamente humano. A linguagem, sozinha, não permite confirmar a autoria."

# Rodadas e pontuação por nível
RODADAS_POR_NIVEL = 2
PONTOS_POR_NIVEL = {"facil": 15, "medio": 35, "dificil": 50}