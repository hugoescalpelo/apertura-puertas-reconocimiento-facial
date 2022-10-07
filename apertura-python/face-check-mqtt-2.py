# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd
from paho.mqtt import client as mqtt_client
import random
import time

# Variables y constantes
broker = '127.0.0.1'
port = 1883
topic = "codigoIoT/mqtt/python"
topic2 = "codigoIoT/mqtt/index"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, mensaje):
    #while True:
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print (result)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

### Inicio del programa
# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/aigeneratedface2.jpg", db_path = "/home/hugo/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
json_view = df.to_json(orient="index")
print ("La expresion en JSON de los resultados es: ")
print (json_view)


# Envio
client = connect_mqtt()
client.loop_start()
publish(client, json_view)