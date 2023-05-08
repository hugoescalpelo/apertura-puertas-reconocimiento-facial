from deepface import DeepFace

obj = DeepFace.analyze (img_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/aigeneratedface1.jpg", actions = ['age', 'gender', 'race', 'emotion'])


print ("El resultado del analisis es: ")
print (obj)
