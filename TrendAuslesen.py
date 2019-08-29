import csv
from itertools import islice
import os
from datetime import *
import pandas as pd
from dask.dataframe.tests.test_categorical import df

class TrendEvaluate():
    def __init__(self, Measuring_point, Datum_Anfang, Datum_Ende, Zeit_Anfang, Zeit_Ende):
        self.MSR = Measuring_point
        self.Datum_Anfang = Datum_Anfang
        self.Datum_Ende = Datum_Ende
        self.Zeit_Anfang = Zeit_Anfang
        self.Zeit_Ende = Zeit_Ende

#Start funktion!
    def Header_Row(self): #Kopfzeile erstellen und anschließend durch suchen nach Nummer in Trend Dateien
        df_Result = pd.DataFrame()
        for element in self.MSR:
            self.element = element
            temp_header = ["Status von: " + element, "Datum: " + element, "Zeitstempel von: " + element, "Messwert von: " + element]
            df2 = df_Result.copy()
            df1 = self.Csv_Reader(temp_header)
            df1.sort_values(temp_header[1])
            df1.sort_values(temp_header[2])
            df_Result = pd.concat([df1,df2 ], axis=1)
        df_Result.to_excel("Trend_Auswertung.xlsx")

    def Csv_Reader(self,Header):
        files = os.listdir(os.getcwd() + "\Trends")
        for file_name in files:
            filename = os.getcwd() + "\Trends\\" + file_name
            print(filename)
            temp_data = []
            count = 0
            with open(filename, newline='', encoding='utf-16') as csvfile:
                for line in islice(csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL), 7, None):
                    temp_line = line[0]  # Daten stehen sind immer eine Liste schmiervariable damit ich nicht an die "Liste" gehen muss
                    temp_row = temp_line.split(";")

                    if count == 0:
                        count +=1
                        self.found_cell = self.list_edit(line)
                        continue
                    else:
                        eval_Row = temp_row[self.found_cell-3:self.found_cell+1]
                        date_begin = datetime.strptime(self.Datum_Anfang, '%d.%m.%y')
                        date_end = datetime.strptime(self.Datum_Ende, '%d.%m.%y')
                        time_begin = datetime.strptime(self.Zeit_Anfang, '%H:%M:%S.%f')
                        time_end = datetime.strptime(self.Zeit_Ende, '%H:%M:%S.%f')
                        try:
                            if eval_Row[1] != "" and eval_Row[2] != "":
                                list_date = datetime.strptime(eval_Row[1], '%d.%m.%y')
                                list_time = datetime.strptime(eval_Row[2], '%H:%M:%S.%fS')
                                if list_date >= date_begin and list_date <= date_end and list_time >= time_begin and list_time <= time_end:
                                    temp_data.append(eval_Row)
                        except IndexError:
                            eval_Row = line[self.found_cell - 3:self.found_cell + 1]
                            if eval_Row[1] != "" and eval_Row[2] != "":
                                list_date = datetime.strptime(eval_Row[1], '%d.%m.%y')
                                list_time = datetime.strptime(eval_Row[2], '%H:%M:%S.%fS')
                                if list_date >= date_begin and list_date <= date_end and list_time >= time_begin and list_time <= time_end:
                                    temp_data.append(eval_Row)

        df = pd.DataFrame(temp_data,columns= Header)
        return df

    def list_edit(self,line):#funktion zum finden von Benutzten Zeilen der MSR stellen
        temp_unit = line[0]
        temp_list = temp_unit.split(";")
        for i in range(4,len(temp_list),4):
            if self.element in temp_list[i]:
                return i
        for y in range(4,len(line),4):
            if self.element in line[y]:
                return y

MSR = ['E12011_Leist','E12011','E12031']
te = TrendEvaluate(MSR,"20.07.19","20.07.19","19:20:00.720","19:30:00.720")
te.Header_Row()