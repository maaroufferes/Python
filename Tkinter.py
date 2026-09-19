import numpy as np
note=np.array([0,15,12,6,18,19,8])
import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Gestion des Notes")
root.geometry("500x400")
tk.Label(root,text="Bienvenue dans l'application de notes",font=("Arial", 16)).pack()
tk.Button(root,text="Afficher les notes",command=lambda: messagebox.showinfo("Notes", str(note)),font=("Arial", 12)).pack()
tk.Button(root,text="Afficher la moyenne",command=lambda: messagebox.showinfo("Moyenne", str(np.mean(note))),font=("Arial", 12)).pack()
tk.Button(root,text="Notes >= 12",command=lambda: messagebox.showinfo("Notes >= 12", str(note[note>=12])),font=("Arial", 12)).pack()
tk.Button(root,text="Bonus",command=lambda: messagebox.showinfo("Notes +2", str(note+2)),font=("Arial", 12)).pack()
tk.Button(root,text="Quitter",command=root.quit,font=("Arial", 12)).pack()
root.mainloop()