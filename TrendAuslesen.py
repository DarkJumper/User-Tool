import csv
from itertools import islice
import os
from datetime import *
import pandas as pd


class TrendEvaluate():
    def __init__(self, Measuring_point, date_begin, date_end):
        self.MSR = Measuring_point
        self.date_begin = date_begin
        self.date_end = date_end
        self.Header_Row()

    # Start funktion!
    def Header_Row(self):  # Kopfzeile erstellen und anschließend durch suchen nach Nummer in Trend Dateien
        df_Result = pd.DataFrame()
        for element in self.MSR:
            self.element = element
            if self.element == "":
                continue
            temp_header = ["Status von: " + element, "Datum: " + element, "Zeitstempel von: " + element,
                           "Messwert von: " + element]
            print(temp_header)
            df2 = df_Result.copy()
            df1 = self.Csv_Reader(temp_header)
            df1.sort_values(temp_header[1])
            df1.sort_values(temp_header[2])
            df_Result = pd.concat([df1, df2], axis=1)
        df_Result.to_excel("Trend_Auswertung.xlsx")

    def Csv_Reader(self, Header):
        temp_data = []
        files = os.listdir(os.getcwd() + "\Trends")
        for file_name in files:
            print(file_name)
            filename = os.getcwd() + "\Trends\\" + file_name
            count = 0
            with open(filename, newline='', encoding='utf-16') as csvfile:
                for line in islice(csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL), None):
                    if count == 0 and "EintragID" in line:
                        count += 1
                        found_cell = self.list_edit(line)
                        if found_cell is None:
                            break
                        continue
                    if count == 1:
                        eval_Row = line[found_cell - 3:found_cell + 1]
                        if eval_Row[1] != "" and eval_Row[2] != "":
                            list_date = datetime.strptime(eval_Row[1], '%d.%m.%y')
                            list_time = datetime.strptime(eval_Row[2].rstrip("S"), '%H:%M:%S.%f')
                            list_combine = datetime.combine(list_date.date(), list_time.time())
                            if self.date_begin <= list_combine <= self.date_end:
                                temp_data.append(eval_Row)

        df = pd.DataFrame(temp_data, columns=Header)
        return df

    def list_edit(self, line):  # funktion zum finden von Benutzten Zeilen der MSR stellen
        for y in range(4, len(line), 4):
            if self.element in line[y]:
                return y