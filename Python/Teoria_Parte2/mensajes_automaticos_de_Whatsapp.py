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
ws.sendwhats_image("GjtWD6Qc9Td1KJTJZnz7MZ","./Teoria_Parte2/cinemark.png","Imagen enviada de prueba")
