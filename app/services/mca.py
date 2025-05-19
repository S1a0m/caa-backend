# matricule change alert

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_confirmation_email(to_email: str, confirmation_url: str, receiver_name: str, receiver_surname: str, vehicle_plate_number: str):
    from_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    subject = "Demande de modification de plaque"
    body = f"""
    <html>
        <body>
            <p>Vous, {receiver_name} {receiver_surname} avez demandé la modification de la plaque d'immatriculation de votre véhicule.</p>
            <p><strong>Immatriculation du véhicule: </strong>{vehicle_plate_number}</p>
            <p><strong>Localisation du véhicule: </strong><!-- se servir d'api JS GPS pour la position du véhicule --></p>
            <p>Est-ce vous ?</p>
            <a href="{confirmation_url}" 
               style="padding:10px 20px; background-color:#4CAF50; color:white; text-decoration:none; border-radius:5px;">
                Confirmer la demande.
            </a>
            <p>Si ce n'est pas vous, vous pouver
                <a href="tel: +22901118" 
                style="padding:10px 20px; background-color:#4CAF50; color:white; text-decoration:none; border-radius:5px;">
                    appeller la police 
                </a>
                pour porter plainte.
            </p>
        </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print("Erreur lors de l’envoi de l’email :", str(e))
        raise
