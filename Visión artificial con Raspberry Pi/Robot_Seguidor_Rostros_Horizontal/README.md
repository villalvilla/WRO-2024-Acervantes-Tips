# Construye un Robot mínimo con RPi que sea capaz de seguir rostros

Como todos tenéis controlado el tema de PWM con RPi, control del L298N con RPi y control de servos de 360º con RPi (no necesitamos nada Analógico, como sabéis), vamos a unir en este primer código de pruebas la magia de vuestro Chasis/Robot con la detección de rostros, para conseguir un pequeño prototipo de robot que siga un rostro humano.

Para ello, os he dejado el código de ejemplo "Seguidor_Rostros.py".

¡CUIDADO! Debéis tener en cuenta que un equipo estáis haciendo la movilidad del robot con servos 360 y el otro lo habéis probado con driver L298N, por lo que deberéis adaptar el código de ejemplo que os dejo a ello.

Imaginamos que en nuestro ejemplo tenemos frames de 640x480 píxeles, como os detallo en la figura. Debéis tener en cuenta que la IA no va a hacer caso a toda la imagen, sino sólo a un pequeño recuadro (os lo detallo en verde como objeto). 

![frame](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/4042a00e-92d4-469f-8953-8ba8521ff008)

Si la cámara del robot detecta el objeto en un lado, como os explico en la siguiente captura:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/954d3c1b-6f7c-41a4-9f30-a5fd7600b57d)

Lo que deberá hacer vuestro robot es girar las ruedas hacia la derecha (en este caso) para centrar el recuadro del objeto de nuevo en medio del frame:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/42838844-612a-41ec-8c3c-1a45827951df)

Lo que tenéis que conseguir, de primeras, es que vuestro driver de motor sea capaz de mover el robot a izquierda y derecha, para que el objeto se pueda centrar en la cámara, según vuestras necesidades. ¡OJO! Estamos considerando, tan solo, movimientos horizontales (eje X), ya que el código para centrar el objeto perfectamente en el Centro del Frame en vertical también, depende de cómo coloquéis las cámaras, el chasis, si sois capaces de elevar/bajar el chasis/cámara, etc.

Por tanto, partimos de una situación similar a esta:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/8eae6365-ad51-4993-8320-418d39b57305)

Sobre esa situación de partida, nos debemos hacer un "croquis", mediante el cuál nos definiremos a izquierda y derecha unos "límites de tolerancia", ya que los motores con los que contamos no tienen una precisión perfecta, y en la vida real contaremos con múltiples casuísticas que harán complicado que podamos trabajar en condiciones ideales. ¡RECORDAD! Siempre siempre debéis trabajar con márgenes de tolerancia y error ó sensibilidad. Se ha fijado una sensibilidad de 20 píxeles, pero se puede ir ajustando según la necesitéis:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/ef33d0eb-6544-4345-b62d-b3cbde02b477)

Una vez tenido todo esto en cuenta, calcular el "centroide" o "centro de referencia" de nuestro recuadro donde se está detectando el rostro se calcularía así:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/8a0dff8c-ac55-4c6a-9e6c-2a8c995f2f0f)

Es decir:
<pre>X+W1/2, Y+h1/2</pre>

O lo que viene siendo lo mismo: la posición de origen en X e Y donde se encuentra el recuadro del rostro más el ancho ó alto del recuadro, dividido entre 2 para hallar su Centro. 

Con esas coordenadas (siempre cogemos sólo las coordenadas X, recordad) son con las que compararemos si están (más/menos 20 píxeles) en el Centro del Frame. Resumiendo:

<pre>
  Sensores:
      lim1X = W/2 + 20
      lim2X = W/2 + 20
  Centroide:
      cX = X + W1/2
      cY = Y + H1/2
</pre>
