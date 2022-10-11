# Bibliotecas
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("img_src", help="Imagen a buscar en la DB del caras")
parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

ruta = args.img_src + " " + args.db_path

print ("Las rutas recibidas son: " + ruta)

###### Programa Basico #####
# # Bibliotecas
# import argparse

# # Programa
# parser = argparse.ArgumentParser()
# parser.parse_args()

##### Programa con un argumento posicional
# # Bibliotecas
# import argparse

# # Configuracion de ArgParse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()

# #Prorgama
# print(args.echo)

