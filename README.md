# Polígonos regulares
Empleando trigonometría obtengo una forma de como dibujar figuras geométricas simples en Python empleando Pygame.

Para ello me baso en la teoría de los vectores, la cual explico brevemente y con mis propias palabras a continuación:

Un vector tiene 4 elementos: Modulo, dirección, sentido y punto de aplicación.
  * Modulo: Longitud del vector, indica como de grande o pequeño es.
  * Dirección: El angulo que tiene respecto al eje X
  * Sentido: La orientación de dicho segmento
  * Punto de aplicación: Punto de origen del vector

El punto de aplicación es conocido, el cuál es el punto central de la ventana creada en pygame. La distancia al centro es dada por el usuario así como el número de lados del polígono a crear.

Una vez conocido el punto de aplicación, el módulo y la dirección del vector, puedo obtener los puntos que los conforman para así dibujar el polígono.

1º 'num_lados' es el número de lados del polígono y 'long' es la distancia de ese punto al centro de la ventana (Ambos modificables por el usuario)

2º Divido 360º entre 'num_lados' (360/num_lados). Así obtengo el ángulo del primer punto. Una vez obtenido ese angulo, calculo los puntos (xi,yi) que se encuentran a dicha distancia. Dichos puntos serían:
  * xi = long*coseno((360/num_lados)*i)
  * yi = long*seno((360/num_lados)*i)
  
Donde 'i' indica los números naturales desde 1 hasta 'num_lados' i = [1,num_lados]

3º Repito el paso 2, 2 veces para obtener el punto (xi,yi) y el punto (xi+1,yi+1). Ambos puntos pertenecen al polígono. 

4º Creo una línea entre ambos puntos. Haciendo esto, acabo cerrando el polígono regular. 

Esta parte puede ser la más complicada y por tanto por eso la desarrollo aquí. El resto está explicado en el código. 
