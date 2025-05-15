def Programm():
    Autor = "JOCHEN MANTERROCHEN"
    Datum = "15.05.3025"
    Problem = "Stein Straße"
    Status = "in Bearbeitung"
    
    burger = [Autor, Datum,Problem, Status]
    print(str(burger))
    
    eingabe = input("Gib eine neue Information ein: ") 
    burger.append(eingabe)  
    
    print("Aktualisierte Daten:", burger)

Programm()

        


        








