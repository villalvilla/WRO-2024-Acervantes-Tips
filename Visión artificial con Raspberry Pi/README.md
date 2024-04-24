# Paso 1: Instalación de sistema operativo recomendado:

Para que todas las librerías verificadas nos funcionen bien con OpenCV, se recomienda esta versión de Raspberry Pi OS: 

https://downloads.raspberrypi.com/raspios_full_armhf/images/raspios_full_armhf-2023-05-03/2023-05-03-raspios-bullseye-armhf-full.img.xz

La instalamos con Raspberry Pi Imager ( descarga para windows desde: https://downloads.raspberrypi.org/imager/imager_latest.exe )

# Paso 2: Configuración inicial de la RPi:

Podemos hacer una configuración inicial básica desde el interfaz de Raspberry Pi Imager o bien nos saldrá el menú de configuración inicial en el primer arranque de la raspberry. Lo importante es configurarla por cable ó wifi, para que tengamos en todo momento acceso a internet para actualización de librerías, paquetes de sistema y demás recursos. La configuración de red la dejamos SIEMPRE en DHCP para no tener problemas de asignación de ips. IMPORTANTE: Activamos SSH por clave al configurar la tarjeta:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/f68d066c-d096-44a5-a7e6-ccdacb9ad1f4)

# Paso 3: Configurar VNC para conectar a la RPi desde Windows:

Como paso número 1 debemos ir a home en nuestra Raspberry, posteriormente a preferencias y a Configuración de Raspberry Pi

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/f3089f5a-148a-4c94-a1d7-5a47eed67164)


Una vez dentro de Configuración de Raspberry Pi, nos deberemos posicionar en la pestaña Interfaces, en la cual habilitaremos VNC como se muestra en la imagen, por último, debes dar clic al botón aceptar

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/0eb54ee8-9ea9-4989-a713-0a6155925157)


Perfecto, se ha habilitado la comunicación mediante VNC con la Raspberry Pi, ahora debemos de ver siempre en nuestro escritorio de nuestras Raspberry Pi el siguiente icono que se encuentra enmarcado en verde.

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/ef364369-c3da-4715-b933-30d23860b387)


Si vamos a este icono de VNC y le damos clic, se nos mostrará una ventana en la cual ubicaremos la sección Conectividad y en ella encontraremos la dirección IP de nuestra Raspberry Pi, asegúrate de tener la Raspberry Pi conectada a tu red, ya sea por WiFi o Ethernet. Ahora apunta esta dirección IP porque la necesitaremos más adelante.

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/7ea960ec-efa2-4f7f-b403-d5142da217a1)


Ahora toca el turno de pasarnos a Windows y realizar la configuración en el, son un poco más de pasos, pero igual de sencillos. Lo primero que debemos hacer es descargar en Windows el programa RealVNC Viewer del siguiente enlace: Descargar VNC Viewer, daremos clic en Download VNC Viewer

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/3dc61504-7622-48c8-85ba-493fab845e0b)


Una vez culminada la descarga, ejecutaremos el instalador y nos solicitará seleccionar el idioma y dar clic en Aceptar. Posteriormente daremos clic en Siguiente y nuevamente en Siguiente.

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/2683857e-6470-424a-b366-4581b41e4452)
 

En esta siguiente pantalla daremos también clic en Siguiente

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/1495b0d1-eed2-4407-9b9a-c37857d262c3)


Damos clic en Ejecutar, muy posiblemente nos solicite aceptar que se ejecute como administrador, comenzará la instalación y al culminar debemos dar clic en Finalizar

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/b583b41e-cbcd-40b8-b089-976f295df65e)
   

En este punto debemos ejecutar el programa RealVNC, iremos a la pestaña Archivo y daremos clic sobre Nueva conexión

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/be9b1d18-bddd-4e71-b831-2af9f0716b2d)


Al realizar el paso anterior se nos abrirá una nueva ventana, en la cual colocaremos la dirección IP que nos arrojó la Raspberry Pi en la sección Conectividad de VNC, daremos clic en Aceptar

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/0acb1937-b3d5-4731-8208-ca39dae07020)


Nos deberá aparecer de la siguiente manera, le daremos doble clic al icono que aparece con la IP de nuestra Raspberry Pi y nos saltará una nueva ventana en donde colocaremos el nombre de usuario que configuramos en la configuración inicial de nuestra Raspberry, al igual que la contraseña. Daremos clic en aceptar y se realizará la conexión con nuestra Raspberry Pi, debemos de poder ver el escritorio y controlarla con nuestro mouse y teclado en Windows.

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/bfaa9307-8bd7-42fb-bae9-8211cfafabd9)

# Paso 4: Configuración y prueba de SSH para conectarnos en remoto a la RPi desde Windows:

Si habéis seguido los pasos del paso 2, deberíais ser capaces de conectaros desde un cmd de windows 11 a vuestra raspberry pi por ssh, escribiendo el siguiente comando:
<pre>
ssh nombre_de_usuario@ip_de_la_RPi
</pre>

