from tkinter import *
from db import *


def head(screen, text, x):
    head = Label(screen, text=text, fg='black',
                 height='2', font=("Roboto", "20", "bold"), bg='#6BACBF')
    head.place(x=x, y=30)


def save_info(album_name, release_year, artist_group_name, buttom_variable, lbl, artist_first_album_r1, artist_first_album_r2, box_name, box_year):
    id_controller()
    try:
        id_count += 1
        instance = str(id_count)+","+album_name.get().upper()+","+str(release_year.get())+","+artist_group_name.get().upper() + \
            "," + buttom_variable.get().upper()
        instance_values = instance.split(",")
        for value in instance_values:
            if value == "":
                instance_values.remove(value)
        if len(instance_values) != 5:
            id_count -= 1
            lbl.configure(text="Algum dado incorreto, tente novamente!",
                          bg='#6BACBF', font=("Roboto,13,bold"))
            delete_entry_values()
            artist_first_album_r1.deselect()
            artist_first_album_r2.deselect()
        else:
            instance = ",".join(instance_values)
            instance = instance + ("\n")
            print(instance)
            write_values(instance)
            box_name.configure(values=read_values(0))
            box_year.configure(values=read_values(1))
            lbl.configure(text="Álbum cadastrado com sucesso!",
                          bg='#6BACBF', font=("Roboto,13,bold"))
            delete_entry_values()
            artist_first_album_r1.deselect()
            artist_first_album_r2.deselect()
    except:
        id_count -= 1
        lbl.configure(text="Algum dado incorreto, tente novamente!",
                      bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values()
        artist_first_album_r1.deselect()
        artist_first_album_r2.deselect()


def search_artist_func(box_name, search_artist, lbl3, list_box_name):
    count = 0
    for name in file_values:
        if box_name.get().upper() in name:
            count += 1
    if len(box_name.get()) != 0 and count > 0:
        print(file_values)
        search_artist.pack_forget()
        lbl3.configure(text="")
        list_box_name.pack(fill="both", expand=True)
        read_values(0)
        delete_entry_values()
    else:
        lbl3.configure(text="Nada encontrado!",
                       bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values()


def search_year_func(box_year, lbl4, list_box_year, search_year):
    if len(box_year.get()) != 0:
        print(file_year_values)
        lbl4.configure(text="")
        read_values(1)
        if len(list_box_year.get_children()) > 0:
            search_year.pack_forget()
            list_box_year.pack(fill="both", expand=True)
            delete_entry_values()
        else:
            lbl4.configure(text="Nada encontrado!",
                           bg='#6BACBF', font=("Roboto,13,bold"))
            delete_entry_values()
    else:
        lbl4.configure(text="Nada encontrado!",
                       bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values()


def back_to_home(screen_conf, artist_first_album_r1, artist_first_album_r2, list_album_screen, search_artist, search_year, subscreen, list_box_name, list_box_year, none_album, register_screen, box_name, box_year, home_screen, lbl):
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    search_artist.pack_forget()
    search_year.pack_forget()
    subscreen.pack_forget()
    list_box_name.pack_forget()
    list_box_year.pack_forget()
    none_album.pack_forget()
    register_screen.pack_forget()
    box_name.pack_forget()
    box_year.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")
    artist_first_album_r1.deselect()
    artist_first_album_r2.deselect()
    delete_treeview_data()
    delete_entry_values()


def go_to_home(screen_conf, list_album_screen, none_album, register_screen, home_screen, lbl, artist_first_album_r1, artist_first_album_r2):
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    none_album.pack_forget()
    register_screen.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")
    artist_first_album_r1.deselect()
    artist_first_album_r2.deselect()
    delete_treeview_data()


def back_to_start(screen_conf, list_album_screen, register_screen, home_screen):
    screen_conf.pack(fill="both", expand=True)
    list_album_screen.pack_forget()
    register_screen.pack_forget()
    home_screen.pack_forget()


def back_to_search_artist(list_box_name, search_artist):
    list_box_name.pack_forget()
    search_artist.pack(fill="both", expand=True)
    delete_treeview_data()


def back_to_search_year(list_box_year, search_year):
    list_box_year.pack_forget()
    search_year.pack(fill="both", expand=True)
    delete_treeview_data()


def button_home(screen, texto: str, back_to, xx, yy, bgcolor, actbg):
    button = Button(screen, text=texto,
                    width='10', bg=bgcolor, fg='black', cursor="hand2", command=back_to, relief="solid", activebackground=actbg, activeforeground="white")
    button.place(x=xx, y=yy)


def load_register_screen(release_year, album_name, artist_group_name, artist_first_album_r1, screen_conf, home_screen, register_screen):
    release_year.set("Ano")
    album_name.set("Álbum")
    artist_group_name.set("Grupo ou Artista")
    artist_first_album_r1.select()
    screen_conf.pack_forget()
    home_screen.pack_forget()
    register_screen.pack(fill="both", expand=True)


def verify_none():
    try:
        file = open("albuns_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        if len(objects[0]) == 0:
            print("Nenhum usuário cadastrado")
            load_list_album_none()
        else:
            load_list_album_screen()
    except:
        print("Nenhum usuário cadastrado")
        load_list_album_none()


def verify_empty(box_r2):
    try:
        file = open("albuns_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        if len(objects[0]) == 0:
            load_list_album_none()
        else:
            box_r2.select()
            load_subscreen()
            delete_treeview_data()
    except:
        load_list_album_none()


def load_subscreen(home_screen, search_artist, search_year, subscreen, lbl3, lbl4):
    home_screen.pack_forget()
    search_artist.pack_forget()
    search_year.pack_forget()
    subscreen.pack(fill="both", expand=True)
    lbl3.configure(text="")
    lbl4.configure(text="")


def load_search_artist_name(subscreen, search_artist):
    subscreen.pack_forget()
    delete_treeview_data()
    search_artist.pack(fill="both", expand=True)


def load_search_year(subscreen, search_year):
    subscreen.pack_forget()
    delete_treeview_data()
    search_year.pack(fill="both", expand=True)


def load_list_album_screen(screen_conf, home_screen, none_album, list_album_screen):
    screen_conf.pack_forget()
    home_screen.pack_forget()
    none_album.pack_forget()
    list_album_screen.pack(fill="both", expand=True)
    read_values(2)


def load_list_album_none(screen_conf, home_screen, search_artist, subscreen, list_album_screen, none_album):
    screen_conf.pack_forget()
    home_screen.pack_forget()
    search_artist.pack_forget()
    subscreen.pack_forget()
    list_album_screen.pack_forget()
    none_album.pack(fill="both", expand=True)
    read_values(2)


def delete_entry_values(album_entry, release_entry, artist_group_entry, box_name, box_year):
    album_entry.delete(0, END)
    release_entry.delete(0, END)
    artist_group_entry.delete(0, END)
    box_name.delete(0, END)
    box_year.delete(0, END)


def delete_treeview_data(list_album_screen, list_box_name, list_box_year):
    for data in list_album_screen.get_children():
        list_album_screen.delete(data)

    for data in list_box_name.get_children():
        list_box_name.delete(data)

    for data in list_box_year.get_children():
        list_box_year.delete(data)


def delete_treeview_register(list_album_screen, list_box_name, list_box_year):
    data = list_album_screen.selection()
    for record in data:
        list_album_screen.delete(record)

    data_box_name = list_box_name.selection()
    for record in data_box_name:
        list_box_name.delete(record)

    data_box_year = list_box_year.selection()
    for record in data_box_year:
        list_box_year.delete(record)
