import os
import csv
import itertools


def M_BIN(data_line):
    final_data = []
    search_data = {'MBIN_B': 0, 'MBIN_K':0,'MBIN_L':0,'Mp': 4, 'Bt0': 4, 'Bt1': 4, 'Mt': 4}
    MBIN_filename = os.getcwd() + "\PRT\\" + "M_BIN.prt"
    new_filename = os.getcwd() + "\Ausgabe\\" + data_line["MBIN_B"] + '.prt'
    with open(MBIN_filename, 'r', encoding='utf-16') as infile, open(new_filename, 'w', encoding='utf-16') as outfile:
        for row in infile:
            striped_row = row.strip().split(';')

            for key in search_data:
                for count, element in enumerate(striped_row, start=0):
                    if key == element:
                        striped_row[count + search_data[key]] = data_line[key]
                        row = ";".join(striped_row)
            final_data.append(row.strip())
        outfile.write('\n'.join(final_data))


def neue_eintraege(data_line):
    #erstellen eines Dictionäris für zu suchende daten(key entspricht den neuen Inhalt
    key_var = [0,"MBIN_B","MBIN_K","MBIN_L","Bt1","Bt0","Mt","Mp"]
    data_iterrator = dict(zip(key_var,data_line))
    return data_iterrator


def csv_groeße_erfassen():
    #erfassen der Csv Länge für prozessbar!
    data_size = os.getcwd() + "\config\\" + "data.csv"
    with open(data_size) as file_size:
        return sum(1 for _ in csv.reader(file_size))


String_MBIN = 'M_BIN'
String_MANA = 'M_ANA'
data_size = csv_groeße_erfassen()
data_filename = os.getcwd() + "\config\\" + "data.csv"
with open(data_filename) as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    for line in itertools.islice(data, 1, None):
        MSR_Tag = line[1]
        dict_list_csv = neue_eintraege(line)
        if line[0] == String_MBIN:
            M_BIN(dict_list_csv)
        # if line[0] == String_MANA:
        #    print("M_ANA gefunden!")
