# Aprendiendo Segmentación por Umbral:

Como habéis leído en el paso 13 del README principal, sabemos de qué se trata la segmentación por umbral:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/af4dd398-12a9-4d98-90af-7af9439dbbae)

¿Pero en qué consiste en pocas palabras? Muy sencillo: Lo que debemos hacer es una "máscara binaria", es decir, identificar el "color buscado" e intercambiarlo por un valor 1 (en este caso blanco) y el resto de los colores de la imagen los sustituiremos por el valor 0 (en este caso negro), quedando una imagen transformada de este tipo:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/0c74e970-fe7a-47ff-b4c1-f678714bb08b)

Pero aún nos quedaría saber exactamente dónde está nuestro objeto, pero esto es muy sencillo, porque si os acordáis de la semana pasada, sólo tenemos que sacar las coordenadas de los píxeles blancos y ya tendríamos la localización exacta de nuestro objeto. Una vez aplicada una técnica parecida a la de la semana pasada, podremos crear una máscara verde en tiempo real con todos los puntos de nuestro objeto, y superponerla en verde, calculando también en rojo el centroide:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/15811589-b9b5-4461-95e7-140b6a68209b)

# Programación de la Segmentación por umbral:

En el código que os dejo en esta carpeta aquí: https://github.com/villalvilla/WRO-2024-Acervantes-Tips/blob/main/Visi%C3%B3n%20artificial%20con%20Raspberry%20Pi/Robot_Seguidor_Color/segmentacionPorUmbral.py realizamos primero la segmentación por umbral, modificando por blanco el color elegido y por negro el resto de la imagen.

Para hacer esto, lo más significativo es que entendáis que es más sencillo realizar esta "conversión" del color original con el formato de imagen HSV en lugar del RGB. Para entender el formato HSV, os dejo un enlace comparativo: https://pro.arcgis.com/es/pro-app/latest/help/analysis/raster-functions/color-model-conversion-function.htm#:~:text=El%20modelo%20de%20color%20HSV,admite%20entradas%20de%203%20bandas.

Una vez conseguida la segmentación por umbral, en otro fichero diferente haremos la detección de objetos por color, para que no os liéis entre lo que es Segmentación por umbral y lo que es detección de objetos por color.

En el código de ejemplo, deberéis seleccionar un recuadro en la pantalla de la cámara del cuál detecte el color, para coger en ese momento el "color del cuál realizar la máscara".

# Programación de la Detección de objetos por color:

Partiendo del código de Segmentación de color, vamos a obtener en el siguiente código: https://github.com/villalvilla/WRO-2024-Acervantes-Tips/blob/main/Visi%C3%B3n%20artificial%20con%20Raspberry%20Pi/Robot_Seguidor_Color/deteccionPorColor.py todas las coordenadas del objeto del color deseado. Para ello, usaremos la máscara binaria y la convertiremos en un rectángulo verde, del cuál sacaremos el centroide, que pintaremos en rojo.

# Programación del robot seguidor de color:

Partiendo del código de Detección de color y del código de seguimiento de rostros que vimos la semana pasada, vamos a obtener el siguiente código: https://github.com/villalvilla/WRO-2024-Acervantes-Tips/blob/main/Visi%C3%B3n%20artificial%20con%20Raspberry%20Pi/Robot_Seguidor_Color/robotSeguidorColor.py que, lo único que hará, será modificar la parte del código que seguía rostros, para que ahora siga objetos de un color determinado.

