# takenlijst.py

import os

# Functie om de takenlijst op te slaan in een bestand
def sla_taken_op(taken):
    with open('takenlijst.txt', 'w') as bestand:
        for taak in taken:
            bestand.write(taak + '\n')

# Functie om de takenlijst uit een bestand te lezen
def lees_taken():
    if os.path.exists('takenlijst.txt'):
        with open('takenlijst.txt', 'r') as bestand:
            taken = bestand.readlines()
        return [taak.strip() for taak in taken]
    return []

# Functie om de lijst van taken weer te geven
def toon_taken(taken):
    if not taken:
        print("Er zijn geen taken in je lijst.")
    else:
        print("\nTakenlijst:")
        for index, taak in enumerate(taken, 1):
            print(f"{index}. {taak}")

# Hoofdprogramma
def main():
    taken = lees_taken()

    while True:
        print("\nWat wil je doen?")
        print("1. Toon takenlijst")
        print("2. Voeg taak toe")
        print("3. Verwijder taak")
        print("4. Verlaat")
        
        keuze = input("Voer je keuze in (1/2/3/4): ")

        if keuze == '1':
            toon_taken(taken)
        elif keuze == '2':
            nieuwe_taak = input("Voer de taak in die je wilt toevoegen: ")
            taken.append(nieuwe_taak)
            sla_taken_op(taken)
            print(f"Taak '{nieuwe_taak}' toegevoegd.")
        elif keuze == '3':
            toon_taken(taken)
            taak_nummer = int(input("Voer het nummer in van de taak die je wilt verwijderen: "))
            if 1 <= taak_nummer <= len(taken):
                verwijderde_taak = taken.pop(taak_nummer - 1)
                sla_taken_op(taken)
                print(f"Taak '{verwijderde_taak}' verwijderd.")
            else:
                print("Ongeldig taaknummer.")
        elif keuze == '4':
            print("Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    main()
