from tkinter import *


screen = Tk()
screen.geometry('600x700')
screen.configure(bg='#6BACBF')
screen.resizable(False, False)

screen_conf = Label(screen, height='2',  bg='#6BACBF')

home_screen = Frame(screen, bg='#6BACBF')
register_screen = Frame(screen, bg='#6BACBF')
list_album_screen = Frame(screen, bg='#6BACBF')

"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"


def instance_format(value):
    print(f"\nNome: {value[0]}")
    lbl = Label(list_album_screen, bg='white', text=f"\nNome: {value[0]}")
    lbl.pack()
    print(f"\nrelease_year: {value[1]}")
    lbl2 = Label(list_album_screen, bg='white',
                 text=f"\nrelease_year: {value[1]}")
    lbl2.pack()
    print(f"\nMátricula: {value[2]}")
    lbl3 = Label(list_album_screen, bg='white',
                 text=f"\nMátricula: {value[2]}")
    lbl3.pack()
    print(f"\nNome: {value[3]}")
    lbl4 = Label(list_album_screen, bg='white',
                 text=f"\nData de nascimento: {value[3]}")
    lbl4.pack()


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
    try:
        file = open("users.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        if len(objects[0]) == 0:
            print("Nenhum usuário cadastrado")
            lbl2.configure(bg='#6BACBF', text="Nenhum usuário cadastrado")
        else:
            for instance in objects:
                print(instance)
                try:
                    if len(instance[0]) == 0:
                        pass
                    else:
                        value = instance.split(',')
                        instance_format(value)
                except:
                    pass
    except:
        lbl2.configure(bg='#6BACBF', text="Nenhum usuário cadastrado")


def save_info():
    instance = album_name.get()+","+release_year.get()+","+artist_group_name.get() + \
        "," + artist_first_album.get()
    instance_values = instance.split(",")
    for value in instance_values:
        if value == "":
            instance_values.remove(value)
    if len(instance_values) != 4:
        lbl.configure(text="Algum dado incorreto, tente novamente!",
                      bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values()

    else:
        instance = ",".join(instance_values)
        instance = instance + ("\n")
        print(instance)
        write_values(instance)
        lbl.configure(text="Álbum cadastrado com sucesso!",
                      bg='#6BACBF', font=("Roboto,13,bold"))
        delete_entry_values()


"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"


def heading(screen):
    heading = Label(screen, text='Albúm de Música', fg='black',
                    height='2', font=("Roboto", "20", "bold"), bg='#6BACBF')
    heading.place(x=197, y=30)


def back_to_home():
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    register_screen.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")
    lbl2.configure(text="")


def go_to_home(event):
    screen_conf.pack_forget()
    list_album_screen.pack_forget()
    register_screen.pack_forget()
    home_screen.pack(fill="both", expand=True)
    lbl.configure(text="")


def back_to_start():
    screen_conf.pack(fill="both", expand=True)
    list_album_screen.pack_forget()
    register_screen.pack_forget()
    home_screen.pack_forget()


def button_home(screen, texto: str, back_to):
    button = Button(screen, text=texto,
                    width='10', bg='#6BACBF', fg='black', cursor="hand2", command=back_to, relief="solid")
    button.place(x=260, y=600)


def load_register_screen():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    register_screen.pack(fill="both", expand=True)


def load_list_album_screen():
    screen_conf.pack_forget()
    home_screen.pack_forget()
    list_album_screen.pack(fill="both", expand=True)
    read_values()


def delete_entry_values():
    album_name_entry.delete(0, END)
    release_year_entry.delete(0, END)
    artist_group_name_entry.delete(0, END)
    artist_first_album_entry.delete(0, END)


"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

screen_conf_button = Button(screen_conf, text='Albúm de Música', fg='black', font=(
    "Roboto", "20", "bold"), bg='#6BACBF', cursor="hand2", relief='flat')
screen_conf_button.place(x='173', y='316')

screen_conf_button.bind('<Button-1>', go_to_home)

"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

"Tela inicio"
register_button = Button(home_screen, text="Novo Albúm",  width='30',
                         bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_register_screen, relief="solid")
register_button.place(x=115, y=130)

list_album_button = Button(home_screen, text="Meus Albúms",  width='30',
                           bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2", command=load_list_album_screen, relief="solid")
list_album_button.place(x=115, y=180)
"Fim tela inicio"

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

"Tela cadastro"
album_name_text = Label(register_screen, text='Nome do Álbum', bd='1', bg='#6BACBF',
                        fg='black', font=("Roboto", "11", "bold"))
release_year_text = Label(register_screen, text='Ano de Lançamento', bd='1', bg='#6BACBF',
                          fg='black', font=("Roboto", "11", "bold"))
artist_group_name_text = Label(register_screen, text='Nome da Banda', bd='1',
                               bg='#6BACBF', fg='black', font=("Roboto", "11", "bold"))
artist_first_album_text = Label(register_screen, text='Primeiro Álbum do Artista',
                                bd='1', bg='#6BACBF', fg='black', font=("Roboto", "11", "bold"))

album_name_text.place(x=215, y=110)
release_year_text.place(x=215, y=185)
artist_group_name_text.place(x=215, y=260)
artist_first_album_text.place(x=215, y=335)

album_name = StringVar(register_screen)
release_year = StringVar(register_screen)
artist_group_name = StringVar(register_screen)
artist_first_album = StringVar(register_screen)

album_name_entry = Entry(register_screen, textvariable=album_name, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "14", "bold"), relief="groove")
release_year_entry = Entry(register_screen, textvariable=release_year, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "14", "bold"), relief="groove")
artist_group_name_entry = Entry(register_screen, textvariable=artist_group_name, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "14", "bold"), relief="groove")
artist_first_album_entry = Entry(register_screen, textvariable=artist_first_album, width='15', bg='white', fg='black', bd=3, font=(
    "Roboto", "14", "bold"), relief="groove")

album_name_entry.place(x=215, y=130, height='30')
release_year_entry.place(x=215, y=205, height='30')
artist_group_name_entry.place(x=215, y=280, height='30')
artist_first_album_entry.place(x=215, y=355, height='30')

register = Button(register_screen, text='Cadastrar Álbum', width='13', bg='#6BACBF', fg='black', bd=3, font=(
    "Roboto", "13", "bold"), cursor="hand2", command=save_info)
register.place(x=230, y=430)


lbl = Label(register_screen, bg='#6BACBF', wraplength=250, width=30)
lbl.place(x=160, y=480)
"Fim tela cadastro"

"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

"Tela de álbuns"

lbl2 = Label(list_album_screen, bg='#6BACBF', wraplength=250, width=30)
lbl2.place(x=160, y=480)

"Fim tela álbuns"
"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

heading(home_screen)
heading(register_screen)
heading(list_album_screen)


button_home(register_screen, "Voltar", back_to_home)
button_home(list_album_screen, "Voltar", back_to_home)
button_home(home_screen, "Voltar", back_to_start)


screen_conf.pack(fill=BOTH, expand=True)
screen.mainloop()
