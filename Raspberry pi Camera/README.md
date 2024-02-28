# Configuración de la Camara en Raspberry Pi para trabajar con Vision Artificial

## 1.- Desplegar la herramienta de configuración

Para poder acceder a la herramienta de configuración basta con ejecutar el siguiente comando en la terminal:
<pre>
sudo raspi-config
</pre>

## 2.- Seleccionamos Interface Options
<pre>
raspi-config –> Interface options
</pre>

## 3.- Seleccionamos I1 Legacy Camera

<pre>
  raspi-config –> Interface options –> I1 Legacy Camera
</pre>

## 4.- Reiniciamos el sistema de la Raspberry Pi
Para que los cambios a la configuración tengan efecto aceptamos reiniciar el sistema seleccionando <Yes>. Una vez el sistema reinicie podremos controlar la cámara desde nuestra Raspberry Pi.

