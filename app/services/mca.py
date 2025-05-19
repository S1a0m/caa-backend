# matricule change alert

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_confirmation_email(to_email: str, confirmation_url: str):
    from_email = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    subject = "Demande de modification de plaque"
    body = f"""
    <html>
        <body>
            <p>Vous avez demandé la modification de la plaque d'immatriculation de votre véhicule.</p>
            <p>Est-ce vous ?</p>
            <a href="{confirmation_url}" 
               style="padding:10px 20px; background-color:#4CAF50; color:white; text-decoration:none; border-radius:5px;">
                Confirmer la demande
            </a>
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
