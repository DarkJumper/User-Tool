import os
import tkinter as tk
from tkinter import filedialog


class GrafikUmbennen:
    def __init__(self):
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app)  # Abspeichern und Beenden des Frames
        self.master.title("Freelance Tool - copyright Peter Schwarz Aug 2019")
        self.pop_up = tk.Frame(self.master)
        # Fenster Definieren Auslagern der Buttons etc. in UI_Inhalt funktion
        self.UI = tk.Frame(self.master)
        self.UI.pack()
        # Widgets initialisieren
        self.head_label_Prt = tk.Label(self.UI, text='Grafikbilder Umbennen')
        self.Durchsuchen_button = tk.Button(self.UI, text="Durchsuchen", height=1, width=20,
                                            command=self.file_dialog)
        self.Rename_button = tk.Button(self.UI, text="Auführen!", height=1, width=20,
                                       command=self.Rename_Ausführen, activebackground='#40FF00')
        self.setting_entry = tk.Entry(self.UI, width="50")
        self.safe_settings_button = tk.Button(self.UI, text="Zurück!", height=1, width=20,
                                              command=self.quit_app, background='#FE2E2E')
        self.var = tk.StringVar()
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.Checkbox_PNG = tk.Checkbutton(self.UI, text='PNG', offvalue="", onvalue=".png", variable=self.var)
        self.Checkbox_JPG = tk.Checkbutton(self.UI, text='JPG', offvalue="", onvalue=".jpg",
                                           variable=self.var1)
        self.Checkbox_GIF = tk.Checkbutton(self.UI, text='GIF', offvalue="", onvalue=".gif",
                                           variable=self.var2)
        # Widgets positionieren
        self.head_label_Prt.grid(row=0, column=0, columnspan=2)
        self.Durchsuchen_button.grid(row=1, column=0)
        self.setting_entry.grid(row=1, column=1, padx=5, pady=10, ipady=3)
        self.Checkbox_PNG.grid(row=2, column=0)
        self.Checkbox_JPG.grid(row=3, column=0)
        self.Checkbox_GIF.grid(row=4, column=0)
        self.Rename_button.grid(row=2, column=1)
        self.safe_settings_button.grid(row=3, column=1)
        self.UI.mainloop()

    # Dateipfad Fenster Öffnen
    def file_dialog(self):
        filename = filedialog.askopenfilename(filetypes=(("Csv files", "*.csv;*.csv")
                                                         , ("All files", "*.*")))
        self.setting_entry.insert(0, filename)

    def Rename_Ausführen(self):
        FGR = []
        try:
            with open(self.setting_entry.get(), 'r', newline='', encoding='utf-16') as file:
                for row in file:
                    splitted_row = row.strip().split(";")
                    if '[PBV:OBJPATH]' in row and "FGRBLT" in row and not "Pool" in row:
                        FGR.append(splitted_row[-1].replace("/", "_"))
                FGR.sort()
                for count, Grafik in enumerate(FGR, start=1):
                    old_file = os.path.join(os.getcwd() + "\FGR", "image" + str(count).zfill(
                        4) + self.var.get() + self.var1.get() + self.var2.get())
                    new_file = os.path.join(os.getcwd() + "\FGR",
                                            Grafik + self.var.get() + self.var1.get() + self.var2.get())
                    os.rename(old_file, new_file)
        except FileNotFoundError:
            self.pop_up_Fenster("Image Datei konnte nicht gefunden werden!")

    def pop_up_Fenster(self, text):
        # Bei erneutem öffnen wird fenster ein Zweitesmal definiert
        self.pop_up = tk.Frame(self.master)
        self.pop_up.pack()
        Info_Text = tk.Label(self.pop_up, text=text, font=('Arial', 10))
        quit_button = tk.Button(self.pop_up, text="Ok", height=1, width=20, activebackground='#FF0000',
                                command=self.close_pop_up)
        Info_Text.pack()
        quit_button.pack()

    def close_pop_up(self):
        self.pop_up.destroy()

    # Hauptfenster schließen
    def quit_app(self):
        self.master.destroy()