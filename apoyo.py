#Importo la libreria de pygame
import pygame

#Creo un función llamada parada
def parada():
    #Comprueba si se ha obtenido un evento
    for event in pygame.event.get():
        #Si ese evento es la pulsación del botón de escape entra
        if event.type == pygame.QUIT:
            #Esto hace que deje el bucle infinito
            return False
    #De no ser introducido, sigue el bucle
    return True


#Defino los colores a emplear
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

#Son guardados en un array para ser usados más facilmente en el programa principal
colores = [BLACK,WHITE]
