from tkinter import *
from tkinter import ttk


global id_count

try:
    file = open("albums_data.txt", 'r', encoding='utf-8')
    objects = file.read().split('\n')
    file.close()
    id_count = int(objects[-2].split(",")[0])
except:
    id_count = 0


def write_values(values):
    try:
        file = open("albums_data.txt", "a", encoding='utf-8')
        file.write(values)
        file.close()
    except:
        file = open("albums_data.txt", "w", encoding='utf-8')
        file.write(values)
        file.close()


def read_values(pick):
    global file_values
    file_values = []
    global file_year_values
    file_year_values = []
    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
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
                    if int(box_year.get()) >= int(values[2]) and radio_year.get() == 1:
                        list_box_year.insert('', END, values=values)
                    elif int(box_year.get()) == int(values[2]) and radio_year.get() == 2:
                        list_box_year.insert('', END, values=values)
                    elif int(box_year.get()) <= int(values[2]) and radio_year.get() == 3:
                        list_box_year.insert('', END, values=values)
            except:
                pass
    except:
        pass
    if pick == 0:
        return sorted(set(file_values))
    elif pick == 1:
        return sorted(set(file_year_values))


def save_info():
    global id_count
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


def head(screen, text, x):
    head = Label(screen, text=text, fg='black',
                 height='2', font=("Roboto", "20", "bold"), bg='#6BACBF')
    head.place(x=x, y=30)


def back_to_home():
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


def go_to_home(event):
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    none_album.pack_forget()
    register_screen.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")
    artist_first_album_r1.deselect()
    artist_first_album_r2.deselect()
    delete_treeview_data()


def back_to_start():
    screen_conf.pack(fill="both", expand=True)
    list_album_screen.pack_forget()
    register_screen.pack_forget()
    home_screen.pack_forget()


def back_to_search_artist():
    list_box_name.pack_forget()
    search_artist.pack(fill="both", expand=True)
    delete_treeview_data()


def back_to_search_year():
    list_box_year.pack_forget()
    search_year.pack(fill="both", expand=True)
    delete_treeview_data()


def back(screen, texto: str, back_to, xx, yy, bgcolor, actbg):
    button = Button(screen, text=texto,
                    width='10', bg=bgcolor, fg='black', cursor="hand2", command=back_to, relief="solid", activebackground=actbg, activeforeground="white")
    button.place(x=xx, y=yy)


def load_register_screen():
    release_year.set("Ano")
    album_name.set("Álbum")
    artist_group_name.set("Grupo ou Artista")
    artist_first_album_r1.select()
    screen_conf.pack_forget()
    home_screen.pack_forget()
    register_screen.pack(fill="both", expand=True)


def verify_none():
    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
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


def verify_empty():
    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
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


def load_subscreen():
    home_screen.pack_forget()
    search_artist.pack_forget()
    search_year.pack_forget()
    subscreen.pack(fill="both", expand=True)
    lbl3.configure(text="")
    lbl4.configure(text="")


def load_search_artist_name():
    subscreen.pack_forget()
    delete_treeview_data()
    search_artist.pack(fill="both", expand=True)


def load_search_year():
    subscreen.pack_forget()
    delete_treeview_data()
    search_year.pack(fill="both", expand=True)


def search_artist_func():
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


def search_year_func():
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


def load_list_album_screen():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    none_album.pack_forget()
    list_album_screen.pack(fill="both", expand=True)
    read_values(2)


def load_list_album_none():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    search_artist.pack_forget()
    subscreen.pack_forget()
    list_album_screen.pack_forget()
    none_album.pack(fill="both", expand=True)
    read_values(2)


def delete_entry_values():
    album_name_entry.delete(0, END)
    release_year_entry.delete(0, END)
    artist_group_name_entry.delete(0, END)
    box_name.delete(0, END)
    box_year.delete(0, END)


def delete_treeview_data():
    for data in list_album_screen.get_children():
        list_album_screen.delete(data)

    for data in list_box_name.get_children():
        list_box_name.delete(data)

    for data in list_box_year.get_children():
        list_box_year.delete(data)


def delete_treeview_register():
    data = list_album_screen.selection()
    for record in data:
        list_album_screen.delete(record)

    data_box_name = list_box_name.selection()
    for record in data_box_name:
        list_box_name.delete(record)

    data_box_year = list_box_year.selection()
    for record in data_box_year:
        list_box_year.delete(record)


"//////////////////////////////////////////////////////////////////////////////"
"CLASSE TELA"

