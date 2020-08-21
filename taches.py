import tkinter as tk
from tkinter import ttk
import tkcalendar  as cal

font = "Arial"

def get_desc():
    return desc.get("1.0", tk.END+'-1c')
    

def save():
    if titre.get() == "" :
        titre.configure(highlightbackground = "red")
    else:
        titre.configure(highlightbackground = "white")

    if dated.get_date() > datef.get_date() :
        pass
    else:
        pass
        

    if get_desc() == "":
        desc.configure(highlightbackground = "red")
    else:
        desc.configure(highlightbackground = "red")


prog = tk.Tk()
prog.title("Tâches")

fen = ttk.Frame(prog, padding="10 10 10 10")
fen.pack()

cadre1 = ttk.Frame(fen, padding="5 5 5 5")
cadre1.grid(row =0, column = 0, sticky="NWES")

listbox = tk.Listbox(cadre1, height=13, font="Arial")
listbox.grid(row =0, column = 0, sticky="NWES")

for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)


# cadre 2
cadre2 = ttk.Frame(fen, padding="5 5 5 5")
cadre2.grid(row =0, column = 1)

tk.Label(cadre2, text = "Titre : ", font = "Arial").grid(
    row = 0, column = 0, columnspan = 4, sticky="W")

svt = tk.StringVar()
titre = tk.Entry(cadre2, textvariable=svt, width=50, font = "Arial",
                 highlightthickness=1)
titre.grid(row = 1, column = 0, columnspan=4)

tk.Label(cadre2, text = "Date début : ", font = "Arial").grid(
    row = 2, column = 0, sticky="W")
dated = cal.DateEntry(cadre2, date_pattern="dd/mm/Y", font = "Arial", locale="fr_FR",
                      highlightthickness=1)
dated.grid(row = 2, column = 1)

tk.Label(cadre2, text = "Date fin : ", font = "Arial").grid(
    row = 2, column = 2, sticky="W")
datef = cal.DateEntry(cadre2, date_pattern="dd/mm/Y", font = "Arial", locale="fr_FR",
                      highlightthickness=1)
datef.grid(row = 2, column = 3, sticky="E")


tk.Label(cadre2, text = "Description : ", font = "Arial").grid(
    row = 3, column = 0, columnspan = 4, sticky="W")
svd = tk.StringVar()
desc = tk.Text(cadre2, width=22, height=6, font = "Arial",
               highlightthickness=1)
desc.grid(row = 4, column = 0, sticky="EW", columnspan=4)

B = tk.Button(cadre2, text="Sauvegarder", command=lambda: save(), font = "Arial")
B.grid(row = 5, column = 0, sticky="E", columnspan=4)


prog.mainloop()
