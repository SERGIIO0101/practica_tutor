#PASO 1: CONFIGURACIÓN INICIAL
#   Importar librerias
import pygame
import sys
import random
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
#PASO 2: FUNCIONES
#   Menú
def mostrar_menu():
    while True:
        ventana.fill (NEGRO)
        fuente = pygame.font.Sysfont(None, 60)
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
    texto = fuente.render("¡Perdiste!")