# Construye un Robot mínimo con RPi que sea capaz de seguir rostros

Como todos tenéis controlado el tema de PWM con RPi, control del L298N con RPi y control de servos de 360º con RPi (no necesitamos nada Analógico, como sabéis), vamos a unir en este primer código de pruebas la magia de vuestro Chasis/Robot con la detección de rostros, para conseguir un pequeño prototipo de robot que siga un rostro humano.

Para ello, os he dejado el código de ejemplo "Seguidor_Rostros.py".

¡CUIDADO! Debéis tener en cuenta que un equipo estáis haciendo la movilidad del robot con servos 360 y el otro lo habéis probado con driver L298N, por lo que deberéis adaptar el código de ejemplo que os dejo a ello.

Imaginamos que en nuestro ejemplo tenemos frames de 640x480 píxeles, como os detallo en la figura. Debéis tener en cuenta que la IA no va a hacer caso a toda la imagen, sino sólo a un pequeño recuadro (os lo detallo en verde como objeto). 

