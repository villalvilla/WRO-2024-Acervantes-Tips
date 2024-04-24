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

