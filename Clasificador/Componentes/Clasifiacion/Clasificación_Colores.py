### Se importan las librerias a utilizar
import cv2
import numpy as np
import time

# Definimos el puerto de la cámara a emplear  
cap = cv2.VideoCapture(0)

## Define la forma de la figura a detectar
prevCircle = None
dist = lambda x1,y1,x2,y2: (x1-x2)**2 + (y1-y2)**2 

##Tipo de letra 
font = cv2.FONT_HERSHEY_SIMPLEX

## Función para dibujar los contornos y clasificar según el color 
def draw(mask, color):
    ##Función para encontrar contornos
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ##Se establece un condicional para determinar un area más limitada
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 10000:
            ## Coordenadas     
            M = cv2.moments(c)
            if (M["m00"] == 0):
                M["m00"] = 1
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
            ##Suavizar los contornos
            newContorno = cv2.convexHull(c) 
            ##Texto en la imagen                   
            cv2.putText(frame, '{}, {}'.format(x, y), (x+10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
            ###Dibujar Contornos
            cv2.drawContours(frame, [newContorno], 0, color, 3)
            ##Condicional para imprimir según la clasificacion
            if color == (255,0,0):
                data = "Azul"
            elif color == (0,0,255):
                data = "Rojo"
            elif color == (0,255,0):
                data = "Verde"
            elif color == (255,0,255) or color == (255,255,0):
                data = "Basura"
            print(data)

### Rangos HSV de colores a detectar
azulBajo = np.array([100, 100, 20], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)

verdeBajo = np.array([45,100,20], np.uint8)
verdeAlto = np.array([70,255,255], np.uint8)

rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([5, 255, 255], np.uint8)

rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([179, 255, 255], np.uint8)

amarilloBajo = np.array([15, 100, 20], np.uint8)
amarilloAlto = np.array([45, 255, 255], np.uint8)

moradoBajo = np.array([15, 100, 20], np.uint8)
moradoAlto = np.array([45, 255, 255], np.uint8)

while True:
    #time.sleep(1)

    data0 = 0
    ### Obtenemos un valor booleano e imagen
    ret, frame = cap.read()
    if not ret: break

    ##Convierte la imagen a diferentes formatos 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurFrame = cv2.GaussianBlur(grayFrame, (17,17), 0)

    ##Función de circulo
    circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1],prevCircle[0],prevCircle[1]):
                    chosen = i
                    data0 = "Circulo"
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0,100,100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255), 3)
        prevCircle = chosen

    print(data0)

    #if ret == True:
    if data0 == "Circulo":

        # Pasamos de BGR a HSV
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #### Buscar HSV establecidos anteriormente en la imagen capturada
        maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
        maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)
        maskamarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
        maskmorado = cv2.inRange(frameHSV, moradoBajo, moradoAlto)
        maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
        maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
        maskRojo = cv2.add(maskRojo1, maskRojo2)

        ##Dibuja los contornos con sus respectivos colores
        draw(maskAzul, (255, 0, 0))
        draw(maskRojo, (0, 0, 255))
        draw(maskVerde, (0, 255, 0))
        draw(maskamarillo, (255,255,0))
        draw(maskmorado,(255,0,255))

    ##Mostramos la ventana de captura        
    cv2.imshow('Captura de video', frame)

    ##Detenemos la visualización con la tecla 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

#Detenemos la captura de video
cap.release()
#Cerramos todas las ventanas
cv2.destroyAllWindows()