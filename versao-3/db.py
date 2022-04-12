from tkinter import *


def id_controller():
    global id_count

    try:
        file = open("albuns_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        id_count = int(objects[-2].split(",")[0])
    except:
        id_count = 0
    return (id_count)


def write_values(values):
    try:
        file = open("albuns_data.txt", "a", encoding='utf-8')
        file.write(values)
        file.close()
    except:
        file = open("albuns_data.txt", "w", encoding='utf-8')
        file.write(values)
        file.close()


def read_values(pick, list_album_screen, box_name, list_box_name, box_year, list_box_year, radio_ano):
    global file_values
    file_values = []
    global file_year_values
    file_year_values = []
    try:
        file = open("albuns_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        for instance in objects:
            file_values.append(instance.split(',')[1])
            file_year_values.append(int(instance.split(',')[2]))
            try:
                if len(instance[0]) == 0:
                    pass
                else:
                    values = instance.split(",")
                    list_album_screen.insert('', END, values=values)
                    if box_name.get().upper() in values[1].upper():
                        list_box_name.insert('', END, values=values)
                    if int(box_year.get()) > int(values[2]) and radio_ano.get() == 1:
                        list_box_year.insert('', END, values=values)
                    elif int(box_year.get()) == int(values[2]) and radio_ano.get() == 2:
                        list_box_year.insert('', END, values=values)
                    elif int(box_year.get()) < int(values[2]) and radio_ano.get() == 3:
                        list_box_year.insert('', END, values=values)
            except:
                pass
    except:
        pass
    if pick == 0:
        return sorted(set(file_values))
    elif pick == 1:
        return sorted(set(file_year_values))


