import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Constantes
ANCHO, ALTO = 600, 400
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 50, 50)
AZUL = (50, 100, 200)
VERDE = (50, 200, 100)

FUENTE = pygame.font.SysFont(None, 36)

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Dados 2 Jugadores")

# Dibujar dado con puntos
def dibujar_dado(superficie, x, y, valor):
    tam = 60
    pygame.draw.rect(superficie, BLANCO, (x, y, tam, tam), border_radius=8)
    puntos = {
        1: [(x + 30, y + 30)],
        2: [(x + 15, y + 15), (x + 45, y + 45)],
        3: [(x + 15, y + 15), (x + 30, y + 30), (x + 45, y + 45)],
        4: [(x + 15, y + 15), (x + 45, y + 15), (x + 15, y + 45), (x + 45, y + 45)],
        5: [(x + 15, y + 15), (x + 45, y + 15), (x + 30, y + 30), (x + 15, y + 45), (x + 45, y + 45)],
        6: [(x + 15, y + 15), (x + 45, y + 15), (x + 15, y + 30), (x + 45, y + 30), (x + 15, y + 45), (x + 45, y + 45)],
    }
    for px, py in puntos[valor]:
        pygame.draw.circle(superficie, NEGRO, (px, py), 6)

# Botón
class Boton:
    def __init__(self, texto, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, VERDE, self.rect, border_radius=6)
        texto = FUENTE.render(self.texto, True, NEGRO)
        superficie.blit(texto, texto.get_rect(center=self.rect.center))

    def fue_presionado(self, pos):
        return self.rect.collidepoint(pos)

# Función principal del juego
def juego():
    turno = 0  # 0 para jugador 1, 1 para jugador 2
    puntajes = [0, 0]
    dado1, dado2 = 1, 1
    ganador = None
    reloj = pygame.time.Clock()
    boton_reiniciar = Boton("Reiniciar", ANCHO//2 - 60, ALTO//2 + 50, 120, 40)

    en_juego = True
    while True:
        pantalla.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if ganador and boton_reiniciar.fue_presionado(evento.pos):
                    return juego()

            if evento.type == pygame.KEYDOWN and en_juego:
                if evento.key == pygame.K_SPACE:
                    dado1 = random.randint(1, 6)
                    dado2 = random.randint(1, 6)
                    suma = dado1 + dado2
                    puntajes[turno] += suma
                    if puntajes[turno] >= 50:    #mayor a 50 gana
                        ganador = turno
                        en_juego = False
                    else:
                        turno = 1 - turno

        # Títulos y nombres
        txt_j1 = FUENTE.render("Jugador 1", True, ROJO)
        txt_j2 = FUENTE.render("Jugador 2", True, AZUL)
        pantalla.blit(txt_j1, (30, 20))
        pantalla.blit(txt_j2, (ANCHO - 160, 20))

        # Puntajes
        p1 = FUENTE.render(f"Puntos: {puntajes[0]}", True, BLANCO)
        p2 = FUENTE.render(f"Puntos: {puntajes[1]}", True, BLANCO)
        pantalla.blit(p1, (30, 60))
        pantalla.blit(p2, (ANCHO - 160, 60))

        # Turno
        turno_texto = f"Turno de Jugador {turno + 1} (ESPACIO para tirar)"
        turno_render = FUENTE.render(turno_texto, True, VERDE)
        pantalla.blit(turno_render, (ANCHO // 2 - turno_render.get_width() // 2, ALTO - 50))

        # Dados
        dibujar_dado(pantalla, ANCHO // 2 - 80, ALTO // 2 - 40, dado1)
        dibujar_dado(pantalla, ANCHO // 2 + 20, ALTO // 2 - 40, dado2)

        # Ganador
        if ganador is not None:
            texto_win = FUENTE.render(f"🎉 Ganó el Jugador {ganador + 1} 🎉", True, VERDE)
            pantalla.blit(texto_win, (ANCHO // 2 - texto_win.get_width() // 2, ALTO // 2 - 80))
            boton_reiniciar.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(30)

# Ejecutar juego
juego()
