from db_json import *


def navigation(screen_forget, screen_pack):
    screen_forget.pack_forget()
    screen_pack.pack(fill="both", expand=True)


def id_controller():
    global id_count
    try:
        objects = read_values()
        id_count = len(objects)
        print(id_count)
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
        instance = {
            "id": id_count,
            "name": album_name.get().upper(),
            "year": release_year.get(),
            "artist": artist_group_name.get().upper(),
            "buttom_r": buttom_r.get()
        }
        count = 0
        for x in instance:
            if instance[x] == "" or instance[x] == " ":
                count += 1
        if count > 0:
            lbl.configure(text="Algum dado incorreto, tente novamente!",
                          bg='#6BACBF', font=("Roboto,13,bold"))
        else:
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
        objects = read_values()
        if len(objects) == 0:
            navigation(home_frame, none_album)
        else:
            navigation(home_frame, list_album)
    except:
        navigation(home_frame, none_album)


def delete_treeview_register(list_album_frame):
    data = list_album_frame.selection()
    for record in data:
        list_album_frame.delete(record)


def catch_info(pick, list_album_frame, combobox, radio_ano, end):
    if pick != 0:
        global file_values
        file_values = []
    try:
        objects = read_values()
        for instance in objects:
            try:
                if pick == 1:
                    file_values.append(instance['name'])
                elif pick == 2:
                    file_values.append(instance['year'])

                values = []
                for value in instance.values():
                    values.append(value)
                print(values)
                if pick == 0:
                    list_album_frame.insert('', end, values=values)
                elif pick == 1 and combobox.get().upper() in values[1].upper():
                    list_album_frame.insert('', end, values=values)
                elif pick == 2:
                    if int(combobox.get()) >= int(values[2]) and radio_ano.get() == 1:
                        list_album_frame.insert('', end, values=values)
                    elif int(combobox.get()) == int(values[2]) and radio_ano.get() == 2:
                        list_album_frame.insert('', end, values=values)
                    elif int(combobox.get()) <= int(values[2]) and radio_ano.get() == 3:
                        list_album_frame.insert('', end, values=values)
            except:
                pass
    except:
        pass
    if pick != 0:
        print((file_values))
        return sorted(set(file_values))


def search(pick, combobox, lbl2, search_by_frame, list_albums_screen, radio_year, end):
    if pick == 0:
        count = 0
        for name in file_values:
            if combobox.get().upper() in name:
                count += 1
        if len(combobox.get()) != 0 and count > 0:
            lbl2.configure(text="")
            navigation(search_by_frame, list_albums_screen(
                1, combobox, 0))
            combobox.delete(0, end)
        else:
            lbl2.configure(text="Nada encontrado!",
                           bg='#6BACBF', font=("Roboto,13,bold"))
            combobox.delete(0, end)
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
                    combobox.delete(0, end)
                else:
                    navigation(search_by_frame, list_albums_screen(
                        2, combobox, radio_year))
                    combobox.delete(0, end)
            else:
                lbl2.configure(text="Nada encontrado!",
                               bg='#6BACBF', font=("Roboto,13,bold"))
                combobox.delete(0, end)
        except:
            lbl2.configure(text="Digite um ano válido!",
                           bg='#6BACBF', font=("Roboto,13,bold"))
            combobox.delete(0, end)
