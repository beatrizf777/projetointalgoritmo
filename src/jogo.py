import pygame

from src.config import *
from src.funcoes import *


def rodar():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Real or AI?")
    relogio = pygame.time.Clock()
    fontes = {
        "titulo": pygame.font.SysFont(None, 64),
        "texto": pygame.font.SysFont(None, 36),
        "normal": pygame.font.SysFont(None, 28),
    }

    estado = MENU
    jogo = novo_jogo()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    if estado == MENU:
                        rodando = False
                    else:
                        estado = MENU
                elif evento.key == pygame.K_RETURN:
                    if estado == MENU or estado == FIM:
                        jogo = novo_jogo()
                        estado = JOGANDO
                    elif estado == FEEDBACK:
                        estado = avancar(jogo)

            elif evento.type == pygame.MOUSEBUTTONDOWN and estado == JOGANDO:
                if BTN_HUMANO.collidepoint(evento.pos):
                    responder(jogo, "humano")
                    estado = FEEDBACK
                elif BTN_IA.collidepoint(evento.pos):
                    responder(jogo, "ia")
                    estado = FEEDBACK

        tela.fill(FUNDO)
        if estado == MENU:
            tela_menu(tela, fontes)
        elif estado == JOGANDO:
            tela_jogando(tela, jogo, fontes)
        elif estado == FEEDBACK:
            tela_feedback(tela, jogo, fontes)
        elif estado == FIM:
            tela_fim(tela, jogo, fontes)

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()