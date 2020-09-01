import random

from ImageShape import *

if __name__ == '__main__':

    width = input("Inserte el ancho") #Ancho de la imagen
    height = input("Inserte el alto") #Alto de la imagen

    nombre = input("Inserte el nombre de la imagen") #La imagen debe estar en la misma carpeta que el código

    shape = ImageShape(int(width), int(height))
    shape.generateShape()
    shape.showShape()
    shape.getShape()
    shape.whatShape(nombre)