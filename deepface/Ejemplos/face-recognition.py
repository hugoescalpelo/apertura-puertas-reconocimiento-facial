# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/aigeneratedface2.jpg", db_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Imagen de mayor similitud")
print (df.identity[0])
print ("Imagen de similitud secundara")
print (df.identity[1])