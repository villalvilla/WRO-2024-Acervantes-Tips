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

# Paso 4: Instalación de dependencias del sistema:

Como vamos a utilizar python3 y en concreto pip installer para la mayoría de recursos, os recomiendo que uséis esta herramienta online siempre que necesitéis revisar los recursos de python y los requisitos de dependencias de los paquetes que queráis utilizar. Viene EXCELENTE saber en todo momento qué necesitamos para tener montada determinada utilidad en python o librería: [piwheels - Package List](https://www.piwheels.org/packages.html)

Dependencias para instalar:
<pre>
#comandos para verificar actualizaciones
sudo apt update
sudo apt upgrade
 
#comandos para instalar las dependencias necesarias
sudo apt-get install libhdf5-dev 
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqt5gui5 
sudo apt-get install libqt5webkit5 
sudo apt-get install libqt5test5
sudo apt-get install libilmbase-dev
sudo apt-get install libopenexr-dev
sudo apt-get install libgstreamer1.0-dev
sudo apt-get install libavcodec-dev
sudo apt-get install libavformat-dev
sudo apt-get install libswscale-dev
sudo apt-get install libwebp-dev
sudo apt install libxcb-shm0 
sudo apt install libcdio-paranoia-dev 
sudo apt install libsdl2-2.0-0 
sudo apt install libxv1 
sudo apt install libtheora0 
sudo apt install libva-drm2 
sudo apt install libva-x11-2 
sudo apt install libvdpau1 
sudo apt install libharfbuzz0b 
sudo apt install libbluray2 
sudo apt install libhdf5-103 
sudo apt install libgtk-3-0 
sudo apt install libdc1394-25
sudo apt install libopenexr25
sudo apt install ffmpeg
sudo apt install libwebpdemux2 libopenjp2-7 libwebpmux3 liblcms2-2
sudo apt-get install gfortran libopenblas-dev liblapack-dev -y
sudo apt install libgfortran5 libatlas3-base
</pre>

# Paso 5: Habilitamos la cámara 
#comando para entrar a la configuración y habilitar cámara
sudo raspi-config




