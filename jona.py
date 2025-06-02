nutzer_liste = []

def registrierung():
    while True:
        email = input("E-Mail-Adresse: ")
        if any(nutzer["email"] == email for nutzer in nutzer_liste):
            print("E-Mail bereits registriert! Bitte versuche eine andere.")
        else:
            password = input("Passwort: ")
            adresse = input("Adresse: ")
            nutzer_liste.append({"email": email, "password": password, "adresse": adresse})
            print("Registrierung erfolgreich!\n")
            break

def login():
    angemeldet = False
    while not angemeldet:
        email = input("E-Mail-Adresse: ")
        password = input("Passwort: ")
        for nutzer in nutzer_liste:
            if nutzer["email"] == email and nutzer["password"] == password:
                print("Login erfolgreich!\n")
                angemeldet = True
                email_global = email
                adresse_global = nutzer["adresse"]
                break
        if not angemeldet:
            print("Fehlerhafte Login-Daten. Bitte versuche es erneut.\n")

registrierung()
login()

while True:
    wahl = input("Möchtest du 1) ein Problem melden oder 2) einen Vorschlag machen? ('q' zum Beenden): ")

    if wahl == "1":
        print("Problem gemeldet:", input("Beschreibe dein Problem: "))
    elif wahl == "2":
        print("Vorschlag gemeldet:", input("Beschreibe deinen Vorschlag: "))
    elif wahl.lower() == "q":
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Eingabe.")
gglkkjkljkl
