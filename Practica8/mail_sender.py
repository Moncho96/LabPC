import smtplib
import imghdr
import pwinput
from email.message import EmailMessage

EMAIL_ADRESS = input("Ingrese su correo: ")
EMAIL_PASSWORD = pwinput.pwinput("Ingrese su contraseña: ")

msg = EmailMessage()
msg['Subject'] = input("Ingresar Asunto: ")
msg['From'] = EMAIL_ADRESS
msg["To"] = input("Ingresa el correo del destinatario: ")
meme = input("Ingrese la ruta de la imagen que quiere enviar: ")
cuerpo = input("Ingrese el mensaje que quiere enviar: ")
msg.set_content(cuerpo)

with open(meme,'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


