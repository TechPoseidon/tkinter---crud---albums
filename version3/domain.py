from tkinter import *
from db import *


def head(screen, text):
    head = Label(screen, text=text, fg='black',
                 height='2', font=("Roboto", "20", "bold"), bg='#6BACBF')
    head.pack(pady=25)
    return(head)


def navigation(screen_forget, screen_pack, app_height):
    screen_forget.pack_forget()
    if type(screen_pack) == Button:
        screen_pack.pack(pady=int(app_height)/2.215)
    else:
        screen_pack.pack(fill="both", expand=True)


def buttom_style(screen, texto: str, back_to, app_height, y, bgcolor, actbg):
    button = Button(screen, text=texto,
                    width='10', bg=bgcolor, fg='black', cursor="hand2", command=back_to, relief="solid", activebackground=actbg, activeforeground="white")
    button.pack(pady=int(app_height)/y)
    return button


def id_controller():
    global id_count

    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        id_count = int(objects[-2].split(",")[0])
    except:
        id_count = 0
    return id_count


def delete_entry_values(album_name, release_year, artist_group_name, artist_first_album_r1):
    album_name.set("")
    release_year.set("")
    artist_group_name.set("")
    artist_first_album_r1.select()


def save_info(album_name, release_year, artist_group_name, buttom_r, lbl, artist_first_album_r1):
    id_count = id_controller()
    try:
        id_count += 1
        instance = str(id_count)+","+album_name.get().upper()+","+str(release_year.get())+","+artist_group_name.get().upper() + \
            "," + buttom_r.get()
        instance_values = instance.split(",")
        for value in instance_values:
            if value == "":
                instance_values.remove(value)
        if len(instance_values) != 5:
            lbl.configure(text="Algum dado incorreto, tente novamente!",
                          bg='#6BACBF', font=("Roboto,13,bold"))
            delete_entry_values(
                album_name, release_year, artist_group_name, artist_first_album_r1)
        else:
            instance = ",".join(instance_values)
            instance = instance + ("\n")
            write_values(instance)
            lbl.configure(text="Álbum cadastrado com sucesso!",
                          bg='#6BACBF', font=("Roboto,13,bold"))
            delete_entry_values(
                album_name, release_year, artist_group_name, artist_first_album_r1)
    except:
        lbl.configure(text="Algum dado incorreto, tente novamente!",
                      bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values(
            album_name, release_year, artist_group_name, artist_first_album_r1)


def verify_none(home_frame, none_album, list_album):
    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        if len(objects[0]) == 0:
            navigation(home_frame, none_album, 0)
        else:
            navigation(home_frame, list_album, 0)
    except:
        navigation(home_frame, none_album, 0)


def delete_treeview_register(list_album_frame):
    data = list_album_frame.selection()
    for record in data:
        list_album_frame.delete(record)


def catch_info(pick, list_album_frame, combobox, radio_ano):
    if pick != 0:
        global file_values
        file_values = []
    try:
        objects = read_values()
        for instance in objects:
            try:
                if len(instance[0]) == 0:
                    pass
                else:
                    if pick == 1:
                        file_values.append(instance.split(',')[1])
                    elif pick == 2:
                        file_values.append(int(instance.split(',')[2]))

                    values = instance.split(",")
                    if pick == 0:
                        list_album_frame.insert('', END, values=values)
                    elif pick == 1 and combobox.get().upper() in values[1].upper():
                        list_album_frame.insert('', END, values=values)
                    elif pick == 2:
                        if int(combobox.get()) >= int(values[2]) and radio_ano.get() == 1:
                            list_album_frame.insert('', END, values=values)
                        elif int(combobox.get()) == int(values[2]) and radio_ano.get() == 2:
                            list_album_frame.insert('', END, values=values)
                        elif int(combobox.get()) <= int(values[2]) and radio_ano.get() == 3:
                            list_album_frame.insert('', END, values=values)
            except:
                pass
    except:
        pass
    if pick != 0:
        return sorted(set(file_values))


def search(pick, combobox, lbl2, search_by_frame, list_albums_screen, radio_year):
    if pick == 0:
        count = 0
        for name in file_values:
            if combobox.get().upper() in name:
                count += 1
        if len(combobox.get()) != 0 and count > 0:
            lbl2.configure(text="")
            navigation(search_by_frame, list_albums_screen(1, combobox, 0), 0)
            combobox.delete(0, END)
        else:
            lbl2.configure(text="Nada encontrado!",
                           bg='#6BACBF', font=("Roboto,13,bold"))
            combobox.delete(0, END)
    elif pick == 1:
        try:
            if len(combobox.get()) != 0:
                lbl2.configure(text="")
                count = 0
                if radio_year.get() == 1 and (int(combobox.get()) >= min(file_values)):
                    count += 1
                elif radio_year.get() == 3 and (int(combobox.get()) <= max(file_values)):
                    count += 1

                if count == 0 and int(combobox.get()) not in file_values:
                    lbl2.configure(text="Nada encontrado!",
                                   bg='#6BACBF', font=("Roboto,13,bold"))
                    combobox.delete(0, END)
                else:
                    navigation(search_by_frame, list_albums_screen(
                        2, combobox, radio_year), 0)
                    combobox.delete(0, END)
            else:
                lbl2.configure(text="Nada encontrado!",
                               bg='#6BACBF', font=("Roboto,13,bold"))
                combobox.delete(0, END)
        except:
            lbl2.configure(text="Digite um ano válido!",
                           bg='#6BACBF', font=("Roboto,13,bold"))
            combobox.delete(0, END)
