import csv
from itertools import islice
import os
from datetime import *
import pandas as pd


class TrendEvaluate():
    def __init__(self, Measuring_point, Datum_Anfang, Datum_Ende, Zeit_Anfang, Zeit_Ende):
        self.MSR = Measuring_point
        self.date_begin, self.date_end = self.date_edit(Datum_Anfang, Datum_Ende, Zeit_Anfang, Zeit_Ende)

    # Start funktion!
    def Header_Row(self):  # Kopfzeile erstellen und anschließend durch suchen nach Nummer in Trend Dateien
        df_Result = pd.DataFrame()
        for element in self.MSR:
            self.element = element
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
                            list_time = datetime.strptime(eval_Row[2], '%H:%M:%S.%fS')
                            list_combine = datetime.combine(list_date.date(), list_time.time())
                            if self.date_begin <= list_combine <= self.date_end:
                                temp_data.append(eval_Row)

        df = pd.DataFrame(temp_data, columns=Header)
        return df

    def list_edit(self, line):  # funktion zum finden von Benutzten Zeilen der MSR stellen
        for y in range(4, len(line), 4):
            if self.element in line[y]:
                print(y)
                return y

    def date_edit(self,Datum_Anfang, Datum_Ende, Zeit_Anfang, Zeit_Ende):
        date_begin = datetime.strptime(Datum_Anfang, '%d.%m.%y')
        date_end = datetime.strptime(Datum_Ende, '%d.%m.%y')
        time_begin = datetime.strptime(Zeit_Anfang, '%H:%M:%S.%f')
        time_end = datetime.strptime(Zeit_Ende, '%H:%M:%S.%f')
        date_combine_begin = datetime.combine(date_begin.date(), time_begin.time())
        date_combine_end = datetime.combine(date_end.date(), time_end.time())
        return date_combine_begin,date_combine_end


MSR = ['Q1001', 'Q1029_Ist','Q1101','Q1301','Q1501','Q1701','Q1801','Q1901']
te = TrendEvaluate(MSR, "28.08.19", "29.08.19", "11:00:00.720", "13:30:00.720")
te.Header_Row()
