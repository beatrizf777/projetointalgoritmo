import random
import pygame

from src.config import *
from src.dados import CONTEUDOS


def novo_jogo():
    # 3 humanos + 3 IAs por partida, embaralhados (ordem aleatória)
    origens = ["humano"] * 3 + ["ia"] * 3
    random.shuffle(origens)

    rodadas = []
    # Níveis na ordem fácil -> médio -> difícil, 2 rodadas por nível
    for i in range(len(origens)):
        nivel = ["facil", "medio", "dificil"][i // RODADAS_POR_NIVEL]
        candidatos = [c for c in CONTEUDOS if c["dificuldade"] == nivel and c["origem"] == origens[i] and c not in rodadas]
        rodadas.append(random.choice(candidatos))
    return {
        "rodadas": rodadas,
        "indice": 0,
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "acertou": None,
    }


def quebrar_texto(texto, fonte, largura_max):
    # Quebra o texto em linhas que cabem na largura
    linhas = []
    atual = ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if fonte.size(teste)[0] <= largura_max:
            atual = teste
        else:
            linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def desenhar_texto(tela, texto, fonte, cor, x, y, largura_max=None):
    if largura_max is None:
        tela.blit(fonte.render(texto, True, cor), (x, y))
        return y + fonte.get_linesize()
    for linha in quebrar_texto(texto, fonte, largura_max):
        tela.blit(fonte.render(linha, True, cor), (x, y))
        y += fonte.get_linesize()
    return y


def desenhar_botao(tela, rect, texto, cor, fonte):
    pygame.draw.rect(tela, cor, rect, border_radius=12)
    img = fonte.render(texto, True, BRANCO)
    tela.blit(img, img.get_rect(center=rect.center))


def desenhar_hud(tela, jogo, fonte):
    desenhar_texto(tela, f"Pontos: {jogo['pontos']}", fonte, BRANCO, 30, 20)
    desenhar_texto(tela, f"Vidas: {jogo['vidas']}", fonte, BRANCO, LARGURA - 140, 20)
    rodada = jogo["indice"] + 1
    total = len(jogo["rodadas"])
    desenhar_texto(tela, f"Rodada {rodada}/{total}", fonte, CINZA, LARGURA // 2 - 60, 20)


def tela_menu(tela, fontes):
    desenhar_texto(tela, "Real or AI?", fontes["titulo"], BRANCO, 280, 180)
    desenhar_texto(tela, "Descubra se o texto foi escrito por um humano ou por uma IA.", fontes["normal"], CINZA, 170, 270)
    desenhar_texto(tela, "ENTER para começar  |  ESC para sair", fontes["normal"], AZUL, 270, 400)


def tela_jogando(tela, jogo, fontes):
    desenhar_hud(tela, jogo, fontes["normal"])
    conteudo = jogo["rodadas"][jogo["indice"]]
    nivel = NOME_DIFICULDADE[conteudo["dificuldade"]]
    desenhar_texto(tela, "Analise o conteúdo  |  Dificuldade: " + nivel, fontes["normal"], CINZA, 60, 90)
    desenhar_texto(tela, '"' + conteudo["texto"] + '"', fontes["texto"], BRANCO, 60, 140, LARGURA - 120)
    desenhar_botao(tela, BTN_HUMANO, "Humano", AZUL, fontes["normal"])
    desenhar_botao(tela, BTN_IA, "Inteligência Artificial", ROXO, fontes["normal"])

def tela_feedback(tela, jogo, fontes):
    desenhar_hud(tela, jogo, fontes["normal"])
    conteudo = jogo["rodadas"][jogo["indice"]]
    if jogo["acertou"]:
        desenhar_texto(tela, "Correto!", fontes["titulo"], VERDE, 60, 110)
    else:
        desenhar_texto(tela, "Errou!", fontes["titulo"], VERMELHO, 60, 110)
    origem = "Humano" if conteudo["origem"] == "humano" else "Inteligência Artificial"
    desenhar_texto(tela, "Origem real: " + origem, fontes["normal"], BRANCO, 60, 210)
    y = desenhar_texto(tela, conteudo["explicacao"], fontes["normal"], CINZA, 60, 260, LARGURA - 120)

    # Mensagem especial só na fase difícil
    if conteudo["dificuldade"] == "dificil":
        y = desenhar_texto(tela, MSG_DIFICIL_TITULO, fontes["texto"], ROXO, 60, y + 25)
        desenhar_texto(tela, MSG_DIFICIL_TEXTO, fontes["normal"], BRANCO, 60, y + 5, LARGURA - 120)

    desenhar_texto(tela, "ENTER para continuar", fontes["normal"], AZUL, 60, 540)


def tela_fim(tela, jogo, fontes):
    venceu = jogo["vidas"] > 0
    titulo = "Você venceu!" if venceu else "Game over"
    cor = VERDE if venceu else VERMELHO
    desenhar_texto(tela, titulo, fontes["titulo"], cor, 60, 140)
    desenhar_texto(tela, f"Pontuação final: {jogo['pontos']}", fontes["normal"], BRANCO, 60, 240)
    desenhar_texto(tela, f"Vidas restantes: {jogo['vidas']}", fontes["normal"], BRANCO, 60, 275)
    desenhar_texto(tela, "ENTER para jogar de novo  |  ESC para o menu", fontes["normal"], AZUL, 60, 420)


def responder(jogo, escolha):
    # escolha: "humano" ou "ia"
    conteudo = jogo["rodadas"][jogo["indice"]]
    if escolha == conteudo["origem"]:
        jogo["pontos"] += PONTOS_POR_NIVEL[conteudo["dificuldade"]]
        jogo["acertou"] = True
    else:
        jogo["vidas"] -= 1
        jogo["acertou"] = False


def avancar(jogo):
    # Retorna o próximo estado
    jogo["indice"] += 1
    if jogo["vidas"] <= 0 or jogo["indice"] >= len(jogo["rodadas"]):
        return FIM
    return JOGANDO