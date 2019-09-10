import tkinter as tk
from tkinter import filedialog
from datetime import *
import FGR_Rename
import TrendAuslesen
import PRT_confi


# Klasse definieren
class App:
    # root/master initialisieren
    def __init__(self):
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app)  # Abspeichern und Beenden des Frames
        self.master.title("Freelance Tool - copyright Peter Schwarz Aug 2019")
        self.set_main_frame()

    # Hauptfenster starten
    def set_main_frame(self):
        # Hauptframe definieren
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack()
        # Widgets initialisieren
        self.quit_button = tk.Button(self.main_frame, text="Beenden", height=1, width=20, activebackground='#FF0000',
                                     command=self.quit_app)
        self.SFP_button = tk.Button(self.main_frame, text="SFP Auswerten", height=1, width=20, background='#58ACFA',
                                    command=self.SFP_Auswerten)
        self.rename_button = tk.Button(self.main_frame, text="Rename Grafik", height=1, width=20, background='#2EFEC8',
                                       command=self.Rename_Grafik_Frame)
        self.trend_button = tk.Button(self.main_frame, text="Trend Auswerten", height=1, width=20, background='#BFFF00',
                                      command=self.Trend_Auswerten)
        self.PRT_button = tk.Button(self.main_frame, text="PRT Erstellen", height=1, width=20, background='#FAAC58',
                                    command=PRT_confi.PrtConfig)
        self.Info_button = tk.Button(self.main_frame, text="INFO!", height=1, width=20, background='#F7FE2E',
                                     command=self.INFO)
        self.copyright = tk.Label(self.main_frame, text='Copyright: Peter Schwarz', font=('Arial', 8))
        # Widgets positionieren
        self.SFP_button.grid(row=0, column=0)
        self.rename_button.grid(row=0, column=1)
        self.trend_button.grid(row=0, column=2)
        self.PRT_button.grid(row=0, column=3)
        self.copyright.grid(row=1, column=0)
        self.Info_button.grid(row=1, column=2)
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
        self.head_label_Prt = tk.Label(self.rename_frame, text='Grafikbilder Umbennen')
        self.Durchsuchen_button = tk.Button(self.rename_frame, text="Durchsuchen", height=1, width=20,
                                            command=self.file_dialog)
        self.Rename_button = tk.Button(self.rename_frame, text="Auführen!", height=1, width=20,
                                       activebackground='#40FF00',
                                       command=self.Rename_Ausführen)
        self.setting_entry = tk.Entry(self.rename_frame, width="50")
        self.safe_settings_button = tk.Button(self.rename_frame, text="Zurück!", height=1, width=20,
                                              background='#FE2E2E',
                                              command=self.safe_settings_RENAME)
        self.var = tk.StringVar()
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.Checkbox_PNG = tk.Checkbutton(self.rename_frame, text='PNG', offvalue="", onvalue="PNG", variable=self.var)
        self.Checkbox_JPG = tk.Checkbutton(self.rename_frame, text='JPG', offvalue="", onvalue="JPG",
                                           variable=self.var1)
        self.Checkbox_GIF = tk.Checkbutton(self.rename_frame, text='GIF', offvalue="", onvalue="GIF",
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
        # Fenster neustarten
        self.master.mainloop()

    def SFP_Auswerten(self):
        # rename Frame Definieren
        self.SFP_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.SFP_frame.pack()
        self.head_label_SFP = tk.Label(self.SFP_frame, text='SFP Auswerten ist noch in Arbeit!')
        self.safe_settings_button_SFP = tk.Button(self.SFP_frame, text="Zurück!", height=1, width=20,
                                                  command=self.safe_settings_SFP)
        self.head_label_SFP.grid(row=0, column=0, columnspan=2)
        self.safe_settings_button_SFP.grid(row=3, column=1)
        self.master.mainloop()

    def Trend_Auswerten(self):
        # rename Frame Definieren
        self.Trend_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.Trend_frame.pack()
        self.head_label_trend = tk.Label(self.Trend_frame, text='Trends Auswerten!', font=('Arial', 10))
        self.label_date = tk.Label(self.Trend_frame, text="Datum", font=('Arial', 8))
        self.label_time = tk.Label(self.Trend_frame, text="Zeit", font=('Arial', 8))
        self.label_begin = tk.Label(self.Trend_frame, text="Von", font=('Arial', 8))
        self.label_end = tk.Label(self.Trend_frame, text="bis", font=('Arial', 8))
        self.label_MSR = tk.Label(self.Trend_frame, text="MSR Stellen", font=('Arial', 8))
        self.safe_settings_button_Trend = tk.Button(self.Trend_frame, text="Zurück!", height=1, width=10,
                                                    background='#FE2E2E',
                                                    command=self.safe_settings_Trend)
        self.button_Trend_Auswerten = tk.Button(self.Trend_frame, text="Auswerten!", height=1, width=10,
                                                command=self.Trend_Auswerten_Aufrufen)
        self.setting_entry_Date_begin = tk.Entry(self.Trend_frame, width="10")
        self.setting_entry_Date_end = tk.Entry(self.Trend_frame, width="10")
        self.setting_entry_time_begin = tk.Entry(self.Trend_frame, width="10")
        self.setting_entry_time_end = tk.Entry(self.Trend_frame, width="10")
        self.MSR_entry = tk.Entry(self.Trend_frame, width="35")
        self.setting_entry_Date_begin.insert(8, 'TT.MM.JJ')
        self.setting_entry_Date_end.insert(8, 'TT.MM.JJ')
        self.setting_entry_time_begin.insert(8, 'HH:MM:SS')
        self.setting_entry_time_end.insert(8, 'HH:MM:SS')
        self.MSR_entry.insert(8, 'P1000,L1000,...')
        self.head_label_trend.grid(row=0, column=0, columnspan=5)
        self.button_Trend_Auswerten.grid(row=3, column=4)
        self.label_date.grid(row=2, column=1)
        self.label_time.grid(row=2, column=2)
        self.label_begin.grid(row=3, column=0)
        self.label_end.grid(row=4, column=0)
        self.setting_entry_Date_begin.grid(row=3, column=1, padx=5, pady=1, ipady=3)
        self.setting_entry_Date_end.grid(row=4, column=1, padx=5, pady=1, ipady=3)
        self.setting_entry_time_begin.grid(row=3, column=2, padx=5, pady=1, ipady=3)
        self.setting_entry_time_end.grid(row=4, column=2, padx=5, pady=1, ipady=3)
        self.MSR_entry.grid(row=1, column=1, padx=1, pady=1, ipady=3, columnspan=5)
        self.label_MSR.grid(row=1, column=0)
        self.safe_settings_button_Trend.grid(row=4, column=4)
        self.master.mainloop()

    def INFO(self):
        # rename Frame Definieren
        self.info_frame = tk.Frame(self.master)
        # Hauptframe schließen
        self.main_frame.destroy()
        self.info_frame.pack()
        self.head_label_info = tk.Label(self.info_frame, text='NOCH PLATZHALTER')
        self.safe_settings_button_info = tk.Button(self.info_frame, text="Zurück!", height=1, width=20,
                                                   command=self.safe_settings_info)
        self.head_label_info.grid(row=0, column=0, columnspan=2)
        self.safe_settings_button_info.grid(row=3, column=1)
        self.master.mainloop()

    def Rename_Ausführen(self):
        Data_typ = self.var.get() + self.var1.get() + self.var2.get()
        file_path = self.setting_entry.get()
        rename = FGR_Rename.GraficRename(file_path, Data_typ)
        rename.Search_Grafic_Name()

    def file_dialog(self):
        filename = filedialog.askopenfilename(filetypes=(("Csv files", "*.csv;*.csv")
                                                         , ("All files", "*.*")))
        self.setting_entry.insert(0, filename)

    # Zum Hauptfenster zurückkehren
    def safe_settings_RENAME(self):
        # Einstellungsframe schließen
        self.rename_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    def Trend_Auswerten_Aufrufen(self):
        MSR = self.MSR_entry.get().split(",")
        try:
            date_begin = datetime.strptime(self.setting_entry_Date_begin.get(), '%d.%m.%y')
            date_end = datetime.strptime(self.setting_entry_Date_end.get(), '%d.%m.%y')
            time_begin = datetime.strptime(self.setting_entry_time_begin.get() + ".000", '%H:%M:%S.%f')
            time_end = datetime.strptime(self.setting_entry_time_end.get() + ".000", '%H:%M:%S.%f')
            TrendAuslesen.TrendEvaluate(MSR, datetime.combine(date_begin.date(), time_begin.time()),
                                        datetime.combine(date_end.date(), time_end.time()))
            self.Message()
        except ValueError:
            # rename Frame Definieren
            self.pop_up = tk.Frame(self.master)
            # Hauptframe schließen
            self.Trend_frame.destroy()
            self.pop_up.pack()
            self.head_label_pop_up = tk.Label(self.pop_up, text='Falscher Datentyp eingegeben!', font=('Arial', 16))
            self.safe_settings_button_pop_up = tk.Button(self.pop_up, text="Zurück!", height=1, width=20,
                                                         background='#FE2E2E',
                                                         command=self.pop_up_close)
            self.head_label_pop_up.grid(row=0, column=0, columnspan=2)
            self.safe_settings_button_pop_up.grid(row=1, column=0, columnspan=2)
            self.master.mainloop()

    def Message(self):
        # rename Frame Definieren
        self.Message = tk.Frame(self.master)
        # Hauptframe schließen
        self.Trend_frame.destroy()
        self.Message.pack()
        self.head_label_message = tk.Label(self.Message, text='Trenddaten Erfolgreich Ausgewertet',
                                           font=('Arial', 14), fg="green")
        self.safe_settings_button_message = tk.Button(self.Message, text="Zurück!", height=1, width=20,
                                                      background='#FE2E2E',
                                                      command=self.Message_close)
        self.head_label_message.grid(row=0, column=0, columnspan=2)
        self.safe_settings_button_message.grid(row=1, column=0, columnspan=2)
        self.master.mainloop()

    # Zum Hauptfenster zurückkehren
    def safe_settings_SFP(self):
        # Einstellungsframe schließen
        self.SFP_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    # Zum Hauptfenster zurückkehren
    def pop_up_close(self):
        # Einstellungsframe schließen
        self.pop_up.destroy()
        # Hauptframe starten
        self.Trend_Auswerten()

    # Zum Hauptfenster zurückkehren
    def Message_close(self):
        # Einstellungsframe schließen
        self.Message.destroy()
        # Hauptframe starten
        self.set_main_frame()

    # Zum Hauptfenster zurückkehren
    def safe_settings_Trend(self):
        # Einstellungsframe schließen
        self.Trend_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    # Zum Hauptfenster zurückkehren
    def safe_settings_info(self):
        # Einstellungsframe schließen
        self.info_frame.destroy()
        # Hauptframe starten
        self.set_main_frame()

    def quit_app(self):
        self.master.destroy()


# App ausführen (Instanz der Klasse App erstellen)
app = App()
