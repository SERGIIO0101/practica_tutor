#PASO 1: CONFIGURACIÓN INICIAL

#   Importar librerias
import pygame
import sys
import random

from pygame.time import Clock

#   Inicializar Pygame
pygame.init()

#   Tamaño ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("!Evita al enemigo!")

#   Colores
BLANCO = (255, 255, 255)
NEGRO  = (0, 0, 0)
ROJO   = (200, 0, 0)
AZUL   = (0, 100, 255)

# Reloj y FPS
clock = pygame.time.Clock()
FPS = 60

#PASO 2: FUNCIONES

#   Menú
def mostrar_menu():
    while True:
        ventana.fill (NEGRO)
        fuente = pygame.font.SysFont(None, 60)
        texto = fuente.render("Presiona ESPACIO para jugar", True, BLANCO)
        ventana.blit(texto, (180, 250))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit ()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                return

#   Jugador
def dibujar_jugador(x, y):
    pygame.draw.rect(ventana, AZUL, (x, y, 50, 50))

#   Enemigos
def dibujar_enemigos(lista_enemigos):
    for enemigo in lista_enemigos:
        pygame.draw.rect (ventana, ROJO, enemigo)

#   Generar enemigo
def generar_enemigo():
    x = random.randint(0, ANCHO - 50)
    return pygame.Rect(x, -50, 50, 50)

#   Colisión
def detectar_colision(jugador, enemigos):
    for enemigo in enemigos:
        if jugador.colliderect(enemigo):
            return True
    return False

#   Mensaje de Game Over (Presionar R para reiniciar)
def mostrar_game_over():
    fuente = pygame.font.SysFont(None, 60)
    texto  = fuente.render("¡Perdiste!, presiona R para volver a intentarlo", True, BLANCO)
    ventana.blit(texto, (250, 250))

    fuente2= pygame.font.SysFont(None, 36)
    texto2 = fuente2.render("Presiona R para reiniciar", True, BLANCO)
    ventana.blit(texto2, (240, 320))

    pygame.display.flip()
    esperar_reinicio()

def esperar_reinicio():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                return

#PASO 3: LÓGICA PRINCIPAL
def jugar():
    jugador  = pygame.Rect(375, 500, 50, 50)
    enemigos = []
    contador = 0
    velocidad_enemigos = 3
    velocidad_jugador  = 5
    puntos = 0

    corriendo = True
    while corriendo:
        clock.tick(FPS)
        ventana.fill(NEGRO)

        #   Contador para generar enemigos
        contador += 1
        if contador % 300 == 0:
            velocidad_enemigos += 0.5

        if contador % 60 == 0:
            enemigos.append(generar_enemigo())
            puntos += 1

        #   Movimiento del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidad_jugador
        if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
            jugador.x += velocidad_jugador

        #   Muevo los enemigos hacia abajo
        for enemigo in enemigos:
            enemigo.y += velocidad_enemigos

        #   Elimino enemigos que salen de pantalla
        enemigos = [e for e in enemigos if e.y < ALTO]

        #   Dibujo todo
        dibujar_jugador(jugador.x, jugador.y)
        dibujar_enemigos(enemigos)

        #   Mostrar puntos en pantalla
        fuente_puntos = pygame.font.SysFont(None, 36)
        texto_puntos  = fuente_puntos.render(f"Puntos: {puntos}", True, BLANCO)
        ventana.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() // 2, 10))
        #   Detectar Colisión
        if detectar_colision(jugador, enemigos):
            mostrar_game_over()
            return

        pygame.display.flip()

        #   Evento de salida
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #   Bucle principal
while True:
    mostrar_menu()
    jugar()




