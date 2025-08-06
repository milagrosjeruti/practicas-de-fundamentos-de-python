import pygame
import sys

# Inicializar pygame
pygame.init()

# Pantalla
ANCHO, ALTO = 900, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("JUEGOS DE DISPAROS!!!!! - 2 Jugadores")

# Colores
NEGRO = (0, 0, 0)
ROJO = (225, 0, 98)
AZUL = (1, 0, 200)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
GRIS = (130, 100, 130)
FONDO_ROJO = (20, 0, 10)
FONDO_AZUL = (0, 0, 50)
FONDO_VERDE = (0, 50, 0)

# Fuente
fuente = pygame.font.SysFont("New Roman", 50)
fuente_grande = pygame.font.SysFont("Arial", 50)

# Variables de juego
reloj = pygame.time.Clock()
velocidad = 5
vel_bala = 10
recarga_ms = 500

# Obstáculos
obstaculo = pygame.Rect(375, 200, 50, 200)

# Función para mostrar texto centrado
def dibujar_texto(texto, fuente, color, y):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=(ANCHO // 2, y))
    pantalla.blit(superficie, rect)

# Función para dibujar texto con fondo rectangular
def dibujar_texto_con_fondo(texto, fuente, color_texto, color_fondo, pos):
    superficie_texto = fuente.render(texto, True, color_texto)
    rect_texto = superficie_texto.get_rect(topleft=pos)
    padding = 12
    rect_fondo = pygame.Rect(
        rect_texto.left - padding,
        rect_texto.top - padding,
        rect_texto.width + 2 * padding,
        rect_texto.height + 2 * padding
    )
    pygame.draw.rect(pantalla, color_fondo, rect_fondo, border_radius=12)
    pantalla.blit(superficie_texto, rect_texto)

# Función para pedir nombres
def pedir_nombres():
    nombre1 = ""
    nombre2 = ""
    activo = 1
    escribiendo = True

    while escribiendo:
        pantalla.fill(NEGRO)
        dibujar_texto("Escribí los nombres y presioná Enter", fuente, BLANCO, 50)

        color1 = ROJO if activo == 1 else BLANCO
        color2 = AZUL if activo == 2 else BLANCO

        dibujar_texto_con_fondo(f"Jugador 1: {nombre1}", fuente, color1, FONDO_ROJO, (100, 150))
        dibujar_texto_con_fondo(f"Jugador 2: {nombre2}", fuente, color2, FONDO_AZUL, (100, 220))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if activo == 1:
                        activo = 2
                    else:
                        escribiendo = False
                elif evento.key == pygame.K_BACKSPACE:
                    if activo == 1:
                        nombre1 = nombre1[:-1]
                    else:
                        nombre2 = nombre2[:-1]
                else:
                    if activo == 1 and len(nombre1) < 10 and evento.unicode.isprintable():
                        nombre1 += evento.unicode
                    elif activo == 2 and len(nombre2) < 10 and evento.unicode.isprintable():
                        nombre2 += evento.unicode

    return nombre1 or "Jugador 1", nombre2 or "Jugador 2"

# Función principal del juego
def juego():
    jugador1 = pygame.Rect(100, 300, 50, 50)
    jugador2 = pygame.Rect(650, 300, 50, 50)
    balas_j1 = []
    balas_j2 = []
    vida_j1 = 5
    vida_j2 = 5
    tiempo_ultimo_disparo_j1 = 0
    tiempo_ultimo_disparo_j2 = 0
    corriendo = True
    ganador = None

    nombre1, nombre2 = pedir_nombres()

    while corriendo:
        reloj.tick(60)
        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                # Disparo jugador 1
                if evento.key == pygame.K_SPACE and tiempo_actual - tiempo_ultimo_disparo_j1 > recarga_ms:
                    bala = pygame.Rect(jugador1.right, jugador1.centery - 5, 10, 5)
                    balas_j1.append(bala)
                    tiempo_ultimo_disparo_j1 = tiempo_actual
                # Disparo jugador 2
                if evento.key == pygame.K_RETURN and tiempo_actual - tiempo_ultimo_disparo_j2 > recarga_ms:
                    bala = pygame.Rect(jugador2.left - 10, jugador2.centery - 5, 10, 5)
                    balas_j2.append(bala)
                    tiempo_ultimo_disparo_j2 = tiempo_actual

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and jugador1.top > 0:
            jugador1.y -= velocidad
        if teclas[pygame.K_s] and jugador1.bottom < ALTO:
            jugador1.y += velocidad
        if teclas[pygame.K_a] and jugador1.left > 0:
            jugador1.x -= velocidad
        if teclas[pygame.K_d] and jugador1.right < ANCHO:
            jugador1.x += velocidad

        if teclas[pygame.K_UP] and jugador2.top > 0:
            jugador2.y -= velocidad
        if teclas[pygame.K_DOWN] and jugador2.bottom < ALTO:
            jugador2.y += velocidad
        if teclas[pygame.K_LEFT] and jugador2.left > 0:
            jugador2.x -= velocidad
        if teclas[pygame.K_RIGHT] and jugador2.right < ANCHO:
            jugador2.x += velocidad

        # Mover balas
        for bala in balas_j1:
            bala.x += vel_bala
        for bala in balas_j2:
            bala.x -= vel_bala

        # Colisiones
        for bala in balas_j1[:]:
            if obstaculo.colliderect(bala):
                balas_j1.remove(bala)
            elif jugador2.colliderect(bala):
                vida_j2 -= 1
                balas_j1.remove(bala)
            elif bala.x > ANCHO:
                balas_j1.remove(bala)

        for bala in balas_j2[:]:
            if obstaculo.colliderect(bala):
                balas_j2.remove(bala)
            elif jugador1.colliderect(bala):
                vida_j1 -= 1
                balas_j2.remove(bala)
            elif bala.x < 0:
                balas_j2.remove(bala)

        if vida_j1 <= 0:
            ganador = nombre2
            corriendo = False
        elif vida_j2 <= 0:
            ganador = nombre1
            corriendo = False

        # Dibujar
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, ROJO, jugador1)
        pygame.draw.rect(pantalla, AZUL, jugador2)
        pygame.draw.rect(pantalla, GRIS, obstaculo)

        for bala in balas_j1:
            pygame.draw.rect(pantalla, BLANCO, bala)
        for bala in balas_j2:
            pygame.draw.rect(pantalla, BLANCO, bala)

        # Barras de vida
        pygame.draw.rect(pantalla, ROJO, (20, 20, vida_j1 * 30, 20))
        pygame.draw.rect(pantalla, AZUL, (ANCHO - 20 - vida_j2 * 30, 20, vida_j2 * 30, 20))

        # Nombres con fondo
        dibujar_texto_con_fondo(nombre1, fuente, ROJO, FONDO_ROJO, (20, 50))
        dibujar_texto_con_fondo(nombre2, fuente, AZUL, FONDO_AZUL, (ANCHO - fuente.size(nombre2)[0] - 28, 50))

        pygame.display.flip()

    # Pantalla final con opción de reiniciar
    esperando = True
    while esperando:
        pantalla.fill(NEGRO)
        dibujar_texto_con_fondo(f"¡{ganador} ha ganado!", fuente_grande, VERDE, FONDO_VERDE, (ANCHO//2 - 200, ALTO // 2 - 50))
        dibujar_texto("Presioná R para reiniciar o ESC para salir", fuente, BLANCO, ALTO // 2 + 20)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    juego()
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Ejecutar el juego
juego()