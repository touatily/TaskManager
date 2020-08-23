import tkinter as tk
from tkinter import ttk
import tkcalendar  as cal
from tkinter import filedialog as fd
import json
import os
from datetime import date

font = "Arial"
tasks = []
newTask = {"title":"", "description":"", "start":None, "end":None}
currFile = None

def get_desc():
    return desc.get("1.0", tk.END+'-1c')
    

def save(event = None):
    if titre.get() == "" :
        sv.set("Empty title!")
    elif dated.get_date() > datef.get_date() :
        sv.set("End date less than start date!")
    elif get_desc() == "":
        sv.set("Empty description!")
    else:
        sv.set("")
        task = {}
        task["title"] = titre.get()
        task["description"] = get_desc()
        task["start"] = str(dated.get_date())
        task["end"] = str(datef.get_date())
        act = listbox.get(listbox.curselection())
        #print(act)
        if act ==  "+":
            listbox.delete(len(tasks))
            listbox.insert(tk.END, str(len(tasks)+1) + "- " + task["title"])
            tasks.append(task)
            listbox.insert(tk.END, "+")
            listbox.select_set(len(tasks)-1)
        else:
            index = int(act.split("-")[0])
            listbox.delete(index-1)
            listbox.insert(index-1, str(index) + "- " + task["title"])
            tasks[index - 1] = task
            #listbox.insert(tk.END, "+")
            listbox.select_set(index - 1)
            
            
def saveInFile(event=None):
    global currFile
    if currFile == None:
        filename = fd.asksaveasfilename(initialdir = "./Data", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename=="" or len(filename) == 0: return
        with open(filename, "w") as f:
            json.dump(tasks, f)
            currFile = filename
            prog.title("TaskManager" + " - " + os.path.basename(filename))
    else:
        with open(currFile, "w") as f:
            json.dump(tasks, f, indent=4)
            
def saveAs(event=None):
    filename = fd.asksaveasfilename(initialdir = "./Data", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filename=="" or len(filename) == 0: return
    with open(filename, "w") as f:
        json.dump(tasks, f)
        currFile = filename
        prog.title("TaskManager" + " - " + os.path.basename(filename))
            

def openFile(event=None):
    global currFile, tasks
    filename = fd.askopenfilename(initialdir = "./Data", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if filename=="" or len(filename) == 0: return
    with open(filename, "r") as f:
        c = json.load(f)
        prog.title("TaskManager" + " - " + os.path.basename(filename))
        currFile = filename
        listbox.delete(0,tk.END)
        for i, item in enumerate(c):
            listbox.insert(tk.END, str(i+1) + "- " + item["title"])
        listbox.insert(tk.END, "+")
        listbox.select_set(0)
        svt.set(c[0]["title"])
        desc.delete(1.0,"end")
        desc.insert(1.0,c[0]["description"])
        dated.set_date(date.fromisoformat(c[0]["start"]))
        datef.set_date(date.fromisoformat(c[0]["end"]))
        tasks=c
        print(tasks)
            


def onselect(event):
    global newTask
    if listbox.curselection() == tuple():
        listbox.select_set(tk.ACTIVE)
        return
    curr = listbox.get(listbox.curselection())
    if curr == "+":
        svt.set(newTask["title"])
        desc.delete(1.0,"end")
        desc.insert(1.0,newTask["description"])
    else:
        index = int(curr.split("-")[0])-1
        if index < len(tasks):
            svt.set(tasks[index]["title"])
            desc.delete(1.0,"end")
            desc.insert(1.0,tasks[index]["description"])
            
            
def up(event=None):
    pass
    
def down(event = None):
    pass
    
def quitApp(event=None):
    prog.quit()

prog = tk.Tk()
prog.title("TaskManager")

# Menu

menubar = tk.Menu(prog)
filemenu = tk.Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", accelerator="Ctrl+N")
filemenu.add_command(label = "Open", accelerator="Ctrl+O", command=openFile)
filemenu.add_command(label = "Save", accelerator="Ctrl+S", command=saveInFile)
filemenu.add_command(label = "Save as...", command=saveAs)
filemenu.add_command(label = "Close", accelerator="Ctrl+W")
filemenu.add_command(label = "Print in PDF", accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label = "Exit", accelerator="Ctrl+Q", command=quitApp)
menubar.add_cascade(label = "File", menu = filemenu)


helpmenu = tk.Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Help", accelerator="F1")
helpmenu.add_command(label="About")
menubar.add_cascade(label = "Help", menu = helpmenu)

prog.config(menu = menubar)

prog.bind("<Control-s>", saveInFile)
prog.bind("<Control-o>", openFile)
prog.bind("<Return>", save)
prog.bind("<Control-q>", quitApp)
prog.bind("<Button-1>", lambda e: print(str(dated.get_date())))
prog.bind("<Up>", lambda e: print("Up"))
prog.bind("<Down>", lambda e: print("Down"))
### end Menu configuration 

fen = ttk.Frame(prog, padding="10 10 10 10")
fen.pack()

cadre1 = ttk.Frame(fen, padding="5 5 5 5")
cadre1.grid(row =0, column = 0, sticky="NWES")

listbox = tk.Listbox(cadre1, height=13, font="Arial", exportselection=0)
listbox.grid(row =0, column = 0, sticky="NWES")

listbox.bind('<<ListboxSelect>>', onselect)

for i, item in enumerate(tasks):
    listbox.insert(tk.END, str(i+1) + "- " + item["title"])
listbox.insert(tk.END, "+")
listbox.select_set(0)

# cadre 2
cadre2 = ttk.Frame(fen, padding="5 5 5 5")
cadre2.grid(row =0, column = 1)

tk.Label(cadre2, text = "Titre : ", font = "Arial").grid(
    row = 0, column = 0, columnspan = 4, sticky="W")

svt = tk.StringVar()
titre = tk.Entry(cadre2, textvariable=svt, width=50, font = "Arial", highlightthickness=1)
titre.grid(row = 1, column = 0, columnspan=4)

tk.Label(cadre2, text = "Date début : ", font = "Arial").grid(row = 2, column = 0, sticky="W")
dated = cal.DateEntry(cadre2, date_pattern="dd/mm/Y", font = "Arial", locale="fr_FR", borderwidth=1)
dated.grid(row = 2, column = 1)

tk.Label(cadre2, text = "Date fin : ", font = "Arial").grid(row = 2, column = 2, sticky="W")
datef = cal.DateEntry(cadre2, date_pattern="dd/mm/Y", font = "Arial", locale="fr_FR", borderwidth=1)
datef.grid(row = 2, column = 3, sticky="E")


tk.Label(cadre2, text = "Description : ", font = "Arial").grid(
    row = 3, column = 0, columnspan = 4, sticky="W")


desc = tk.Text(cadre2, width=22, height=6, font = "Arial", highlightthickness=1)
desc.grid(row = 4, column = 0, sticky="EW", columnspan=4)

sv = tk.StringVar()
sv.set("  ")
errLabel = tk.Label(cadre2, textvariable=sv, fg="red")
errLabel.grid(row = 5, column = 0, sticky="EW", columnspan=4)


B = tk.Button(cadre2, text="Valider", command=lambda: save(), font = "Arial")
B.grid(row = 6, column = 0, sticky="E", columnspan=4)


prog.mainloop()
