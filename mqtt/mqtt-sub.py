# Bibliotecas
#import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import random

# Datos del broker
broker = '3.122.69.139'
port = 1883
topic = "codigoIoT/mqtt/python"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

# Conexion al broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Suscripción
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

# Opcion A
client = connect_mqtt()
subscribe(client)
client.loop_forever()

# # Opcion B
# def run():
#     client = connect_mqtt()
#     subscribe(client)
#     client.loop_forever()

# if __name__ == '__main__':
#     run()

# # Opcion C
# if __name__ == '__main__':
#     client = connect_mqtt()
#     subscribe(client)
#     client.loop_forever()