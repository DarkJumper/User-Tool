import os
import csv
import itertools


def prt_beschreiben(data_name, write_data):
    new_filename = os.getcwd() + "\Ausgabe\\" + data_name + '.prt'
    with open(new_filename, 'w', encoding='utf-16') as outfile:
        outfile.write('\n'.join(write_data))


def target_change(key_searched, searching_line, new_target):
    # sucht zeile mit ergebnis und ändert diese liste wird zurück gegeben bei keinem fund wird
    # "nothing" zurück gegeben eventuell mit einer exception ändern
    stripped_line = searching_line.strip().split(';')
    for count, element in enumerate(stripped_line, start=0):
        if key_searched[0] == element:
            stripped_line[count] = new_target[key_searched[1]]
            return stripped_line
    return "nothing"


def neue_eintraege(data_line):
    # erstellen eines Dictionäris für zu suchende daten(key entspricht den neuen Inhalt
    key_var = [0, "MBIN_B", "MBIN_K", "MBIN_L", "Bt1", "Bt0", "Mt", "Mp"]
    data_iterrator = dict(zip(key_var, data_line))
    return data_iterrator


def csv_groeße_erfassen():
    # erfassen der Csv Länge für prozessbar!
    data_size = os.getcwd() + "\config\\" + "data.csv"
    with open(data_size) as file_size:
        return sum(1 for _ in csv.reader(file_size))


def used_search_key(search_tags):
    switcher={
        "[PB:NODE]": ["MBIN",1]
    }
    return switcher[search_tags]


def M_BIN(data_line):
    final_data = []
    search_tags = ["[PB:NODE]"]  # ,"[MSR:RECORD]","[EAM:RECORD]"]
    MBIN_filename = os.getcwd() + "\PRT\\" + "M_BIN.prt"
    with open(MBIN_filename, 'r', encoding='utf-16') as infile:
        for row in infile:
            for tags in search_tags:
                if tags in row:
                    key_line = used_search_key(tags)
                    new_line = target_change(key_line, row, data_line)
                    print(new_line)
                    if new_line == "nothing":
                        break

    #                row = ";".join(striped_row)
    #    final_data.append(row.strip())
    # prt_beschreiben(data_line["MBIN_B"],final_data)
    # search_data = {'MBIN_B': 0, 'MBIN_K':0,'MBIN_L':0,'Mp': 4, 'Bt0': 4, 'Bt1': 4, 'Mt': 4}


String_MBIN = 'M_BIN'
String_MANA = 'M_ANA'
data_size = csv_groeße_erfassen()
data_filename = os.getcwd() + "\config\\" + "data.csv"
with open(data_filename) as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    for line in itertools.islice(data, 1, None):
        if line[0] == String_MBIN:
            M_BIN(line)
        # if line[0] == String_MANA:
        #    print("M_ANA gefunden!")
