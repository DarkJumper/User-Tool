import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import csv


# Klasse definieren
class PrtConfig:
    # Main frame Definieren
    def __init__(self):
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app)  # Abspeichern und Beenden des Frames
        self.master.title("Freelance Tool - copyright Peter Schwarz Aug 2019")
        self.Login()

    def Login(self):
        self.login = tk.Frame(self.master)
        self.login.pack()
        self.usr_label = tk.Label(self.login, text="Benutzer: ")
        self.pas_label = tk.Label(self.login, text="Passwort: ")
        self.User_entry = tk.Entry(self.login, bd=5, width=20)
        self.Passwort_entry = tk.Entry(self.login, show="*", bd=5, width=20)
        self.Button_Anmelden = tk.Button(self.login, text="Anmelden!", height=1, width=10, command=self.Anmelden)
        self.close = tk.Button(self.login, text="Schließen!", height=1, width=10, command=self.quit_app)
        self.usr_label.grid(row=0, column=0)
        self.pas_label.grid(row=1, column=0)
        self.User_entry.grid(row=0, column=1)
        self.Passwort_entry.grid(row=1, column=1)
        self.close.grid(row=2, column=2)
        self.Button_Anmelden.grid(row=2, column=1)
        self.login.mainloop()

    def Anmelden(self):
        login_user = self.User_entry.get()
        login_passwort = self.Passwort_entry.get()
        if "admin" == login_passwort and "admin" == login_user:
            messagebox.showinfo(message="Anmeldung erfolgreich!")
            self.login.destroy()
            self.Status_information()
        else:
            messagebox.showinfo(message="Anmeldung fehlgeschlagen!")

    def Status_information(self):
        self.status_Anzeigen = tk.Frame(self.master)
        self.status_Anzeigen.pack()
        self.status_label = tk.Label(self.status_Anzeigen, text="Work in Progess")
        self.Status_Grafik = ttk.Progressbar(self.status_Anzeigen, orient="horizontal", length=200, mode="determinate")
        self.status_label.grid(row=0, column=0)
        self.Status_Grafik.grid(row=1, column=0)
        self.Erstellen_laut_liste()
        self.status_Anzeigen.mainloop()

    # Hauptfenster schliesen
    def quit_app(self):
        self.master.destroy()


#test = PrtConfig()