Recuerda sustituir nombre_de_usuario e ip_de_la_Rpi por el nombre de usuario y la ip de la raspberry correspondientes.

Te recomiendo que instales todas las librerías usando ssh, porque de esa manera podrás seguir el tutorial en windows y copiar/pegar los comandos en la shell (linea de comandos) de linux, además de poder ir documentando en tu github (esto es crucial para llevar a buen puerto vuestro proyecto) cualquier cambio o librería que no funcione correctamente con tu instalación.

A este efecto, con el objetivo de prevenir pérdidas de conexión mientras instalas paquetes en tu raspberry, te recomiendo que instales el paquete de debian "screen". Lo que hace screen es crear un proceso en el árbol raíz de procesos de linux y vincular tu shell remota a ese proceso raíz, de tal manera que, si se te corta la conexión con la RPi, el proceso sigue corriendo en background y podrás hacer un "reattach" cuando vuelvas a tener conexión, sin perder ningún proceso crítico. Para instalar screen:

<pre>
 sudo apt install screen
</pre>

Para usar screen sólo tendras que escribir en la shell de ssh "screen" (sin comillas) y te aparecerá lo siguiente:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/fdb6e531-8c83-4570-b3f2-56ef44a4d636)

Pulsa la tecla espacio para continuar y estarás dentro de screen. Para salir de screen, recuerda poner exit en el ssh.

Para reconectar una sesión perdida, prueba lo siguiente:

<pre>
 screen -ls
</pre>

Te aparecerá algo similar a esto:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/a7f5ac5b-9815-4b56-a176-709b986a4303)

El código del principio de línea es lo que tendrás que usar para reconectarte (en mi caso 19746.pts-1.rocinante)

Con ese código, simplemente haz:
<pre>
 screen -ra 19746.pts-1.rocinante
</pre>

# Paso 5: Instalación de dependencias del sistema:

Como vamos a utilizar python3 y en concreto pip installer para la mayoría de recursos, os recomiendo que uséis esta herramienta online siempre que necesitéis revisar los recursos de python y los requisitos de dependencias de los paquetes que queráis utilizar. Viene EXCELENTE saber en todo momento qué necesitamos para tener montada determinada utilidad en python o librería: [piwheels - Package List](https://www.piwheels.org/packages.html)

Dependencias para instalar:
<pre>
#comandos para verificar actualizaciones
sudo apt update
sudo apt upgrade
 
#comandos para instalar las dependencias necesarias
sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev  libqt5gui5  libqt5webkit5  libqt5test5 libilmbase-dev libopenexr-dev libgstreamer1.0-dev libavcodec-dev libavformat-dev libswscale-dev libwebp-dev
 
sudo apt install libxcb-shm0  libcdio-paranoia-dev  libsdl2-2.0-0  libxv1  libtheora0  libva-drm2  libva-x11-2  libvdpau1  libharfbuzz0b  libbluray2  libhdf5-103  libgtk-3-0  libdc1394-25 libopenexr25 ffmpeg libwebpdemux2 libopenjp2-7 libwebpmux3 liblcms2-2 gfortran libopenblas-dev liblapack-dev
 
sudo apt install libgfortran5 libatlas3-base git
</pre>

# Paso 6: Habilitamos la cámara 
Al final de la instalación de todas las dependencias, es importante habilitar la configuración de la cámara con raspi-config. ¡Ojo! Como sabéis, esto implicará usar las librerías de picamera 1.0, en lugar de picamera 2.0 que hemos venido usando en las últimas clases, pero he verificado las fuentes con piwheels y es mucho más seguro utilizar picamera hasta que se estabilice un poco más picamera 2, por lo que habilitamos picamera en raspi-config y reiniciamos la raspberry pi.

<pre>
sudo raspi-config
</pre>

# Paso 7: Instalación de librerías:

Como sabéis, para el proyecto de visión artificial vamos a usar OpenCV. Como os he comentado en clase, piwheels nos ha sido de gran ayuda para identificar qué librerías de python necesitamos que no nos hagan "romperse" las dependencias y "crashear" nuestra instalación, por lo que os dejo por aquí las librerías que debemos instalar:

<pre>
 #actualizamos primero pip:
pip install --upgrade pip
</pre>

Después debemos instala numpy. ¡Ojo! Como os he explicado, SIEMPRE nos vamos a verificar las últimas releases con piwheels, para lo que debemos saber primero nuestra versión de python. Para ello ejecutamos en el terminal lo siguiente:
<pre>
 python
</pre>

Eso nos mostrará lo siguiente:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/46b09278-63a4-40a5-86cd-98563683b9f6)

Por tanto, sabemos que tenemos la versión 3.9.2, con lo cuál vamos a piwheels y buscamos "numpy", lo cuál nos devuelve lo siguiente:

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/2eab4736-05f6-4133-8e49-d6ffac26168a)

