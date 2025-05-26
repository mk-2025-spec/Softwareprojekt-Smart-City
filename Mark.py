# Liste für alle Meldungen
meldungen = []

# Funktion: Bürger meldet ein Problem 
def problem_melden():
    beschreibung = input(" Was ist ihr Anliegen(Problem oder Vorschlag)?")

  #Prüfen, ob das Problem schon gemeldet wurde
    for i in meldung:
        if beschreibung == "beschreibung":
            print("Ihr Anliegen wurde bereits gemeldet")
            print(">>", i ["beschreibung"])
            return

    neue_meldung = {
      "beschreibung" : beschreibung,
      "thema":"",
      "Wichtigkeit/Relevanz" : ""
    }

    meldung.append(neue_meldung)
    print( "Ihre Meldung ist gespeichert")

