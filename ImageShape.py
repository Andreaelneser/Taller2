import cv2
import numpy as np
import random
from PIL import Image

numero = random.randint(0, 4) #generación del número random

class ImageShape:
    def __init__(self, width, height):

        self.width = width

        self.height = height

    def generateShape(self):

        self.shape = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        ancho_m = self.width/2 #Mitad del ancho
        alto_m = self.height/2 #Mitad del alto
        ancho_mm = self.width/4 #Mitad de la mitad del ancho
        alto_mm = self.height/4 #Mitad de la mitad del alto
        minimo = min(self.height, self.width)/2

        if numero == 0:  #triángulo
            print('La figura es un triángulo')
            t1 = (int(ancho_m), int(alto_m - int((np.sqrt(3)/2)*int(minimo/2)))) #punto 1 triángulo
            t2 = (int(ancho_m) - int(ancho_mm), int(alto_m + ((np.sqrt(3)/2)*int(minimo/2)))) #punto 2 triángulo
            t3 = (int(ancho_m) + int(ancho_mm), int(alto_m + ((np.sqrt(3)/2)*int(minimo/2)))) #punto 3 triángulo
            puntos = np.array([t1,t2,t3])
            self.shape = cv2.drawContours(self.shape, [puntos], 0, (255, 255, 0),cv2.FILLED) #creación del triángulo con los puntos dados
            cv2.imshow("Triángulo", self.shape) #mostrar imagen
            cv2.waitKey(0)

        elif numero == 1: #cuadrado
            print('La figura es un cuadrado')
            c1 = (int(ancho_m) - int(int(minimo)/2), int(alto_m) - int(int(minimo)/2))
            c2 = (int(ancho_m) + int(int(minimo)/2), int(alto_m) + int(int(minimo)/2))
            cv2.rectangle(self.shape, c1, c2, (255, 255, 0), cv2.FILLED) #creación del cuadrado con los puntos dados
            c_rot = cv2.getRotationMatrix2D((int(ancho_m), int(alto_m)), 45, 1.0)  #rotación
            self.shape = cv2.warpAffine(self.shape, c_rot, (self.width, self.height))
            cv2.imshow('Cuadrado', self.shape)  # Mostrar imagen
            cv2.waitKey(0)  # Dejar la imagen en pantalla hasta que se presione cualquier cosa

        elif numero == 2: #rectángulo
            print('La figura es un rectángulo')
            r1 = (int(ancho_m) - int(ancho_mm), int(alto_m) - int(alto_mm))
            r2 = (int(ancho_m) + int(ancho_mm), int(alto_m) + int(alto_mm))
            cv2.rectangle(self.shape, r1, r2,(255,255,0), cv2.FILLED) #creación del rectángulo con los puntos dados
            cv2.imshow('Rectángulo', self.shape)  # Mostrar imagen
            cv2.waitKey(0)  # Dejar la imagen en pantalla hasta que se presione cualquier cosa

        else: #circulo
            print('La figura es un circulo')
            circulo = cv2.circle(self.shape, (int(self.width/2), int(self.height/2)), int(min(self.height, self.width)/2), [255, 255, 0], -1) #imagen, centro, radio,color, relleno
            cv2.imshow('Circulo', circulo)  # Mostrar circulo generado
            cv2.waitKey(0)  # Dejar la imagen en pantalla hasta que se presione cualquier cosa

    def showShape(self):

        im = Image.fromarray(self.shape)
        cor = x,y = self.width/2, self.height/2 #coordenadas del pixel
        dato_pixel = im.getpixel(cor) #obtención del pixel

        print(dato_pixel)

        if dato_pixel ==  "[0, 0, 0]": #Si el pixel es negro
                   black = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                   cv2.imshow('Figura', black)  # Mostrar imagen en negro
        else: #si no es negro
                    cv2.imshow('Figura', self.shape)  # Mostrar imagen 
                    cv2.waitKey(5000)  # Dejar la imagen en pantalla  5 segundos


    def getShape(self):

        #Condicionales para obtener el nombre de la figura
        if numero == 0:
             nom_fig = "Triangle"
             print(nom_fig)

        elif numero == 1:
            nom_fig = "Square"
            print(nom_fig)

        elif numero == 2:
            nom_fig = "Rectangle"
            print(nom_fig)

        else:
            nom_fig = "Circle"
            print(nom_fig)


        return nom_fig, self.shape

    def whatShape(self, nombre):

        nfig = '0' #inicialización variable nfig (que contiene el nombre de la figura detectada)
        fig = cv2.imread(nombre)
        imgGrey = cv2.cvtColor(fig, cv2.COLOR_BGR2GRAY) #se pasa la imagen a grises
        _, thrash = cv2.threshold(imgGrey, 100, 200, cv2.THRESH_BINARY) #umbralización
        contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #contornos

        cv2.imshow("img", imgGrey)
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            cv2.drawContours(fig, [approx], 0, (0, 0, 0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            if len(approx) == 3:
                cv2.putText(fig, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
                nfig = "Triangle"
                print(nfig)
            elif len(approx) == 4:
                x1, y1, w, h = cv2.boundingRect(approx)
                aspectRatio = float(w) / h
                if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                    cv2.putText(fig, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
                    nfig = "Square"
                    print(nfig)
                else:
                    cv2.putText(fig, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
                    nfig = "Rectangle"
                    print(nfig)
            else:
                cv2.putText(fig, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 255, 255))
                nfig = "Circle"
                print(nfig)

        cv2.imshow("shapes", fig)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return nfig
