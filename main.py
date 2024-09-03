# Exemple de script pour envoyer une newsletter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def envoyer_newsletter(liste_destinataires, sujet, corps_html):
    """ Fonction qui permet d'automatiser l'envoi du message 
    Arguments:
    liste_destinataires(liste des destinataire)
    sujet(str): l'objet du message
    coprs_html(str): le coprs du message 
    """
    email_expéditeur = "sabre22@live.fr"
    mot_de_passe = "-@4>>(b9)@o;^=DKN9s+?DNz%)Kdh_"
    serveur_smtp = "smtp.office365.com" # pour gmail: "smtp.gmail.com"
    port_smtp = 587 # STARTTLS est une commande qui permet de sécuriser une connexion SMTP en passant d'une connexion non chiffrée à une connexion chiffrée (TLS/SSL) en cours de route.

    for destinataire in liste_abonnes:
        # On cree un instance de la classe MIMEMultipart
        message = MIMEMultipart()
        message['From'] = email_expéditeur
        message['To'] = destinataire
        message['Subject'] = sujet
        # L'instancition de la Classe MIMEText avec comme premier parametre le corp et comme deuxieme parametre son type 
        # Ca peut etre de type html cest a dire des bloc de code html ou plain qui veut dire du text brute
        message.attach(MIMEText(corps_html, 'html'))

        try:
            # On prepare l'envoi 
            serveur = smtplib.SMTP(serveur_smtp, port_smtp)
            # On securise 
            serveur.starttls()
            # On s'authentifie
            serveur.login(email_expéditeur, mot_de_passe)
            # On envoi le message 
            serveur.send_message(message)
            # On quitte
            serveur.quit()
            print(f"Newsletter envoyée à {destinataire}")
        except Exception as e:
            print(f"Erreur lors de l'envoi à {destinataire}: {e}")


# Liste d'abonnés et contenu de la newsletter
liste_abonnes = ["arab.fechetah@outlook.fr", "amazigh51@outlook.fr"]
sujet = "Newsletter du mois"
corps_html = "<html><body><h1>Bienvenue dans notre newsletter!</h1><p>Voici les dernières nouvelles...</p></body></html>"

envoyer_newsletter(liste_abonnes, sujet, corps_html)