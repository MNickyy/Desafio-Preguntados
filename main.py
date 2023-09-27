import pygame
from datos import lista
from constantes import *

# Listas
preguntas = []
opcion_a = []
opcion_b = []
opcion_c = []
respuesta = []

# Puntaje, contador, respuesta seleccionada, banderas
score = 0
contador = 0
bandera_inicial = False
respuesta_seleccionada = ""
oportunidades_restantes = 2
bandera_final = False

for i in range(len(lista)):
    preguntas.append(lista[i]["pregunta"])
    opcion_a.append(lista[i]["a"])
    opcion_b.append(lista[i]["b"])
    opcion_c.append(lista[i]["c"])
    respuesta.append(lista[i]["correcta"])

pygame.init()
pantalla = pygame.display.set_mode([1200, 675])  # Ancho y Alto
bandera = True

# Fondo, Título, Ícono
pygame.display.set_caption("Desafio Preguntados")
icono = pygame.image.load("Imagenes\Logo.jpg")
pygame.display.set_icon(icono)
fondo_pantalla = pygame.image.load("Imagenes\Fondo.jpg")
imagen_reset = pygame.image.load("Imagenes\Reset.jpg")


# Fuente de Texto
arial = pygame.font.SysFont("arial", 38)
comicsansms = pygame.font.SysFont("comicsans", 20)
comicsansms_finalizado = pygame.font.SysFont("comicsans", 30)

# Texto
texto_pregunta_sig = arial.render("Pregunta", True, (Blanco))
texto_reiniciar = arial.render("Reiniciar", True, (Blanco))
texto_score = comicsansms.render("Score:", True, (Blanco))
texto_score_0 = comicsansms.render("0", True, (Blanco))
texto_opcion_A = comicsansms.render("A.", True, (Blanco))
texto_opcion_B = comicsansms.render("B.", True, (Blanco))
texto_opcion_C = comicsansms.render("C.", True, (Blanco))
texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
texto_finalizado = comicsansms_finalizado.render("¡Juego finalizado!", True, (Blanco))
texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
texto_reset = comicsansms.render("¿Desea jugar de nuevo?", True, (Blanco))

# Rectángulos
deco_p_rect = pygame.Rect((115, 165), (970, 100))
deco_r_rect = pygame.Rect((45, 20), (230, 110))
deco_sp_rect = pygame.Rect((925, 20), (230, 115))
deco_sc_rect = pygame.Rect((485, 45), (210, 80))
deco_a_rect = pygame.Rect((295, 315), (610, 80))
deco_b_rect = pygame.Rect((295, 415), (610, 80))
deco_c_rect = pygame.Rect((295, 515), (610, 80))

pregunta_sig_rect = pygame.Rect((930, 25), (220, 100))
reiniciar_rect = pygame.Rect((50, 25), (220, 100))
score_rect = pygame.Rect((490, 50), (200, 70))
preguntas_rect = pygame.Rect((120, 170), (960, 90))
respuesta_A_rect = pygame.Rect((300, 320), (600, 70))
respuesta_B_rect = pygame.Rect((300, 420), (600, 70))
respuesta_C_rect = pygame.Rect((300, 520), (600, 70))
fondo_final_rect = pygame.Rect((405, 25), (380, 210))
final_rect = pygame.Rect((410, 30), (370, 200))

