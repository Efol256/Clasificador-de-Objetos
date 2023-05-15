# Clasificador_de_Objetos
Este repositorio contienen todo el material involucrado en el desarrollo y la implementación del prototipo de clasificador de objetos por forma y color, utilizando procesamiento de imágenes, una placa de desarrollo raspberry pi pico, usando como actuadores servomotores y escrito en micro python.

## En qué consiste?
El clasificador de objetos consiste en un dispositivo capaz de diferenciar entre objetos y los colores de estos en tiempo real. Específicamente está diseñado para separar figuras esféricas en cuatro compartimientos según tres colores; rojo, verde o azul, en caso que no se cumplan las condiciones de forma o color, el objeto es depositado en un compartimiento aparte.

## Cómo funciona?
Este dispositvo utiliza como herramientas deep learning: modelo de aprendizaje automático entrenado en un conjunto de datos etiquetados previamente capaz de distinguir entre formas y colores. El modelo ha sido desarrollado en el lenguaje python.

Se utiliza una cámara para establecer las caracterísitcas del objeto en timepo real, las imágenes son procesadas por un dispositvo externo utilizando un algoritmo especializado dado a las limitaciones de la placa de desarrollo (raspberry pi pico); por lo tanto la información una vez procesada es enviada a través de comución serial al controlador. Cabe destacar que el sistema cuenta con un sensor de proximidad con la finalidad de corroborar la presencia del objeto y evitar el envío constante de información sin peso hacia el controlador, esto permite el ahorro de recursos.

La función del controlador, para este caso, una raspberry pi pico, es la de interpretar la información transmitida a través de puertos  seriales desde el dispositivo externo para indicarle al resto del sistema su función. Para ser más específicos, esta se encarga de contabilizar la cantidad de objetos que han sido clasificados, en qué compartimiento se depositaron, el tiempo en que fueron clasificados, cómo deben posicionarse los servos para que el objeto se deposite en el lugar correcto, mostrar en una pantalla lcd el color del objeto clasificado y encender un led con el color indicado; esta información se preserva en un archivo .txt para ser analizada en cuyo caso se necesite. 

## Requisitos
Para utilizar el clasificador necesitarás: Python 3, las siguientes librerías y materiales:

### Librerías
Estas se instalan a través del comando pip. Asegúrese de que el programa Python se encuente incluido en el path y que esta herramienta esté instalada en su sistema.

- 
- 
- OpenCV (https://opencv.org/releases/)
- 

### Materiales
- Una placa de desarrollo Raspberry Pi Pico
- Un cable USB para conectar la placa a tu computadora
- Servomotores
- Sensor de proximidad 
- Una pantalla LCD 
- LEDs de colorers: rojo, verde y  azul
- Resistencias y protoboard
- Objetos de colores 
- Una cámara 

## Cómo utilizar?
Para utilizar el clasificador, sigue estos pasos:

1. Clona este repositorio en tu computadora.
2. Conecta la placa de desarrollo Raspberry Pi Pico a tu computadora utilizando el cable USB.
3. Conecta los servomotores, el sensor de proximidad, la pantalla LCD y los LEDs a la placa de desarrollo siguiendo el esquema de            conexiones provisto.
4. Carga el archivo main.py en la placa de desarrollo.
5. Ejecuta el código en tu computadora para procesar las imágenes y enviar la información al dispositivo externo (Raspberry Pi Pico).
6. Ubica objetos dentro del rango de visión de la cámara para que el sistema pueda ir clasificando.
7. Observa cómo el sistema va clasificando de manera autónoma.

Espera a que el clasificador de objetos procese los objetos y los clasifique en los compartimientos correspondientes.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. Si deseas contribuir, cree un fork del repositorio y envíe un pull request con sus cambios.
