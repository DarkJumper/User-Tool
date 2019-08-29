import tkinter as tk
from tkinter import filedialog
import FGR_Rename

#Klasse definieren
class App:
    # root/master initialisieren
    def __init__(self):
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app) #Abspeichern und Beenden des Frames
        self.master.title("Freelance Tool - copyright Peter Schwarz Aug 2019")
        self.set_main_frame()

    # Hauptfenster starten
    def set_main_frame(self):
        # Hauptframe definieren
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()
        # Widgets initialisieren
        self.quit_button = tk.Button(self.main_frame, text="Beenden", height= 1, width= 20, activebackground='#FF0000',
                                    command= self.quit_app)
        self.SFP_button = tk.Button(self.main_frame, text="SFP Auswerten",height= 1, width= 20, background='#58ACFA',
                                    command= self.SFP_Auswerten)
        self.rename_button = tk.Button(self.main_frame, text="Rename Grafik",height= 1, width= 20, background='#2EFEC8',
                                    command=self.Rename_Grafik_Frame)
        self.trend_button = tk.Button(self.main_frame, text="Trend Auswerten",height= 1, width= 20, background='#BFFF00')
        self.PRT_button = tk.Button(self.main_frame, text="PRT Erstellen",height= 1, width= 20, background='#FAAC58')
        self.copyright = tk.Label(self.main_frame, text='Copyright: Peter Schwarz', font=('Arial', 8))
        # Widgets positionieren
        self.SFP_button.grid(row=0, column=0)
        self.rename_button.grid(row=0, column=1)
        self.trend_button.grid(row=0, column=2)
        self.PRT_button.grid(row=0, column=3)
        self.copyright.grid(row=1, column=0)
        self.quit_button.grid(row=1, column=3)
        # Fenster neustarten
        self.master.mainloop()

    # Einsellungsfenster starten
    def Rename_Grafik_Frame(self):
        # rename Frame Definieren
        self.rename_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.rename_frame.pack()
        # Widgets initialisieren
        self.head_label = tk.Label(self.rename_frame, text='Grafikbilder Umbennen')
        self.Durchsuchen_button = tk.Button(self.rename_frame, text="Durchsuchen",height= 1, width= 20,
                                            command=self.file_dialog)
        self.Rename_button = tk.Button(self.rename_frame, text="Auführen!", height=1, width=20, activebackground='#40FF00',
                                            command=self.Rename_Ausführen)
        self.setting_entry = tk.Entry(self.rename_frame,width="50")
        self.safe_settings_button = tk.Button(self.rename_frame, text="Zurück!", height= 1, width= 20,
                                            command=self.safe_settings1)
        self.var = tk.StringVar()
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.Checkbox_PNG = tk.Checkbutton(self.rename_frame, text='PNG',offvalue="", onvalue="PNG", variable=self.var)
        self.Checkbox_JPG = tk.Checkbutton(self.rename_frame, text='JPG',offvalue="", onvalue="JPG", variable=self.var1)
        self.Checkbox_GIF = tk.Checkbutton(self.rename_frame, text='GIF',offvalue="", onvalue="GIF", variable=self.var2)
        # Widgets positionieren
        self.head_label.grid(row=0, column=0, columnspan=2)
        self.Durchsuchen_button.grid(row=1, column=0)
        self.setting_entry.grid(row=1, column=1,padx=5,pady=10,ipady=3)
        self.Checkbox_PNG.grid(row=2, column=0)
        self.Checkbox_JPG.grid(row=3, column=0)
        self.Checkbox_GIF.grid(row=4, column=0)
        self.Rename_button.grid(row=2, column=1)
        self.safe_settings_button.grid(row=3, column=1)
        # Fenster neustarten
        self.master.mainloop()

    def SFP_Auswerten(self):
        # rename Frame Definieren
        self.SFP_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.SFP_frame.pack()
        self.safe_settings_button = tk.Button(self.SFP_frame, text="Zurück!", height=1, width=20,
                                              command=self.safe_settings2)
        self.safe_settings_button.grid(row=3, column=1)
        self.master.mainloop()

    def file_dialog(self):
        filename = filedialog.askopenfilename(filetypes=(("Csv files", "*.csv;*.csv")
                                                         , ("All files", "*.*")))
        self.setting_entry.insert(0,filename)

    def Rename_Ausführen(self):
        Data_typ = self.var.get() + self.var1.get() + self.var2.get()
        file_path = self.setting_entry.get()
        rename = FGR_Rename.GraficRename(file_path, Data_typ)
        rename.Search_Grafic_Name()


    # Zum Hauptfenster zurückkehren
    def safe_settings1(self):
        # Einstellungsframe schließen
        self.rename_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    # Zum Hauptfenster zurückkehren
    def safe_settings2(self):
        # Einstellungsframe schließen
        self.SFP_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    def quit_app(self):
        self.master.destroy()


# App ausführen (Instanz der Klasse App erstellen)
app = App()