screen = Tk()
screen.title("Álbum de Música")
screen.geometry('600x700')
screen.configure(bg='#6BACBF')
screen.resizable(False, False)

"FIM CLASSE TELA"
"//////////////////////////////////////////////////////////////////////////////"
"Tela inicial"

screen_conf = Label(screen, height='2',  bg='#6BACBF')
screen_conf_button = Button(screen_conf, text='Albúm de Música', fg='black', font=(
    "Roboto", "20", "bold"), bg='#6BACBF', cursor="hand2", relief='flat', activeforeground="white")
screen_conf_button.place(x='173', y='316')

screen_conf_button.bind('<Button-1>', go_to_home)

"Fim tela inicial"
"//////////////////////////////////////////////////////////////////////////////"
"Tela home"

home_screen = Frame(screen, bg='#6BACBF')

register_button = Button(home_screen, text="Novo Albúm",  width='30',
                         bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_register_screen, relief="solid", activebackground="#4edae4", activeforeground="white")
register_button.place(x=115, y=130)

list_album_button = Button(home_screen, text="Meus Albúms",  width='30',
                           bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2", command=verify_none, relief="solid", activebackground="#4edae4", activeforeground="white")
list_album_button.place(x=115, y=180)

search_main_button = Button(home_screen, text="Buscar Albúm",  width='30',
                            bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=verify_empty, relief="solid", activebackground="#4edae4", activeforeground="white")
search_main_button.place(x=115, y=230)


"Fim home"
"//////////////////////////////////////////////////////////////////////////////"
"Tela cadastro"

register_screen = Frame(screen, bg='#6BACBF')

album_name_text = Label(register_screen, text='Nome do Álbum', bd='1', bg='#6BACBF',
                        fg='black', font=("Roboto", "11", "bold"))
release_year_text = Label(register_screen, text='Ano de Lançamento', bd='1', bg='#6BACBF',
                          fg='black', font=("Roboto", "11", "bold"))
artist_group_name_text = Label(register_screen, text='Nome da Banda', bd='1',
                               bg='#6BACBF', fg='black', font=("Roboto", "11", "bold"))
artist_first_album_text = Label(register_screen, text='Primeiro Álbum do Artista',
                                bd='1', bg='#6BACBF', fg='black', font=("Roboto", "11", "bold"))

album_name_text.place(x=225, y=110)
release_year_text.place(x=225, y=185)
artist_group_name_text.place(x=225, y=260)
artist_first_album_text.place(x=225, y=335)

album_name = StringVar(register_screen)
release_year = IntVar(register_screen)
artist_group_name = StringVar(register_screen)


album_name_entry = Entry(register_screen, textvariable=album_name, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "11"), relief="groove")
release_year_entry = Entry(register_screen, textvariable=release_year, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "11"), relief="groove")
artist_group_name_entry = Entry(register_screen, textvariable=artist_group_name, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "11"), relief="groove")