# Empieza el juego
while bandera:
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            if (bandera_final == True):
                if((posicion_click[0] > 540 and posicion_click [0] < 630) and (posicion_click[1] > 130 and posicion_click[1] < 220)):
                    contador = 0
                    score = 0
                    bandera_inicial = False
                    texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                    texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                    texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                    texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                    texto_score_0 = comicsansms.render("0", True, (Blanco))
                    
                    bandera_final = False
                    
            # Boton reiniciar
            if ((posicion_click[0] > 50 and posicion_click[0] < 270) and (posicion_click[1] > 25 and posicion_click[1] < 125)):
                contador = 0
                score = 0
                bandera_inicial = False
                texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                texto_score_0 = comicsansms.render("0", True, (Blanco))
                
            # Boton pregunta
            if ((posicion_click[0] > 930 and posicion_click[0] < 1150) and (posicion_click[1] > 25 and posicion_click[1] < 125)):
                if contador < len(preguntas):
                    print(contador)
                    texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                    texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                    texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                    texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                    texto_score_0 = comicsansms.render(f"{score}", True, (Blanco))
                    contador += 1
                    bandera_inicial = True
                    oportunidades_restantes = 2
                else:
                    texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                    texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                    texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                    texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                    texto_score_0 = comicsansms.render("0", True, (Blanco))
                    bandera_inicial = False
                    contador = 0
                    bandera_final = True
                    texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                    score = 0

            # Verifica si la opción seleccionada es correcta
            if ((posicion_click[0] > 300 and posicion_click[0] < 900) and (posicion_click[1] > 320 and posicion_click[1] < 390)):
                respuesta_seleccionada = "a"
                if contador < len(preguntas):
                    print(contador)
                    if ((bandera_inicial == True) and (respuesta_seleccionada == respuesta[contador-1])):
                        score += 10
                        texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                        texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                        texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                        texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                        texto_score_0 = comicsansms.render(f"{score}", True, (Blanco))
                        contador += 1
                        oportunidades_restantes = 2
                    else:
                        if (oportunidades_restantes == 2) and (bandera_inicial == False):
                            pass
                        elif  (oportunidades_restantes > 1):
                            oportunidades_restantes -= 1
                        else:
                        # Avanzar a la siguiente pregunta si no quedan oportunidades
                            if contador < len(preguntas):
                                texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                                texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                                texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                                texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                                contador += 1
                                oportunidades_restantes = 2  # Reiniciar oportunidades
                            else:
                                contador = 0
                                bandera_inicial = False
                                texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                                texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                                texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                                texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                                texto_score_0 = comicsansms.render("0", True, (Blanco))
                                bandera_final = True
                                texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                                score = 0
                else:
                    contador = 0
                    bandera_inicial = False
                    texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                    texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                    texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                    texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                    texto_score_0 = comicsansms.render("0", True, (Blanco))
                    bandera_final = True
                    texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                    score = 0

            if ((posicion_click[0] > 300 and posicion_click[0] < 900) and (posicion_click[1] > 420 and posicion_click[1] < 490)):
                respuesta_seleccionada = "b"
                if contador < len(preguntas):
                    print(contador)
                    if (bandera_inicial == True) and (respuesta_seleccionada == respuesta[contador-1]):
                        score += 10
                        texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                        texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                        texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                        texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                        texto_score_0 = comicsansms.render(f"{score}", True, (Blanco))
                        contador += 1
                        oportunidades_restantes = 2
                    else:
                        if (oportunidades_restantes == 2) and (bandera_inicial == False):
                            pass
                        elif  (oportunidades_restantes > 1):
                            oportunidades_restantes -= 1
                        else:
                        # Avanzar a la siguiente pregunta si no quedan oportunidades
                            if contador < len(preguntas):
                                texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                                texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                                texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                                texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                                oportunidades_restantes = 2  # Reiniciar oportunidades
                                contador += 1
                            else:
                                contador = 0
                                bandera_inicial = False
                                texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                                texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                                texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                                texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                                texto_score_0 = comicsansms.render("0", True, (Blanco))
                                bandera_final = True
                                texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                                score = 0
                else:
                    contador = 0
                    bandera_inicial = False
                    texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                    texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                    texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                    texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                    texto_score_0 = comicsansms.render("0", True, (Blanco))
                    bandera_final = True
                    texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                    score = 0

            if ((posicion_click[0] > 300 and posicion_click[0] < 900) and (posicion_click[1] > 520 and posicion_click[1] < 590)):
                respuesta_seleccionada = "c"
                if contador < len(preguntas):
                    print(contador)
                    if (bandera_inicial == True) and (respuesta_seleccionada == respuesta[contador-1]):
                        score += 10
                        texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                        texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                        texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                        texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                        texto_score_0 = comicsansms.render(f"{score}", True, (Blanco))
                        contador += 1
                        oportunidades_restantes = 2
                    else:
                        if (oportunidades_restantes == 2) and (bandera_inicial == False):
                            pass
                        elif  (oportunidades_restantes > 1):
                            oportunidades_restantes -= 1
                        else:
                        # Avanzar a la siguiente pregunta si no quedan oportunidades
                            if contador < len(preguntas):
                                texto_preguntas = comicsansms.render(preguntas[contador], True, (Blanco))
                                texto_opcion_A = comicsansms.render("A. " + opcion_a[contador], True, (Blanco))
                                texto_opcion_B = comicsansms.render("B. " + opcion_b[contador], True, (Blanco))
                                texto_opcion_C = comicsansms.render("C. " + opcion_c[contador], True, (Blanco))
                                oportunidades_restantes = 2  # Reiniciar oportunidades
                                contador += 1
                            else:
                                contador = 0
                                bandera_inicial = False
                                texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                                texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                                texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                                texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                                texto_score_0 = comicsansms.render("0", True, (Blanco))
                                bandera_final = True
                                texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                                score = 0
                else:
                    contador = 0
                    bandera_inicial = False
                    texto_preguntas = comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
                    texto_opcion_A = comicsansms.render("A.", True, (Blanco))
                    texto_opcion_B = comicsansms.render("B.", True, (Blanco))
                    texto_opcion_C = comicsansms.render("C.", True, (Blanco))
                    texto_score_0 = comicsansms.render("0", True, (Blanco))
                    bandera_final = True
                    texto_score_final = comicsansms.render("Puntaje final: " + str(score), True, (Blanco))
                    score = 0

        # Quitar el Juego
    if evento.type == pygame.QUIT:
        bandera = False

    pantalla.blit(fondo_pantalla, (0, 0))

    if (bandera_final == True):
        pygame.draw.rect(pantalla, (Blanco), fondo_final_rect, 0, 20)
        pygame.draw.rect(pantalla, (Negro), final_rect, 0, 20)
        pantalla.blit(texto_finalizado, (470, 610))
        pantalla.blit(texto_score_final, (520, 40))
        pantalla.blit(imagen_reset, (540, 130))
        pantalla.blit(texto_reset, (480, 85))

    else:
        pygame.draw.rect(pantalla, (Naranja_oscuro), deco_p_rect, 0, 20)
        pygame.draw.rect(pantalla, (Rojo_oscuro), deco_r_rect, 0, 20)
        pygame.draw.rect(pantalla, (Verde_oscuro), deco_sp_rect, 0, 20)
        pygame.draw.rect(pantalla, (Amarillo_oscuro), deco_sc_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul_oscuro), deco_a_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul_oscuro), deco_b_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul_oscuro), deco_c_rect, 0, 20)

        pygame.draw.rect(pantalla, (Verde), pregunta_sig_rect, 0, 20)
        pygame.draw.rect(pantalla, (Rojo), reiniciar_rect, 0, 20)
        pygame.draw.rect(pantalla, (Amarillo), score_rect, 0, 20)
        pygame.draw.rect(pantalla, (Naranja), preguntas_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul), respuesta_A_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul), respuesta_B_rect, 0, 20)
        pygame.draw.rect(pantalla, (Azul), respuesta_C_rect, 0, 20)
        pantalla.blit(texto_pregunta_sig, (965, 50))
        pantalla.blit(texto_reiniciar, (85, 50))
        pantalla.blit(texto_score, (560, 55))
        pantalla.blit(texto_opcion_A, (330, 340))
        pantalla.blit(texto_opcion_B, (330, 440))
        pantalla.blit(texto_opcion_C, (330, 540))
        pantalla.blit(texto_score_0, (573, 83))
        pantalla.blit(texto_preguntas, (200, 200))
    pygame.display.flip()


