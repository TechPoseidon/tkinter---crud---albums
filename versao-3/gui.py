from tkinter import *
from tkinter import ttk
from domain import *


def start_screen():
    global screen
    global screen_conf
    global screen_conf_button
    screen = Tk()
    screen.title("Álbum de Música")
    screen.geometry('600x700')
    screen.configure(bg='#6BACBF')
    screen.resizable(False, False)
    nothing_registered_screen()
    albums_registered_screen()
    screen_conf = Label(screen, height='2',  bg='#6BACBF')
    screen_conf_button = Button(screen_conf, text='Albúm de Música', fg='black', font=(
        "Roboto", "20", "bold"), bg='#6BACBF', cursor="hand2", relief='flat', activeforeground="white", command=lambda: go_to_home(screen_conf, list_album_screen,
                                                                                                                                   none_album, register_screen, home_screen, lbl, artist_first_album_r1, artist_first_album_r2))
    screen_conf_button.place(x='173', y='316')

    return screen, screen_conf


def main_screen():
    global register_button
    global list_album_button
    global search_main_button
    global home_screen
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


def register_screen():
    global register
    global register_screen
    global lbl
    global album_name_text
    global album_name
    global album_name_entry
    global release_year_text
    global release_year
    global release_year_entry
    global artist_group_name_text
    global artist_group_name
    global artist_group_name_entry
    global artist_first_album_text
    global artist_first_album_r1
    global artist_first_album_r2
    global buttom_variable

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


def nothing_registered_screen():
    global none_album
    global label
    none_album = Frame(screen)
    none_album.configure(bg='#6BACBF')
    label = Label(none_album, bg='#6BACBF', text="Nenhum álbum cadastrado", fg='black', bd=2, font=(
        "Roboto", "15", "bold"))
    label.place(x="190", y="200")
    return none_album


def albums_registered_screen():
    global columns
    global list_album_screen
    global scrollbar
    global style
    columns = ("id", 'album_name', 'release_year',
               'artist_group_name', 'artist_first_album')

    list_album_screen = ttk.Treeview(screen, columns=columns, show='headings')

    list_album_screen.column("id", minwidth="25", width="10",
                             anchor=CENTER)
    list_album_screen.column("album_name", minwidth="50", width="50", anchor=W)
    list_album_screen.column(
        "release_year", minwidth="50", width="50", anchor=W)
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
    return list_album_screen


def albums_data_by_artist():
    global search_artist
    global box_name
    global lbl3
    global list_box_name
    global scrollbar_box_name
    global style_box_name
    global box_name_button
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
    list_box_name.configure(yscroll=scrollbar_box_name.set)

    style_box_name = ttk.Style()
    style_box_name.configure("Treeview", foreground="black", background="#6BACBF",
                             rowheight=30, fieldbackground="#6BACBF")
    style_box_name.map("Treeview", background=[
        ('selected', "#4edae4")], foreground=[('selected', "black")])

    box_name_button = Button(search_artist, text="Pesquisar",
                             width='8', bg="#6BACBF", fg='black', cursor="hand2", font=("Roboto", "9", "bold"), command=search_artist_func, relief="solid", activebackground="aqua", activeforeground="white")
    box_name_button.place(x=335, y=319)


def main_search_screen():
    global subscreen
    global search_artist_button
    global search_year_button
    subscreen = Frame(screen)
    subscreen.configure(background="#6BACBF")

    search_artist_button = Button(subscreen, text="Por Artista",  width='20',
                                  bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_search_artist_name, relief="solid", activebackground="#4edae4", activeforeground="white")
    search_artist_button.place(x=180, y=130)

    search_year_button = Button(subscreen, text="Por Ano",  width='20',
                                bg='#6BACBF', fg='black', bd=3, font=("Roboto", "14", "bold"), cursor="hand2",  command=load_search_year, relief="solid", activebackground="#4edae4", activeforeground="white")
    search_year_button.place(x=180, y=180)


def albums_data_by_year():
    global search_year
    global lbl4
    global list_box_year
    global scrollbar_box_year
    global style_box_year
    global box_year
    global box_year_button
    global radio_ano
    global box_r1
    global box_r2
    global box_r3
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

    radio_ano = IntVar()
    box_r1 = Radiobutton(search_year, variable=radio_ano, width='8', text="Anterior a", font=("Roboto", "10"), cursor="hand2",
                         bg='#6BACBF', fg='black', bd=2, relief="groove", value=1, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
    box_r2 = Radiobutton(search_year, variable=radio_ano, width='8', text="Igual a", font=("Roboto", "10"), cursor="hand2",
                         bg='#6BACBF', fg='black', bd=2, relief="groove", value=2, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
    box_r3 = Radiobutton(search_year, variable=radio_ano, width='8', text="Posterior a", font=("Roboto", "10"), cursor="hand2",
                         bg='#6BACBF', fg='black', bd=2, relief="groove", value=3, selectcolor="white", highlightcolor="white", activebackground="#4edae4", activeforeground="white")
    box_r1.place(x=140, y=260)
    box_r2.place(x=255, y=260)
    box_r3.place(x=370, y=260)


def screen_head_configurations():
    head(home_screen, "Álbum de Música", 197)
    head(register_screen, "Cadastrar Álbum", 197)
    head(subscreen, "Buscar Álbum", 215)
    head(search_artist, "Buscar Por Artista", 197)
    head(search_year, "Buscar Por Ano", 197)


def screen_button_configurations():
    button_home(register_screen, "Voltar", back_to_home,
                260, 600, "#6BACBF", "#4edae4")
    button_home(list_album_screen, "Voltar", back_to_home,
                510, 655, "#4edae4", "#6BACBF")
    button_home(list_album_screen, "Remover", delete_treeview_register,
                510, 625, "#4edae4", "#6BACBF")
    button_home(none_album, "Voltar", back_to_home,
                260, 600, "#6BACBF", "#4edae4")

    button_home(home_screen, "Voltar", back_to_start,
                260, 600, "#6BACBF", "#4edae4")
    button_home(search_artist, "Voltar", load_subscreen,
                260, 600, "#6BACBF", "#4edae4")
    button_home(search_year, "Voltar", load_subscreen,
                260, 600, "#6BACBF", "#4edae4")
    button_home(list_box_name, "Voltar", back_to_search_artist,
                510, 655, "#4edae4", "#6BACBF")
    button_home(list_box_name, "Remover", delete_treeview_register,
                510, 625, "#4edae4", "#6BACBF")
    button_home(list_box_year, "Voltar", back_to_search_year,
                510, 655, "#4edae4", "#6BACBF")
    button_home(list_box_year, "Remover", delete_treeview_register,
                510, 625, "#4edae4", "#6BACBF")
    button_home(subscreen, "Voltar", back_to_home,
                260, 600, "#6BACBF", "#4edae4")


def __main__():
    start_screen()
    screen_conf.pack(fill=BOTH, expand=True)
    screen.mainloop()


__main__()
