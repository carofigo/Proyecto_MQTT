import paho.mqtt.client as mqtt #import the client1
import time

def on_message(     # función que despliega la información del mensaje y del topico
    client, userdata, 
    message):
    time.sleep(1)
    print("\n", "+"*10, "Nuevo mensaje", "+"*10, "\n")
    print("Mensaje recibido:" ,str(message.payload.decode("utf-8")))
    print("Tópico del mensaje recibido:",message.topic)
    print("\n", "+"*35, "\n")
    
ip_dir = str(input("Por favor, deme la dirección IP de su servidor: "))

print("="*7, "Inicializando Cliente", "="*7)
client = mqtt.Client("P1") # creo una nueva instancia de cliente
client.on_message=on_message # aplico la función a la llamada del metodo del mensaje
print("="*7, "Conectando al Servidor", "="*7)
client.connect(ip_dir) # hago la conexión con el servidor
client.loop_start() # inicio el ciclo se la subscripción
topic = str(input("Dígame el nombre del tópico que quiere usar: "))
print("Suscribiendose al tópico:",topic)
client.subscribe(topic) # hago la subscripción al topico introducido

option = 1
print("\n", "#"*10, "Chat Iniciado", "#"*10, "\n")

while option == 1: 
    msj = str(input("Dígame que mensaje quiere enviar: "))
    print("Publicando mensaje en el tópico:",topic)
    client.publish(topic,msj) # publico el mensaje en el topico introducido
    time.sleep(2)
    option = int(input("\n ¿Quiere seguir chateando? [1 = Si | 2 = No] \n > "))

print("\n", "#"*10, "Chat Terminado", "#"*10, "\n")
client.loop_stop() # paro el ciclo de subscripción

