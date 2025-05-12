
print("Was möchtest du dem Chat melden?")
print("1: Ein Problem melden")
print("2: Einen Vorschlag melden")

while True:
    wahl = input("Bitte gib 1 oder 2 ein (oder 'q' zum Beenden): ")

    if wahl == "1":
        problem = input("Was für ein Problem möchtest du melden? ")
        print(f"Du hast folgendes Problem gemeldet: {problem}")

    elif wahl == "2":
        vorschlag = input("Was für einen Vorschlag möchtest du melden? ")
        print(f"Du hast folgenden Vorschlag gemeldet: {vorschlag}")

    elif wahl.lower() == "q":
        print("Programm wird beendet.")
        break
    
    else:
        print("Ungültige Eingabe. Bitte gib 1 oder 2 ein.")