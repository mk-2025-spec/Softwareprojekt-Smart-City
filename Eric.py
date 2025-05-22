autoren = ["Anna Müller", "Peter Schmidt", "Maria Keller", "Lukas Bauer", "Sophie Wagner",
           "Maximilian Hoffmann", "Elena Fischer", "Jochen MANTTEROCHEN"]
daten = ["10.04.3025", "21.03.3025", "05.02.3025", "22.06.3025", "30.07.3025",
         "12.08.3025", "05.09.3025", "15.05.3025"]
problem = ["Brücke beschädigt", "Straßenlaterne defekt", "Wasserschaden im Tunnel",
            "Baum blockiert Straße", "Ampel ausgefallen", "Schlagloch auf Hauptstraße",
            "Ölspur auf Fahrbahn", "Stein Straße"]
status = ["Abgeschlossen", "Gemeldet", "In Bearbeitung", "Gemeldet",
          "In Bearbeitung", "Abgeschlossen", "Gemeldet", "In Bearbeitung"]
#^ Diese Variablen stehen für die jeweiligen Probleme welche Bürger gemeldet haben 
bewertung = [0] * len(problem)

def main():
    for i in range (len(problem)):
        print("===PROBLEM", i + 1, "===")
        print("Autor:", autoren[i])
        print("Datum:", daten[i])
        print("Problem:", problem[i])
        print("Status:", status[i])

#^ Das sind die Bewertungsspeicher der einzelnen Probleme   
        print("Gebe 'up' ein wenn du den Vorschlag gut findest.")
        print("Gebe 'down ein wenn du den Vorschlag nicht gut findest.")
        print("Gebe 'exit' ein wenn du das nächste Problem sehen willst.")
#^ Hier werden alle möglichen Eingaben vorgestellt    
        while True:
            eingabe = input("Wie Findest du das Problem? ")
            if eingabe == "up":
                bewertung[i] = bewertung[i] + 1
                print("Like Vergeben: ",bewertung[i])
            elif eingabe == "down":
                bewertung[i] = bewertung[i] - 1
                print("Dislike vergeben (-1): ",bewertung[i])
            elif eingabe == "exit":
                print("Nächstes Problem")
                break
            else:
                print("Fehler: Bitte nur 'up', 'down' oder 'exit' ein.")
        
            if bewertung[i] >= 5:
                print("Diese Anzeige wurde soeben an den staat gesendet")
                
                print("===ERGEBNISS===")
                print(problem[i], "--->", bewertung[i])
#^ So habe ich mir ein Like-System gebaut mit der hilfe eines Zählers für die jeweiligen Probleme         
#^ "up" für + 1Like "down" für - 1Like "exit" für nächstes Problem    
#^ Am ende habe ich noch eine Fehlermeldung bei Fehlerhaftereingabe programmiert und einen Print Befehl der das Ergebniss zusammenfasst

main()