buttom_variable = StringVar()
artist_first_album_r1 = Radiobutton(register_screen, variable=buttom_variable, width='4', text="Sim", font=("Roboto", "11"), cursor="hand2",
                                    bg='#6BACBF', fg='black', bd=2, relief="groove", value="SIM", selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
artist_first_album_r2 = Radiobutton(register_screen, variable=buttom_variable, width='4', text="Não", font=("Roboto", "11"), cursor="hand2",
                                    bg='#6BACBF', fg='black', bd=2, relief="groove", value="NÃO", selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")


album_name_entry.place(x=225, y=130, height='30')
release_year_entry.place(x=225, y=205, height='30')
artist_group_name_entry.place(x=225, y=280, height='30')
artist_first_album_r1.place(x=227, y=358)
artist_first_album_r2.place(x=301, y=358)


register = Button(register_screen, text='Cadastrar', width='10   ', bg='#6BACBF', fg='black', bd=2, font=(
    "Roboto", "13", "bold"), cursor="hand2", command=save_info, activebackground="#4edae4", activeforeground="white")
register.place(x=245, y=430)


lbl = Label(register_screen, bg='#6BACBF', wraplength=250, width=30)
lbl.place(x=160, y=480)

"Fim tela cadastro"
"//////////////////////////////////////////////////////////////////////////////"
"Tela de álbuns caso nenhum álbum"

none_album = Frame(screen)
none_album.configure(bg='#6BACBF')
label = Label(none_album, bg='#6BACBF', text="Nenhum álbum cadastrado", fg='black', bd=2, font=(
    "Roboto", "15", "bold"))
label.place(x="190", y="200")

"Fim tela álbuns none"
"/////////////////////////////////////////////////////////////////////////////"
"Tela de álbuns caso tenha algum álbum"

columns = ("id", 'album_name', 'release_year',
           'artist_group_name', 'artist_first_album')

list_album_screen = ttk.Treeview(screen, columns=columns, show='headings')

list_album_screen.column("id", minwidth="25", width="10",
                         anchor=CENTER)
list_album_screen.column("album_name", minwidth="50", width="50", anchor=W)
list_album_screen.column("release_year", minwidth="50", width="50", anchor=W)
list_album_screen.column(
    "artist_group_name", minwidth="80", width="50", anchor=W)
list_album_screen.column("artist_first_album",
                         minwidth="50", width="50", anchor=W)

list_album_screen.heading('id', text="ID", anchor=CENTER)
list_album_screen.heading('album_name', text='Álbum', anchor=W)
list_album_screen.heading('release_year', text='Ano', anchor=W)
list_album_screen.heading(
    'artist_group_name', text='Artista/Grupo', anchor=W)
list_album_screen.heading('artist_first_album',
                          text='Primeiro Álbum', anchor=W)

scrollbar = ttk.Scrollbar(
    list_album_screen, orient=VERTICAL, command=list_album_screen.yview)
list_album_screen.configure(yscroll=scrollbar.set)

style = ttk.Style()

style.configure("Treeview", foreground="black", background="#6BACBF",
                rowheight=30, fieldbackground="#6BACBF")
style.map("Treeview", background=[
          ('selected', "#4edae4")], foreground=[('selected', "black")])

"Fim tela álbuns screen"
"//////////////////////////////////////////////////////////////////////////////"
"Tela buscar artista"


search_artist = Frame(screen, bg='#6BACBF')
box_name = ttk.Combobox(search_artist, values=read_values(
    0), width="13", font=("Roboto", "10", "bold"))
box_name.place(x=215, y=320)

lbl3 = Label(search_artist, bg='#6BACBF', wraplength=250, width=30)
lbl3.place(x=170, y=480)

list_box_name = ttk.Treeview(
    screen, columns=columns, show='headings')

list_box_name.column("id", minwidth="25", width="10",
                     anchor=CENTER)
list_box_name.column(
    "album_name", minwidth="50", width="50", anchor=W)
list_box_name.column(
    "release_year", minwidth="50", width="50", anchor=W)
list_box_name.column(
    "artist_group_name", minwidth="80", width="50", anchor=W)
list_box_name.column("artist_first_album",
                     minwidth="50", width="50", anchor=W)

list_box_name.heading('id', text="ID", anchor=CENTER)
list_box_name.heading('album_name', text='Álbum', anchor=W)
list_box_name.heading('release_year', text='Ano', anchor=W)
list_box_name.heading(
    'artist_group_name', text='Artista/Grupo', anchor=W)
list_box_name.heading('artist_first_album',
                      text='Primeiro Álbum', anchor=W)

scrollbar_box_name = ttk.Scrollbar(
    list_box_name, orient=VERTICAL, command=list_box_name.yview)
list_box_name.configure(yscroll=scrollbar.set)

style_box_name = ttk.Style()

style_box_name.configure("Treeview", foreground="black", background="#6BACBF",
                         rowheight=30, fieldbackground="#6BACBF")
style_box_name.map("Treeview", background=[
    ('selected', "#4edae4")], foreground=[('selected', "black")])


box_name_button = Button(search_artist, text="Pesquisar",
                         width='8', bg="#6BACBF", fg='black', cursor="hand2", font=("Roboto", "9", "bold"), command=search_artist_func, relief="solid", activebackground="aqua", activeforeground="white")
box_name_button.place(x=335, y=319)


"Fim tela buscar artista"
"//////////////////////////////////////////////////////////////////////////////"
"Tela de busca"

subscreen = Frame(screen)
subscreen.configure(background="#6BACBF")

search_artist_button = Button(subscreen, text="Por Artista",  width='20',
                              bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_search_artist_name, relief="solid", activebackground="#4edae4", activeforeground="white")
search_artist_button.place(x=180, y=130)

search_year_button = Button(subscreen, text="Por Ano",  width='20',
                            bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_search_year, relief="solid", activebackground="#4edae4", activeforeground="white")
search_year_button.place(x=180, y=180)

"Fim tela de busca"
"//////////////////////////////////////////////////////////////////////////////"
"Tela buscar por ano"

search_year = Frame(screen, bg='#6BACBF')

lbl4 = Label(search_year, bg='#6BACBF', wraplength=250, width=30)
lbl4.place(x=170, y=480)

list_box_year = ttk.Treeview(
    screen, columns=columns, show='headings')

list_box_year.column("id", minwidth="25", width="10",
                     anchor=CENTER)
list_box_year.column(
    "album_name", minwidth="50", width="50", anchor=W)
list_box_year.column(
    "release_year", minwidth="50", width="50", anchor=W)
list_box_year.column(
    "artist_group_name", minwidth="80", width="50", anchor=W)
list_box_year.column("artist_first_album",
                     minwidth="50", width="50", anchor=W)

list_box_year.heading('id', text="ID", anchor=CENTER)
list_box_year.heading('album_name', text='Álbum', anchor=W)
list_box_year.heading('release_year', text='Ano', anchor=W)
list_box_year.heading(
    'artist_group_name', text='Artista/Grupo', anchor=W)
list_box_year.heading('artist_first_album',
                      text='Primeiro Álbum', anchor=W)

scrollbar_box_year = ttk.Scrollbar(
    list_box_year, orient=VERTICAL, command=list_box_year.yview)
list_box_year.configure(yscroll=scrollbar.set)

style_box_year = ttk.Style()

style_box_year.configure("Treeview", foreground="black", background="#6BACBF",
                         rowheight=30, fieldbackground="#6BACBF")
style_box_year.map("Treeview", background=[
    ('selected', "#4edae4")], foreground=[('selected', "black")])

box_year = ttk.Combobox(
    search_year, values=read_values(1), width="8", font=("Roboto", "11", "bold"))
box_year.place(x=230, y=320)

box_year_button = Button(search_year, text="Pesquisar",
                         width='8', bg="#6BACBF", fg='black', cursor="hand2", font=("Roboto", "9", "bold"), command=search_year_func, relief="solid", activebackground="aqua", activeforeground="white")
box_year_button.place(x=320, y=319)


radio_year = IntVar()
box_r1 = Radiobutton(search_year, variable=radio_year, width='8', text="Anterior a", font=("Roboto", "10"), cursor="hand2",
                     bg='#6BACBF', fg='black', bd=2, relief="groove", value=1, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
box_r2 = Radiobutton(search_year, variable=radio_year, width='8', text="Igual a", font=("Roboto", "10"), cursor="hand2",
                     bg='#6BACBF', fg='black', bd=2, relief="groove", value=2, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
box_r3 = Radiobutton(search_year, variable=radio_year, width='8', text="Posterior a", font=("Roboto", "10"), cursor="hand2",
                     bg='#6BACBF', fg='black', bd=2, relief="groove", value=3, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
box_r1.place(x=140, y=260)
box_r2.place(x=255, y=260)
box_r3.place(x=370, y=260)


"Fim tela buscar por ano"
"//////////////////////////////////////////////////////////////////////////////"

head(home_screen, "Álbum de Música", 197)
head(register_screen, "Cadastrar Álbum", 197)
head(subscreen, "Buscar Álbum", 215)
head(search_artist, "Buscar Por Artista", 197)
head(search_year, "Buscar Por Ano", 197)

back(register_screen, "Voltar", back_to_home,
     260, 600, "#6BACBF", "#4edae4")
back(list_album_screen, "Voltar", back_to_home,
     510, 655, "#4edae4", "#6BACBF")
back(list_album_screen, "Remover", delete_treeview_register,
     510, 625, "#4edae4", "#6BACBF")
back(none_album, "Voltar", back_to_home, 260, 600, "#6BACBF", "#4edae4")

back(home_screen, "Voltar", back_to_start,
     260, 600, "#6BACBF", "#4edae4")
back(search_artist, "Voltar", load_subscreen,
     260, 600, "#6BACBF", "#4edae4")
back(search_year, "Voltar", load_subscreen,
     260, 600, "#6BACBF", "#4edae4")
back(list_box_name, "Voltar", back_to_search_artist,
     510, 655, "#4edae4", "#6BACBF")
back(list_box_name, "Remover", delete_treeview_register,
     510, 625, "#4edae4", "#6BACBF")
back(list_box_year, "Voltar", back_to_search_year,
     510, 655, "#4edae4", "#6BACBF")
back(list_box_year, "Remover", delete_treeview_register,
     510, 625, "#4edae4", "#6BACBF")
back(subscreen, "Voltar", back_to_home,
     260, 600, "#6BACBF", "#4edae4")

screen_conf.pack(fill=BOTH, expand=True)
screen.mainloop()
