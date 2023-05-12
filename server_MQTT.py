import paho.mqtt.client as mqtt #import the client1
import time

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    
ip_dir = str(input("Por favor, deme la dirección IP de su servidor: "))

print("="*7, "Inicializando Cliente", "="*7)
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("="*7, "Conectando al Servidor", "="*7)
client.connect(ip_dir) #connect to broker
client.loop_start() #start the loop
topic = str(input("Digame el nombre del topico que quiere usar: "))
print("Suscribiendose al topico:",topic)
client.subscribe(topic)

option = 1
print("#"*10, "Iniciando Chat", "#"*10)

while option == 1: 
    msj = str(input("Digame que mensaje quiere enviar: "))
    print("Publicando mensaje en el topico:",topic)
    client.publish(topic,msj)
    time.sleep(1)
    option = int(input("¿Quiere seguir chateando? [1 = Si; 2 = No] \n > "))

print("#"*10, "Terminando Chat", "#"*10)
client.loop_stop()

