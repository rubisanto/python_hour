import pytz
from datetime import datetime

# Demandez à l'utilisateur de saisir le nom du pays ou du fuseau horaire
pays_ou_fuseau = input("Saisissez le nom du pays ou du fuseau horaire : ")

try:
    # Recherchez le fuseau horaire correspondant au pays ou au fuseau horaire saisi
    tz = pytz.timezone(pays_ou_fuseau)

    # Obtenez l'heure actuelle dans le fuseau horaire spécifié
    heure_actuelle = datetime.now(tz)

    # Affichez l'heure actuelle
    print(
        f"L'heure actuelle dans {pays_ou_fuseau} est : {heure_actuelle.strftime('%Y-%m-%d %H:%M:%S')}")

except pytz.UnknownTimeZoneError:
    print("Fuseau horaire inconnu. Assurez-vous de saisir un nom de pays ou un fuseau horaire valide.")
