def Programm():
    Autor = "Max Mustermann"
    Datum = "15.05.2025"
    Problem = "Stein Straße"
    Status = "in Bearbeitung"
    
    burger = [Autor, Datum,Problem, Status]
    print(str(burger))
    
    eingabe = input("Gib eine neue Information ein: ")  # Speichert die Eingabe des Nutzers
    burger.append(eingabe)  # Fügt die Eingabe zur Liste hinzu
    
    print("Aktualisierte Daten:", burger)

Programm()

        


        








