#---------------------------------------------------------------------------------------------
#Programa para dibujar figuras geométricas regulares en el centro de la pantalla
#---------------------------------------------------------------------------------------------

#Importo las librerias necesarias así como el otro archivo llamado 'apoyo'
import pygame
import apoyo
import math

#Inicio pygame
pygame.init()
#Pongo una resolución de pantalla
alto = 500
anch = 500
#Dicha resolución es almacenada en un array
resol = [alto,anch]
#Obtengo el centro de la pantalla
centro = [alto/2,anch/2]
#Llamo al display de pantalla con dicha resolución
screen = pygame.display.set_mode(resol)


#Dibujo una figura geométrica con una longitud y un numero de lados predeterminados
long = 80
num_lados = 4
#Dibujo cualquier figura regular
for i in range(num_lados):
        #Obtengo el angulo en el que se encuentra el primer punto
        ang = math.radians((360/num_lados)*i)
        #Obtengo el angulo en el que se encuentra el segundo punto
        angsig = math.radians((360/num_lados)*(i+1)) 
        #Con trigonometría paso de un angulo y una distancia, a un punto llamado A
        puntoA = [long*math.cos(ang)+(alto/2),long*math.sin(ang)+(anch/2)]
        #Con trigonometría paso de un angulo y una distancia, a un punto llamado B
        puntoB = [long*math.cos(angsig)+(alto/2),long*math.sin(angsig)+(anch/2)]
        #Dibujo la línea entre ambos puntos
        pygame.draw.line(screen,apoyo.colores[1],puntoA,puntoB)

#Actualizo la pantalla tras dibujar la figura
pygame.display.flip()

#Creo un bucle infinito para observar si se ha pulsado el botón de salida.
running = True
while running:
    #Si se ha pulsado, salgo del bucle infinito
    running = apoyo.parada()
#Cierro la pantalla
pygame.quit()


