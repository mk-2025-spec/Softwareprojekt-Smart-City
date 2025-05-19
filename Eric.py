problem1 = "BANK KAPUTT"
problem2 = "STRAENßENLATERNE DEFEKT"
problem3 = "MÜLL NICHT ABGEHOLT"

def main():
    bewertung1 = 0
    bewertung2 = 0
    bewertung3 = 0
    
    print("Gebe 'up' ein wenn du den Vorschlag gut findest.")
    print("Gebe 'down ein wenn du den Vorschlag nicht gut findest.")
    print("Gebe 'exit' ein wenn du das Programm beenden willst.")
    
    while True:
        print("Problem: ", problem1)
        eingabe = input("Wie Findest du das Problem? ")
        if eingabe == "up":
            bewertung1 = bewertung1 + 1
            print("Like Vergeben: ",bewertung1)
        elif eingabe == "down":
            bewertung1 = bewertung1 - 1
            print("Dislike vergeben (-1): ",bewertung1)
        elif eingabe == "exit":
            print("Nächstes Problem")
            break
        else:
            print("Fehler: Bitte nur 'up', 'down' oder 'exit' ein.")
        
        if bewertung1 >= 5:
            print("Diese Anzeige wurde soeben an den staat gesendet")
            
        print("===ERGEBNISS===")
        print(problem1, "-->", bewertung1)
        
        
        
    while True:
        print("Problem: ", problem2)
        eingabe = input("Wie Findest du das Problem? ")
        if eingabe == "up":
            bewertung2 = bewertung2 + 1
            print("Like Vergeben: ",bewertung2)
        elif eingabe == "down":
            bewertung2 = bewertung2 - 1
            print("Dislike vergeben (-1): ",bewertung2)
        elif eingabe == "exit":
            print("Nächstes Problem")
            break
        else:
            print("Fehler: Bitte nur 'up', 'down' oder 'exit' ein.")
        
        if bewertung2 >= 5:
            print("Diese Anzeige wurde soeben an den staat gesendet")
            
        print("===ERGEBNISS===")
        print(problem2, "-->", bewertung2)
        
        
        
    while True:
        print("Problem: ", problem3)
        eingabe = input("Wie Findest du das Problem? ")
        if eingabe == "up":
            bewertung3 = bewertung3 + 1
            print("Like Vergeben: ",bewertung3)
        elif eingabe == "down":
            bewertung3 = bewertung3 - 1
            print("Dislike vergeben (-1): ",bewertung3)
        elif eingabe == "exit":
            print("Nächstes Problem")
            break
        else:
            print("Fehler: Bitte nur 'up', 'down' oder 'exit' ein.")
        
        if bewertung3 >= 5:
            print("Diese Anzeige wurde soeben an den staat gesendet")
            
        print("===ERGEBNISS===")
        print(problem3, "-->", bewertung3)
        
        print("Es gibt keine weiteren Probleme")
    print("Es gibt keine weiteren Probleme")
main()
