import tkinter as tk
from tkinter import messagebox
import json
import os

# Functie om de gegevens op te slaan in een bestand
def sla_op(data, bestand):
    with open(bestand, 'w') as file:
        json.dump(data, file, indent=4)

# Functie om de gegevens uit een bestand te laden
def laad_bestand(bestand):
    if os.path.exists(bestand):
        with open(bestand, 'r') as file:
            return json.load(file)
    return {}

# Functie om de gegevens van de planning weer te geven
def toon_planning(planning):
    planning_tekst = f"Training: {planning['training']['doel']} voor {planning['training']['duur']}\n"
    planning_tekst += f"Dieet: Ontbijt: {planning['dieet']['ontbijt']}, Lunch: {planning['dieet']['lunch']}, Diner: {planning['dieet']['diner']}, Tussendoortjes: {planning['dieet']['tussendoortjes']}\n"
    planning_tekst += f"Werk: Werkuren: {planning['werk']['werkuren']}, Taak: {planning['werk']['taak']}\n"
    planning_tekst += f"Sociaal: Vrienden: {', '.join(planning['sociaal']['vrienden'])}, Fanaten: {planning['sociaal']['fanaten']}, Tribute: {planning['sociaal']['tribute']}"
    
    messagebox.showinfo("Je Dagplanning", planning_tekst)

# Functie om het trainingsschema in te voeren
def trainingsschema():
    def opslaan_training():
        planning['training'] = {
            "doel": entry_training.get(),
            "duur": entry_duur.get()
        }
        messagebox.showinfo("Training", "Training opgeslagen!")
        root_training.destroy()

    root_training = tk.Toplevel(root)
    root_training.title("Training Invoer")
    
    tk.Label(root_training, text="Wat is je trainingsdoel voor vandaag?").pack()
    entry_training = tk.Entry(root_training)
    entry_training.pack()

    tk.Label(root_training, text="Hoe lang train je vandaag?").pack()
    entry_duur = tk.Entry(root_training)
    entry_duur.pack()

    tk.Button(root_training, text="Opslaan", command=opslaan_training).pack()

# Functie om het dieet in te voeren
def dieetplan():
    def opslaan_dieet():
        planning['dieet'] = {
            "ontbijt": entry_ontbijt.get(),
            "lunch": entry_lunch.get(),
            "diner": entry_diner.get(),
            "tussendoortjes": entry_tussendoortjes.get()
        }
        messagebox.showinfo("Dieet", "Dieet opgeslagen!")
        root_dieet.destroy()

    root_dieet = tk.Toplevel(root)
    root_dieet.title("Dieet Invoer")
    
    tk.Label(root_dieet, text="Wat eet je voor ontbijt?").pack()
    entry_ontbijt = tk.Entry(root_dieet)
    entry_ontbijt.pack()

    tk.Label(root_dieet, text="Wat eet je voor lunch?").pack()
    entry_lunch = tk.Entry(root_dieet)
    entry_lunch.pack()

    tk.Label(root_dieet, text="Wat eet je voor diner?").pack()
    entry_diner = tk.Entry(root_dieet)
    entry_diner.pack()

    tk.Label(root_dieet, text="Wat zijn je tussendoortjes?").pack()
    entry_tussendoortjes = tk.Entry(root_dieet)
    entry_tussendoortjes.pack()

    tk.Button(root_dieet, text="Opslaan", command=opslaan_dieet).pack()

# Functie om het werkrooster in te voeren
def werkrooster():
    def opslaan_werk():
        planning['werk'] = {
            "werkuren": entry_werkuren.get(),
            "taak": entry_taak.get()
        }
        messagebox.showinfo("Werk", "Werkrooster opgeslagen!")
        root_werk.destroy()

    root_werk = tk.Toplevel(root)
    root_werk.title("Werk Invoer")
    
    tk.Label(root_werk, text="Van welke tijd tot welke tijd werk je?").pack()
    entry_werkuren = tk.Entry(root_werk)
    entry_werkuren.pack()

    tk.Label(root_werk, text="Wat is je belangrijkste taak voor vandaag?").pack()
    entry_taak = tk.Entry(root_werk)
    entry_taak.pack()

    tk.Button(root_werk, text="Opslaan", command=opslaan_werk).pack()

# Functie om sociale activiteiten in te voeren
def sociale_activiteiten():
    def opslaan_sociaal():
        planning['sociaal'] = {
            "vrienden": entry_vrienden.get().split(','),
            "fanaten": entry_fanaten.get(),
            "tribute": entry_tribute.get()
        }
        messagebox.showinfo("Sociaal", "Sociaal plan opgeslagen!")
        root_sociaal.destroy()

    root_sociaal = tk.Toplevel(root)
    root_sociaal.title("Sociaal Invoer")
    
    tk.Label(root_sociaal, text="Met wie wil je vandaag afspreken?").pack()
    entry_vrienden = tk.Entry(root_sociaal)
    entry_vrienden.pack()

    tk.Label(root_sociaal, text="Wie van je trouwe volgelingen wil je in de spotlight zetten?").pack()
    entry_fanaten = tk.Entry(root_sociaal)
    entry_fanaten.pack()

    tk.Label(root_sociaal, text="Hoe wil je de wereld eren vandaag?").pack()
    entry_tribute = tk.Entry(root_sociaal)
    entry_tribute.pack()

    tk.Button(root_sociaal, text="Opslaan", command=opslaan_sociaal).pack()

# Functie om de hoofdpagina weer te geven
def hoofdpagina():
    global planning
    planning_bestand = 'dagplanning.json'
    planning = laad_bestand(planning_bestand)

    if not planning:
        messagebox.showinfo("Welkom", "Welkom! Je gaat je dag plannen.")
    else:
        toon_planning(planning)

# Hoofdvenster voor de GUI
root = tk.Tk()
root.title("Dagplanner")

planning = {}

# Knoppen voor verschillende invoeropties
tk.Button(root, text="Trainingsschema invoeren", command=trainingsschema).pack(pady=5)
tk.Button(root, text="Dieetplan invoeren", command=dieetplan).pack(pady=5)
tk.Button(root, text="Werkrooster invoeren", command=werkrooster).pack(pady=5)
tk.Button(root, text="Sociaal plan invoeren", command=sociale_activiteiten).pack(pady=5)
tk.Button(root, text="Bekijk je planning", command=lambda: toon_planning(planning)).pack(pady=5)

root.mainloop()
