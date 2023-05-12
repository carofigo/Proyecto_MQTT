# Proyecto_MQTT

by Andrea Carolina Figueroa Orihuela, Diego Sahid García Galván and Marco Miloslavich Airola

## A final project for the "Computational tools: the art of programming" course at ITESM

We were asked to build a program capable of connecting to a server with an open AWS IP using the "Mosquitto" message broker.

Our code is able to connect to the AWS server, ask the topic to which you want to send the message and subscribe, to later request the message and print it on the screen. Finally, a selector is displayed to the user to continue chatting or leave the chat and end the program.

For this project, we used AWS to host the server that would be the intermediary between the sender and the receiver, as well as Amazon Linux 2 as the embedded operating system. We installed the "Mosquitto" message broker and to create the user interface from the terminal, we used the paho.mqtt.client Python package, as well as the Python time module to give a more leisurely experience.

After importing the necessary modules, we create the "on_message" function that receives the message written by the sender, this function will display both the message and the topic in which it was published. Consequently, we ask the user for the IP address of the server and initialize a client. Subsequently, we assign the message reading protocol the function that we defined at the beginning, we connect to the server with the received IP and we subscribe to the topic. Finally, we request the message from the user and we publish it in the selected topic, finally, we ask the user if he wants to continue chatting or end the conversation.