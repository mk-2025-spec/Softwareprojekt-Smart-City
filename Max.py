def Programm():
    # Daten als Liste von Einträgen
    daten = [
        ["Anna Müller", "10.04.3025", "Brücke beschädigt", "Abgeschlossen"],
        ["Peter Schmidt", "21.03.3025", "Straßenlaterne defekt", "Gemeldet"],
        ["Maria Keller", "05.02.3025", "Wasserschaden im Tunnel", "In Bearbeitung"],
        ["Lukas Bauer", "22.06.3025", "Baum blockiert Straße", "Gemeldet"],
        ["Sophie Wagner", "30.07.3025", "Ampel ausgefallen", "In Bearbeitung"],
        ["Maximilian Hoffmann", "12.08.3025", "Schlagloch auf Hauptstraße", "Abgeschlossen"],
        ["Elena Fischer", "05.09.3025", "Ölspur auf Fahrbahn", "Gemeldet"],
        ["JOCHEN MANTERROCHEN", "15.05.3025", "Stein Straße", "in Bearbeitung"]
    ]
    
    # Einträge anzeigen
    for i, eintrag in enumerate(daten, start=1):
        print(f"Burger {i}:", eintrag)
    
    return daten

def filterfunktion(daten):
    suchbegriff = input("Wonach möchtest du suchen? ").lower()
    
    for eintrag in daten:
        if any(suchbegriff in feld.lower() for feld in eintrag):
            print("Gefunden:", eintrag)

# Hauptprogramm
daten = Programm()          # Programm() aufrufen und Rückgabe in 'daten' speichern
filterfunktion(daten)      # daten an die Filterfunktion übergeben