Si os fijáis, en la columna de arriba de cada versión diferente de python os pone un nombre (buster, bullseye, etc). Aparte de ser nombres de personajes de Toy Story, son los nombres de las versiones de Debian. En nuestro caso, para comprobar la versión de debian que estamos usando (raspbian es una branch de debian) debemos poner lo siguiente en la línea de comandos:

<pre>
lsb_release -a 
</pre>

Y nos dirá qué versión de debian estamos ejecutando.

Ya sabemos que estamos usando python 3.9.2 y debian bullseye, por lo que en piwheels debemos seleccionar la versión más moderna en este momento (1.26.4). ¡Ojo! No selecciono la opción 2.0 porque esas versiones aún están marcadas como pre-release y me pueden dar problemas. ¡VAMOS A LO SEGURO!

Instalamos numpy:

<pre>
pip3 install -U numpy==1.26.4
</pre>

Constantemente nos va a dar este warning pip: WARNING: The script f2py is installed in '/home/miky/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Podemos ignorarlo, ya que por defecto siempre vamos a usar el mismo usuario (en vuestro caso en lugar de /home/miky pondrá /home/nombre_de_vuestro_usuario). A futuro, cuando montéis todo sobre una dietpi u otra distro SIN X-WINDOWS, debéis considerar si añadir la ruta que os sugiere al PATH de ejecución del sistema. De momento no es necesario.

# Paso 8: Instalación de OpenCV:

Ya hemos comprobado que piwheels es un grandísimo aliado, por lo que nos vamos derechos a comprobar qué necesito para que opencv corra sin problemas en mi bullseye. Buscando opencv-python vemos que nos sugiere los siguientes comandos (Ten en cuenta que, para que no sea taaaan largo, yo ya te he resumido en el paso 5 los apt install que necesitabas, por lo que sólo son necesarios los pip/pip3 install):

![image](https://github.com/villalvilla/WRO-2024-Acervantes-Tips/assets/3918996/a2fb96a0-05d7-448c-b980-632e0d4cf904)

¡Ojo! Aquí nos podemos equivocar pero bien. La última versión compatible sin problemas con bullseye y python 3.9 es la 4.6.0.66, por lo que la instalo en mi sistema:

<pre>
pip3 install opencv-python==4.6.0.66
</pre>

# Paso 9: Instalación de scipy y diversos kits de librerías

Como ya es habitual, buscamos los diversos paquetes que debo instalar previamente con piwheels, por lo que obtendremos el siguiente resultado:

<pre>
pip3 install scipy==1.13.0
pip3 install scikit-learn==1.4.2
pip3 install pyefd==1.5.1
pip3 install scikit-image==0.19.3
pip3 install imutils==0.5.4
</pre>

# Paso 10: Probar los ejemplos de captura de imágenes y videos:

Os recomiendo, antes de clonar todo en una rapsberry pi sin X (entorno de escritorio), que uséis un editor de código visual, que os permita ejecutar código de una manera "amigable", aunque por ssh también lo podréis ejecutar. Yo os recomiendo Thonny, que suele venir instalado en la distro de raspbian.

Os he dejado, para abrir boca, 2 códigos de captura de imágenes en esta misma carpeta donde tenéis el readme. Podéis empezar por "Captura_de_Imagenes.py".

Para ejecutarlo, primero haced un clone de este repositorio y os ubicáis en la carpeta de visión artificial, con los siguientes comandos:
<pre>
git clone https://github.com/villalvilla/WRO-2024-Acervantes-Tips.git
cd WRO-2024-Acervantes-Tips/Visión\ artificial\ con\ Raspberry\ Pi/Captura_imagenes/
</pre>

Recordad que para hacer la captura de las imágenes, tenéis que estar ejecutando código en las X de la Raspberry o mediante VNC con Thonny o terminal directamente:

<pre>
 python3 Captura_de_Imagenes.py
</pre>

Probamos ahora el código de captura secuencial de imágenes:

<pre>
python3 Captura_de_Imagenes_Sucesiva.py
</pre>

# Paso 11: Probar el ejemplo de Robot seguidor de Rostros Horizontal:

En la carpeta Robot_Seguidor_Rostros aquí: https://github.com/villalvilla/WRO-2024-Acervantes-Tips/tree/main/Visi%C3%B3n%20artificial%20con%20Raspberry%20Pi/Robot_Seguidor_Rostros

Os he dejado el guión detallado de cómo proceder con el código de detección de rostros y cómo configurar vuestro Robot para que los motores se muevan según la cámara detecte un rostro o no.
¡CUIDADO! Debéis tener en cuenta que un equipo estáis haciendo la movilidad del robot con servos 360 y el otro lo habéis probado con driver L298N, por lo que deberéis adaptar el código de ejemplo que os dejo a ello.



