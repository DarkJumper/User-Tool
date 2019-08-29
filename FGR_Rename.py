import os
import tkinter as tk

class GraficRename():
    def __init__(self, File, Data_Typ):
        self.File = File
        self.Data_Typ = Data_Typ

    def Search_Grafic_Name(self):
        try:
            count = 1
            FGR = []
            Value = []
            with open(self.File, 'r', newline='', encoding='utf-16') as file:
                for row in file:
                    splitted_row = row.strip().split(";")
                    if '[PBV:OBJPATH]' in row and "FGRBLT" in row and not "Pool" in row:
                        FGR.append(splitted_row[-1].replace("/", "_"))
                        FGR.sort()
                        Value.append("image" + str(count).zfill(4))
                        count += 1
                self.Rename(FGR,Value)

        except FileNotFoundError:
            self.found_failer("CSV File konnte nicht gefunden werden!")

    def Rename(self,new_Name,old_Name):
        try:
            Typ = self.data_typ()
            for element in range(0, len(new_Name)):
                old_file = os.path.join(os.getcwd() + "\FGR", old_Name[element] + Typ)
                new_file = os.path.join(os.getcwd() + "\FGR", new_Name[element] + Typ)
                os.rename(old_file, new_file)
        except FileNotFoundError:
            self.found_failer("Image Datei konnte nicht gefunden werden!")

    def found_failer(self,Text):
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit_app)  # Abspeichern und Beenden des Frames
        self.master.title(Text)
        self.Info_Text = tk.Label(self.master, text=Text, font=('Arial', 10))
        self.quit_button = tk.Button(self.master, text="Ok", height=1, width=20, activebackground='#FF0000',
                                     command=self.quit_app)
        self.Info_Text.pack()
        self.quit_button.pack()


    def data_typ(self):
        if self.Data_Typ == "PNG":
            self.Typ = ".png"
        if self.Data_Typ == "JPG":
            self.Typ = ".jpg"
        if self.Data_Typ == "GIF":
            self.Typ = ".gif"
        else:
            self.Typ = ".png"

        return self.Typ

    def quit_app(self):
        self.master.destroy()