#import
import smtplib
import json
from email.message import EmailMessage

#configuration du fichier json
json_file = open("config.json")
gmail_conf = json.load(json_file)

# verifions si le fichier a ete bien load
print(gmail_conf)

# message a envoyer
msg = EmailMessage()
msg["from"]=gmail_conf["email"],
msg["subject"]= "Envoie message automatique avec python"
msg.set_content("Salut je viens de vous envoyer un mail automatique grace a un script python")

# connecter mon compte mail
for destinataire in gmail_conf["listMail"]:
    msg["to"]=destinataire

    with smtplib.SMTP_SSL(gmail_conf["server"],gmail_conf["port"]) as smtp:
        smtp.login(gmail_conf["email"],gmail_conf["pwd"])
        smtp.send_message(msg)
        # verification si l'opération a ete reussi
        print("Email envoyé avec success", destinataire)