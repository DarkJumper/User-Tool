import os
from itertools import islice
import csv
import re
import pandas as pd

class SFPEvaulate():
    def __init__(self):
        pass

    def Csv_Path(self):
        data_line= []
        files = os.listdir(os.getcwd() + "\SFP")
        for file_name in files:
            filename = os.getcwd() + "\SFP\\" + file_name
            print(filename)
            with open(filename, newline='', encoding='utf-16') as csvfile:
                for line in islice(csv.reader(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL), 5, None):
                    last_line = " ".join(re.split("\s+",line[4], flags=re.UNICODE)) # Löschen alle Überflüssigen Whitespaces(Doppelte)
                    sentence = last_line.split(" ")
                    if "Zeitmarke" in sentence or "SignFolgProt" in sentence:
                        continue
                    else:
                        info_line = " ".join(sentence[6:len(sentence)])
                        data_line.append(line[2])
                        data_line.append(sentence[2])
                        data_line.append(sentence[5])
                        data_line.append(info_line)
                        self.Evaluate(data_line)

    def Evaluate(self,data_line):
        Result_line = []
        Result_line.append(data_line)
        df = pd.DataFrame(Result_line)
        print(df)



    def pandas(self):
        files = os.listdir(os.getcwd() + "\SFP")
        for file_name in files:
            filename = os.getcwd() + "\SFP\\" + file_name
            df = pd.read_csv(filename,sep= ';',header= None,skiprows= 5,quotechar='"',quoting= csv.QUOTE_NONE,encoding= 'utf-16')
            print(df)
            #df.to_excel("Test.xlsx")


test =SFPEvaulate()
test.Csv_Path()