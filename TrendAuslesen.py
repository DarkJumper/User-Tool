import csv
from itertools import islice
import os
from datetime import *
import pandas as pd
import openpyxl

class TrendEvaluate():
    def __init__(self, Measuring_point, Datum_Anfang, Datum_Ende, Zeit_Anfang, Zeit_Ende):
        self.MSR = Measuring_point
        self.Datum_Anfang = Datum_Anfang
        self.Datum_Ende = Datum_Ende
        self.Zeit_Anfang = Zeit_Anfang
        self.Zeit_Ende = Zeit_Ende

#Start funktion!
    def Header_Row(self): #Kopfzeile erstellen und anschließend durch suchen nach Nummer in Trend Dateien
        Data = []
        Header = []
        for element in self.MSR:
            print(element)
            self.element = element
            temp_header = ["Status von: " + element, "Datum: " + element, "Zeitstempel von: " + element, "Messwert von: " + element]
            Header.append(temp_header)
            Data.append(self.Csv_Reader())
        self.to_Excel(Data,Header)

    def Csv_Reader(self):
        temp_data = []
        files = os.listdir(os.getcwd() + "\Trends")
        for file_name in files:
            filename = os.getcwd() + "\Trends\\" + file_name
            print(filename)
            count = 0
            with open(filename, newline='', encoding='utf-16') as csvfile:
                for line in islice(csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL), 7, None):
                    if count == 0 and line[0] =="EintragID":
                        count +=1
                        self.found_cell = self.list_edit(line)
                        continue
                    elif self.found_cell is None:
                        continue
                    elif count > 0:
                        date_begin = datetime.strptime(self.Datum_Anfang, '%d.%m.%y')
                        date_end = datetime.strptime(self.Datum_Ende, '%d.%m.%y')
                        time_begin = datetime.strptime(self.Zeit_Anfang, '%H:%M:%S.%f')
                        time_end = datetime.strptime(self.Zeit_Ende, '%H:%M:%S.%f')
                        eval_Row = line[self.found_cell - 3:self.found_cell + 1]
                        if eval_Row[1] != "" and eval_Row[2] != "":
                            list_date = datetime.strptime(eval_Row[1], '%d.%m.%y')
                            list_time = datetime.strptime(eval_Row[2], '%H:%M:%S.%fS')
                            if list_date >= date_begin and list_date <= date_end and list_time >= time_begin and list_time <= time_end:
                               temp_data.append(eval_Row)
        return temp_data

    def list_edit(self,line):#funktion zum finden von Benutzten Zeilen der MSR stellen
        for y in range(4,len(line),4):
            if self.element in line[y]:
                return y

    def to_Excel(self,Data, Header):
        result_header = []
        result = []
        for column in Header:
            result_header = result_header + column
        df = pd.DataFrame(columns=result_header)
        for list in Data:
            if not list:
                result_data = [' ',' ',' ',' ']
                result = result_data
            for row in list:
                result = result + row
                df = df.append(result, ignore_index=True)
        df.to_excel("output.xlsx")  # doctest: +SKIP


MSR = ['Q1001','Q1029_Ist']#,'Q1101','Q1301','Q1501','Q1701','Q1801','Q1901','Q1914']
te = TrendEvaluate(MSR,"28.08.19","29.08.19","11:00:00.720","13:30:00.720")
te.Header_Row()