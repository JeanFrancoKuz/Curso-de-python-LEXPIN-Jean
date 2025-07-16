import pywhatkit as ws

"""Se envia el mensaje a un solo numero de manera immediata"""

#ws.sendwhatmsg_instantly("+584242653244", "Mensaje de prueba desde el visual studio",15)

"""
Enviar mensajes a los grupos de manera immediata se necesita el ID del grupo o el link de compartida
"""


#ws.sendwhatmsg_to_group_instantly("G0yGFH508uzBMv6Y3irJX3","a Frahiner le mide como a un gorila",10)
#ws.sendwhatmsg_to_group_instantly("GjtWD6Qc9Td1KJTJZnz7MZ","Mensaje de prueba, que cool que el mensaje se escriba y lo pueda ver",15)

#ws.sendwhatmsg_to_group("GjtWD6Qc9Td1KJTJZnz7MZ","Hola estamos practicando envio aumatico de mensajes dependiendo la hora pd:JFK",21,9)

"""Enviar imagenes"""
ws.sendwhats_image("+584123971034","./Python/Teoria_Parte2/Mensajes_WHATSAPP/cinemark.png","Imagen enviada de prueba")


"CICLOS PARA ENVIAR A DIFERENTES NUMEROS"

"""
number_list = ["+584123971034", "+584123971034", "+584123971034", "+584123971034",]

for number in number_list:
  ws.sendwhatmsg_instantly(number,"Mensaje de prueba en un bucle")
  
#menu interactivo de envio de mensajes e imagenes

def sendMsg():
  number = input("Ingresa tu numero telefonico, en formato internacional")
  msg = input("Ingresa el mensaje que quieres enviar")
  ws.sendwhatmsg_instantly(number,msg)
  
#crear metodo para enviar, mensaje a grupo, imagen a persona, imagen a grupo, y enviar mensaje agendado
"""


