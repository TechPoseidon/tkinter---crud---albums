from tkinter import *
from tkinter import ttk

global id_count
id_count = 0


def write_values(values):
    try:
        file = open("users.txt", "a", encoding='utf-8')
        file.write(values)
        file.close()
    except:
        file = open("users.txt", "w", encoding='utf-8')
        file.write(values)
        file.close()


def read_values():
    file = open("users.txt", 'r', encoding='utf-8')
    objects = file.read().split('\n')
    file.close()
    for instance in objects:
        try:
            if len(instance[0]) == 0:
                pass
            else:
                values = instance.split(",")
                list_album_screen.insert('', END, values=values)
        except:
            pass


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


def head(screen):
    head = Label(screen, text='Albúm de Música', fg='black',
                 height='2', font=("Roboto", "20", "bold"), bg='#6BACBF')
    head.place(x=197, y=30)


def back_to_home():
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    none_user.pack_forget()
    register_screen.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")
    artist_first_album_r1.deselect()
    artist_first_album_r2.deselect()
    delete_treeview_data()


def go_to_home(event):
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    none_user.pack_forget()
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


def button_home(screen, texto: str, back_to, xx, yy, bgcolor, actbg):
    button = Button(screen, text=texto,
                    width='10', bg=bgcolor, fg='black', cursor="hand2", command=back_to, relief="solid", activebackground=actbg, activeforeground="white")
    button.place(x=xx, y=yy)


def load_register_screen():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    register_screen.pack(fill="both", expand=True)


def verify_none():
    try:
        file = open("users.txt", 'r', encoding='utf-8')
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


def load_list_album_screen():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    none_user.pack_forget()
    list_album_screen.pack(fill="both", expand=True)
    read_values()


def load_list_album_none():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    list_album_screen.pack_forget()
    none_user.pack(fill="both", expand=True)
    read_values()


def delete_entry_values():
    album_name_entry.delete(0, END)
    release_year_entry.delete(0, END)
    artist_group_name_entry.delete(0, END)


def delete_treeview_data():
    for data in list_album_screen.get_children():
        list_album_screen.delete(data)


def delete_treeview_register():
    data = list_album_screen.selection()
    for record in data:
        list_album_screen.delete(record)


# def anterior_a():
# def posterior_a():
# def igual_a():
"//////////////////////////////////////////////////////////////////////////////"
"CLASSE TELA"

screen = Tk()
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
    "Roboto", "13", "bold"), relief="groove")
release_year_entry = Entry(register_screen, textvariable=release_year, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "13", "bold"), relief="groove")
artist_group_name_entry = Entry(register_screen, textvariable=artist_group_name, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "13", "bold"), relief="groove")


buttom_variable = StringVar()
artist_first_album_r1 = Radiobutton(register_screen, variable=buttom_variable, text="Sim",
                                    bg='#6BACBF', fg='black', bd=2, relief="raised", value="SIM", selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
artist_first_album_r2 = Radiobutton(register_screen, variable=buttom_variable, text="Não",
                                    bg='#6BACBF', fg='black', bd=2, relief="raised", value="NÃO", selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")


album_name_entry.place(x=225, y=130, height='30')
release_year_entry.place(x=225, y=205, height='30')
artist_group_name_entry.place(x=225, y=280, height='30')
artist_first_album_r1.place(x=245, y=358)
artist_first_album_r2.place(x=305, y=358)


register = Button(register_screen, text='Cadastrar Álbum', width='13', bg='#6BACBF', fg='black', bd=2, font=(
    "Roboto", "13", "bold"), cursor="hand2", command=save_info, activebackground="#4edae4", activeforeground="white")
register.place(x=230, y=430)


lbl = Label(register_screen, bg='#6BACBF', wraplength=250, width=30)
lbl.place(x=160, y=480)

"Fim tela cadastro"
"//////////////////////////////////////////////////////////////////////////////"
"Tela de álbuns caso nenhum álbum"

none_user = Frame(screen)
none_user.configure(bg='#6BACBF')
label = Label(none_user, bg='#6BACBF', text="Nenhum álbum cadastrado", fg='black', bd=2, font=(
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

head(home_screen)

button_home(register_screen, "Voltar", back_to_home,
            260, 600, "#6BACBF", "#4edae4")
button_home(list_album_screen, "Voltar", back_to_home,
            510, 655, "#4edae4", "#6BACBF")
button_home(list_album_screen, "Remover", delete_treeview_register,
            510, 625, "#4edae4", "#6BACBF")
button_home(none_user, "Voltar", back_to_home, 260, 600, "#6BACBF", "#4edae4")
button_home(home_screen, "Voltar", back_to_start,
            260, 600, "#6BACBF", "#4edae4")

"//////////////////////////////////////////////////////////////////////////////"
"Tela buscar artista"


"Fim tela buscar artista"
"//////////////////////////////////////////////////////////////////////////////"

screen_conf.pack(fill=BOTH, expand=True)
screen.mainloop()
