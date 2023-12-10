import pygame
from datos import lista
from constantes import *
import pygame.mixer

class Juego:
    def __init__(self):
        # Listas
        self.preguntas = []
        self.opcion_a = []
        self.opcion_b = []
        self.opcion_c = []
        self.respuesta = []

        # Puntaje, contador, respuesta seleccionada, banderas
        self.score = 0
        self.contador = 0
        self.bandera_inicial = False
        self.respuesta_seleccionada = ""
        self.oportunidades_restantes = 2
        self.bandera_final = False

        for i in range(len(lista)):
            self.preguntas.append(lista[i]["pregunta"])
            self.opcion_a.append(lista[i]["a"])
            self.opcion_b.append(lista[i]["b"])
            self.opcion_c.append(lista[i]["c"])
            self.respuesta.append(lista[i]["correcta"])

        # Inicializar Pygame
        pygame.init()
        self.pantalla = pygame.display.set_mode([1200, 675])  # Ancho y Alto
        pygame.display.set_caption("Desafío Preguntados")
        self.icono = pygame.image.load("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/Imagenes/Logo.jpg")
        pygame.display.set_icon(self.icono)
        self.fondo_pantalla = pygame.image.load("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/Imagenes/Fondo.jpg")
        self.imagen_reset = pygame.image.load("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/Imagenes/Reset.jpg")

        # Música
        pygame.mixer.init()
        self.sonido_correcto = pygame.mixer.Sound("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/sonidos/respuesta_correcta.wav")
        self.sonido_incorrecto = pygame.mixer.Sound("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/sonidos/respuesta_incorrecta.wav")
        self.musica_fondo = pygame.mixer.Sound("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/sonidos/musica_fondo.wav")
        self.sonido_pregunta = pygame.mixer.Sound("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/sonidos/pregunta.wav")
        self.sonido_reiniciar = pygame.mixer.Sound("C:/Users/nicky/OneDrive/Escritorio/Python 1er cuatri/Desafio Preguntados/sonidos/reiniciar.wav")
        self.musica_fondo.play()


        # Fuente de Texto
        self.arial = pygame.font.SysFont("arial", 38)
        self.comicsansms = pygame.font.SysFont("comicsans", 20)
        self.comicsansms_finalizado = pygame.font.SysFont("comicsans", 30)

        # Texto
        self.texto_pregunta_sig = self.arial.render("Pregunta", True, (Blanco))
        self.texto_reiniciar = self.arial.render("Reiniciar", True, (Blanco))
        self.texto_score = self.comicsansms.render("Score:", True, (Blanco))
        self.texto_score_0 = self.comicsansms.render("0", True, (Blanco))
        self.texto_opcion_A = self.comicsansms.render("A.", True, (Blanco))
        self.texto_opcion_B = self.comicsansms.render("B.", True, (Blanco))
        self.texto_opcion_C = self.comicsansms.render("C.", True, (Blanco))
        self.texto_preguntas = self.comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
        self.texto_finalizado = self.comicsansms_finalizado.render("¡Juego finalizado!", True, (Blanco))
        self.texto_score_final = self.comicsansms.render("Puntaje final: " + str(self.score), True, (Blanco))
        self.texto_reset = self.comicsansms.render("¿Desea jugar de nuevo?", True, (Blanco))

        # Rectángulos
        self.deco_p_rect = pygame.Rect((115, 165), (970, 100))
        self.deco_r_rect = pygame.Rect((45, 20), (230, 110))
        self.deco_sp_rect = pygame.Rect((925, 20), (230, 115))
        self.deco_sc_rect = pygame.Rect((485, 45), (210, 80))
        self.deco_a_rect = pygame.Rect((295, 315), (610, 80))
        self.deco_b_rect = pygame.Rect((295, 415), (610, 80))
        self.deco_c_rect = pygame.Rect((295, 515), (610, 80))

        self.pregunta_sig_rect = pygame.Rect((930, 25), (220, 100))
        self.reiniciar_rect = pygame.Rect((50, 25), (220, 100))
        self.score_rect = pygame.Rect((490, 50), (200, 70))
        self.preguntas_rect = pygame.Rect((120, 170), (960, 90))
        self.respuesta_A_rect = pygame.Rect((300, 320), (600, 70))
        self.respuesta_B_rect = pygame.Rect((300, 420), (600, 70))
        self.respuesta_C_rect = pygame.Rect((300, 520), (600, 70))
        self.fondo_final_rect = pygame.Rect((405, 25), (380, 210))
        self.final_rect = pygame.Rect((410, 30), (370, 200))

    def ejecutar(self):
        bandera = True

        while bandera:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion_click = list(evento.pos)
                    self.verificar_click(posicion_click)

                # Quitar el Juego
                if evento.type == pygame.QUIT:
                    bandera = False

            self.actualizar_pantalla()
            pygame.display.flip()

    def verificar_click(self, posicion_click):
        if self.bandera_final:
            self.verificar_click_final(posicion_click)
        else:
            self.verificar_click_juego(posicion_click)

    def verificar_click_final(self, posicion_click):
        if (540 < posicion_click[0] < 630) and (130 < posicion_click[1] < 220):
            self.iniciar_juego()

    def verificar_click_juego(self, posicion_click):
        # Boton reiniciar
        if (50 < posicion_click[0] < 270) and (25 < posicion_click[1] < 125):
            self.iniciar_juego()
            self.sonido_reiniciar.play()

        # Boton pregunta
        if (930 < posicion_click[0] < 1150) and (25 < posicion_click[1] < 125):
            self.mostrar_siguiente_pregunta()
            self.sonido_pregunta.play()

        # Verifica si la opción seleccionada es correcta
        if (300 < posicion_click[0] < 900):
            if (320 < posicion_click[1] < 390):
                self.verificar_respuesta("a")
            elif (420 < posicion_click[1] < 490):
                self.verificar_respuesta("b")
            elif (520 < posicion_click[1] < 590):
                self.verificar_respuesta("c")

    def mostrar_siguiente_pregunta(self):
        if self.contador < len(self.preguntas):
            self.texto_preguntas = self.comicsansms.render(self.preguntas[self.contador], True, (Blanco))
            self.texto_opcion_A = self.comicsansms.render("A. " + self.opcion_a[self.contador], True, (Blanco))
            self.texto_opcion_B = self.comicsansms.render("B. " + self.opcion_b[self.contador], True, (Blanco))
            self.texto_opcion_C = self.comicsansms.render("C. " + self.opcion_c[self.contador], True, (Blanco))
            self.texto_score_0 = self.comicsansms.render(f"{self.score}", True, (Blanco))
            self.contador += 1
            self.bandera_inicial = True
            self.oportunidades_restantes = 2
        else:
            self.texto_preguntas = self.comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
            self.texto_opcion_A = self.comicsansms.render("A.", True, (Blanco))
            self.texto_opcion_B = self.comicsansms.render("B.", True, (Blanco))
            self.texto_opcion_C = self.comicsansms.render("C.", True, (Blanco))
            self.texto_score_0 = self.comicsansms.render("0", True, (Blanco))
            self.bandera_inicial = False
            self.contador = 0
            self.bandera_final = True
            self.texto_score_final = self.comicsansms.render("Puntaje final: " + str(self.score), True, (Blanco))
            self.score = 0

    def verificar_respuesta(self, opcion):
        self.respuesta_seleccionada = opcion
        if self.contador < len(self.preguntas):
            if self.bandera_inicial and self.respuesta_seleccionada == self.respuesta[self.contador - 1]:
                self.score += 10
                self.sonido_correcto.play()
                self.mostrar_siguiente_pregunta()
            else:
                if self.oportunidades_restantes > 1:
                    self.sonido_incorrecto.play()
                    self.oportunidades_restantes -= 1
                else:
                    self.sonido_incorrecto.play()
                    self.mostrar_siguiente_pregunta()

    def iniciar_juego(self):
        self.contador = 0
        self.score = 0
        self.bandera_inicial = False
        self.texto_preguntas = self.comicsansms.render("¡Haga click en pregunta para comenzar!", True, (Blanco))
        self.texto_opcion_A = self.comicsansms.render("A.", True, (Blanco))
        self.texto_opcion_B = self.comicsansms.render("B.", True, (Blanco))
        self.texto_opcion_C = self.comicsansms.render("C.", True, (Blanco))
        self.texto_score_0 = self.comicsansms.render("0", True, (Blanco))
        self.bandera_final = False

    def actualizar_pantalla(self):
        self.pantalla.blit(self.fondo_pantalla, (0, 0))

        if self.bandera_final:
            pygame.draw.rect(self.pantalla, (Blanco), self.fondo_final_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Negro), self.final_rect, 0, 20)
            self.pantalla.blit(self.texto_finalizado, (470, 610))
            self.pantalla.blit(self.texto_score_final, (520, 40))
            self.pantalla.blit(self.imagen_reset, (540, 130))
            self.pantalla.blit(self.texto_reset, (480, 85))

        else:
            pygame.draw.rect(self.pantalla, (Naranja_oscuro), self.deco_p_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Rojo_oscuro), self.deco_r_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Verde_oscuro), self.deco_sp_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Amarillo_oscuro), self.deco_sc_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul_oscuro), self.deco_a_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul_oscuro), self.deco_b_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul_oscuro), self.deco_c_rect, 0, 20)

            pygame.draw.rect(self.pantalla, (Verde), self.pregunta_sig_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Rojo), self.reiniciar_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Amarillo), self.score_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Naranja), self.preguntas_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul), self.respuesta_A_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul), self.respuesta_B_rect, 0, 20)
            pygame.draw.rect(self.pantalla, (Azul), self.respuesta_C_rect, 0, 20)
            self.pantalla.blit(self.texto_pregunta_sig, (965, 50))
            self.pantalla.blit(self.texto_reiniciar, (85, 50))
            self.pantalla.blit(self.texto_score, (540, 70))
            self.pantalla.blit(self.texto_score_0, (620, 70))
            self.pantalla.blit(self.texto_opcion_A, (320, 340))
            self.pantalla.blit(self.texto_opcion_B, (320, 440))
            self.pantalla.blit(self.texto_opcion_C, (320, 540))
            self.pantalla.blit(self.texto_preguntas, (180, 200))

        pygame.display.flip()

# Cerrar Pygame
if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
    pygame.quit()
