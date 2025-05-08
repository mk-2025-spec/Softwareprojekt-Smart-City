def smartcity():
    print("behoben")
    
    
smartcity()

























































import datetime

class Meldung:
    def __init__(self, titel, beschreibung, ersteller):
        self.titel = titel
        self.beschreibung = beschreibung
        self.ersteller = ersteller
        self.datum = datetime.datetime.now()
        self.status = "🟡 Gelesen"
        self.likes = 0

    def set_status(self, neuer_status):
        self.status = neuer_status

    def like(self):
        self.likes += 1

    def anzeigen(self):
        return f"{self.titel} - {self.status}\n{self.beschreibung}\nErstellt von: {self.ersteller} am {self.datum.strftime('%d-%m-%Y %H:%M')}\nLikes: {self.likes}"

# Beispiel für Nutzung
meldung1 = Meldung("Kaputte Straßenlaterne", "Laterne seit 3 Tagen defekt", "Max Mustermann")

# Status ändern
meldung1.set_status("🟠 In Bearbeitung")
meldung1.like()
meldung1.like()

# Anzeigen der Meldung
print(meldung1.anzeigen())


import datetime

class Meldung:
    def __init__(self, titel, beschreibung, ersteller):
        self.titel = titel
        self.beschreibung = beschreibung
        self.ersteller = ersteller
        self.datum = datetime.datetime.now()
        self.status = "🟡 Gelesen"
        self.likes = 0

    def set_status(self, neuer_status):
        self.status = neuer_status

    def like(self):
        self.likes += 1

    def anzeigen(self):
        return f"{self.titel} - {self.status}\n{self.beschreibung}\nErstellt von: {self.ersteller} am {self.datum.strftime('%d-%m-%Y %H:%M')}\nLikes: {self.likes}"

class StadtserviceApp:
    def __init__(self):
        self.meldungen = []

    def neue_meldung(self, titel, beschreibung, ersteller):
        meldung = Meldung(titel, beschreibung, ersteller)
        self.meldungen.append(meldung)

    def zeige_alle_meldungen(self):
        if not self.meldungen:
            print("Keine Meldungen vorhanden.")
        else:
            for meldung in self.meldungen:
                print(meldung.anzeigen())
                print("-" * 40)

# Beispiel für Nutzung
app = StadtserviceApp()
app.neue_meldung("Kaputte Straßenlaterne", "Laterne seit 3 Tagen defekt", "Max Mustermann")
app.neue_meldung("Illegaler Müll", "Müllablagerung an Bushaltestelle", "Erika Musterfrau")

# Status ändern und Likes hinzufügen
app.meldungen[0].set_status("🟠 In Bearbeitung")
app.meldungen[0].like()
app.meldungen[1].set_status("🟢 Behoben")
app.meldungen[1].like()
app.meldungen[1].like()

# Alle Meldungen anzeigen
app.zeige_alle_meldungen()







































