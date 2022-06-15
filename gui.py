from tkinter import *
from tkinter import ttk
from domain import *


def main():
    global bgcolor, cursor, activebgcolor

    bgcolor = "#6BACBF"
    cursor = "hand2"
    activebgcolor = "#4edae4"

    class_screen = screen()
    class_screen.mainloop()


def screen():
    global class_screen, class_screen_button, screen_width, screen_height, app_width, app_height

    class_screen = Tk()
    screen_width = class_screen.winfo_screenwidth()
    screen_height = class_screen.winfo_screenheight()

    app_width = str(int(31.62 * (screen_width//100)))
    app_height = str(int(70 * (screen_height//100)))

    x = int((int(screen_width) / 2) - (int(app_width) / 2))
    y = int((int(screen_height) / 2) - (int(app_height) / 2))

    class_screen.title("Álbum de Música")
    class_screen.geometry(f'{app_width}x{app_height}+{x}+{y}')
    class_screen.configure(bg=bgcolor)
    class_screen.resizable(True, True)

    class_screen_button = Button(class_screen, text='Albúm de Música', fg='black', font=(
        "Roboto", "20", "bold"), bg=bgcolor, cursor=cursor, relief='flat', activebackground=bgcolor, activeforeground="black", command=lambda: navigation(class_screen_button, home_screen(), 0))
    class_screen_button.pack(pady=int(app_height)/2.215)

    return class_screen


def home_screen():
    global home_frame
    home_frame = Frame(class_screen, bg=bgcolor)

    head(home_frame, "Álbum de Música")

    new_album_buttom = Button(home_frame, text="Novo Albúm",  width=int(int(app_width)/23),
                              bg=bgcolor, fg='black', bd=3, font=("Roboto", "14", "bold"), cursor=cursor,  command=lambda: navigation(home_frame, register_screen(), 0), relief="solid", activebackground=activebgcolor, activeforeground="white")
    new_album_buttom.pack(pady=int(app_height)/70)

    my_albums_buttom = Button(home_frame, text="Meus Albúms",  width=int(int(app_width)/23),
                              bg=bgcolor, fg='black', bd=3, font=("Roboto", "14", "bold"), cursor=cursor, command=lambda: verify_none(home_frame, none_album_screen(0), list_albums_screen(0, 0, 0)), relief="solid", activebackground=activebgcolor, activeforeground="white")
    my_albums_buttom.pack(pady=int(app_height)/70)

    search_albums_buttom = Button(home_frame, text="Buscar Albúm",  width=int(int(app_width)/23),
                                  bg=bgcolor, fg='black', bd=3, font=("Roboto", "14", "bold"), cursor=cursor,  command=lambda: verify_none(home_frame, none_album_screen(1), main_search_screen()), relief="solid", activebackground=activebgcolor, activeforeground="white")
    search_albums_buttom.pack(pady=int(app_height)/70)

    buttom_style(home_frame, "Voltar", lambda: navigation(
        home_frame, class_screen_button, app_height), app_height, 7, bgcolor, activebgcolor)
    return home_frame


def register_screen():
    global register_frame, buttom_r

    register_frame = Frame(class_screen, bg=bgcolor)
    head(register_frame, "Cadastrar Álbum")

    album_name = StringVar(register_frame)
    release_year = IntVar(register_frame)
    artist_group_name = StringVar(register_frame)
    buttom_r = StringVar()

    album_name_text = Label(register_frame, text='Nome do Álbum', bd='1', bg=bgcolor,
                            fg='black', font=("Roboto", "11", "bold"))
    album_name_text.pack(pady=int(app_height)/140)

    album_name_entry = Entry(register_frame, textvariable=album_name, width='15', bg='white', fg='black', bd=3, font=(
        "Roboto", "11"), relief="groove")
    album_name_entry.pack(pady=int(app_height)/140)

    release_year_text = Label(register_frame, text='Ano de Lançamento', bd='1', bg=bgcolor,
                              fg='black', font=("Roboto", "11", "bold"))
    release_year_text.pack(pady=int(app_height)/140)

    release_year_entry = Entry(register_frame, textvariable=release_year, width='15', bg='white', fg='black', bd=3, font=(
        "Roboto", "11"), relief="groove")
    release_year_entry.pack(pady=int(app_height)/140)

    artist_group_name_text = Label(register_frame, text='Nome da Banda', bd='1',
                                   bg=bgcolor, fg='black', font=("Roboto", "11", "bold"))
    artist_group_name_text.pack(pady=int(app_height)/140)

    artist_group_name_entry = Entry(register_frame, textvariable=artist_group_name, width='15', bg='white', fg='black', bd=3, font=(
        "Roboto", "11"), relief="groove")
    artist_group_name_entry.pack(pady=int(app_height)/140)

    artist_first_album_text = Label(register_frame, text='Primeiro Álbum do Artista',
                                    bd='1', bg=bgcolor, fg='black', font=("Roboto", "11", "bold"))
    artist_first_album_text.pack(pady=int(app_height)/140)

    artist_first_album_r1 = Radiobutton(register_frame, width='4', variable=buttom_r, text="Sim", font=("Roboto", "11"), cursor=cursor,
                                        bg=bgcolor, fg='black', bd=2, relief="groove", value="SIM", selectcolor="white", highlightcolor="white", activebackground=activebgcolor, activeforeground="white")
    artist_first_album_r2 = Radiobutton(register_frame, width='4', variable=buttom_r, text="Não", font=("Roboto", "11"), cursor=cursor,
                                        bg=bgcolor, fg='black', bd=2, relief="groove", value="NÃO", selectcolor="white", highlightcolor="white", activebackground=activebgcolor, activeforeground="white")

    artist_first_album_r1.pack(pady=int(app_height)/140)
    artist_first_album_r2.pack(pady=int(app_height)/140)

    album_name.set("Álbum")
    release_year.set("Ano")
    artist_group_name.set("Grupo ou Artista")
    artist_first_album_r1.select()

    register = Button(register_frame, text='Cadastrar', width='10   ', bg=bgcolor, fg='black', bd=2, font=(
        "Roboto", "13", "bold"), cursor=cursor, command=lambda: save_info(album_name, release_year, artist_group_name, buttom_r, lbl, artist_first_album_r1), activebackground=activebgcolor, activeforeground="white")
    register.pack(pady=int(app_height)/140)

    lbl = Label(register_frame, bg=bgcolor, wraplength=250, width=30)
    lbl.configure(text="")
    lbl.pack(pady=int(app_height)/140)

    buttom_style(register_frame, "Voltar", lambda: navigation(register_frame, home_frame, 0),
                 app_height, 350, bgcolor, activebgcolor)
    return register_frame


def none_album_screen(pick):
    global none_album_frame
    none_album_frame = Frame(class_screen)
    none_album_frame.configure(bg=bgcolor)
    label = Label(none_album_frame, bg=bgcolor, text="Nenhum álbum cadastrado", fg='black', bd=2, font=(
        "Roboto", "17", "bold"))

    if pick == 0:
        head(none_album_frame, "Meus Álbums")
    elif pick == 1:
        head(none_album_frame, "Buscar Álbum")
    label.pack(pady=int(app_height)/70)
    buttom_style(none_album_frame, "Voltar", lambda: navigation(
        none_album_frame, home_frame, 0), app_height, 7, bgcolor, activebgcolor)
    return none_album_frame


def list_albums_screen(pick, combobox, radio_year):
    columns = ("id", 'album_name', 'release_year',
               'artist_group_name', 'artist_first_album')
    global list_album_frame
    list_album_frame = ttk.Treeview(
        class_screen, columns=columns, show='headings')

    list_album_frame.column("id", minwidth="25", width="10",
                            anchor=CENTER)
    list_album_frame.column("album_name", minwidth="50", width="50", anchor=W)
    list_album_frame.column(
        "release_year", minwidth="50", width="50", anchor=W)
    list_album_frame.column(
        "artist_group_name", minwidth="80", width="50", anchor=W)
    list_album_frame.column("artist_first_album",
                            minwidth="50", width="50", anchor=W)

    list_album_frame.heading('id', text="ID", anchor=CENTER)
    list_album_frame.heading('album_name', text='Álbum', anchor=W)
    list_album_frame.heading('release_year', text='Ano', anchor=W)
    list_album_frame.heading(
        'artist_group_name', text='Artista/Grupo', anchor=W)
    list_album_frame.heading('artist_first_album',
                             text='Primeiro Álbum', anchor=W)

    scrollbar = ttk.Scrollbar(
        list_album_frame, orient=VERTICAL, command=list_album_frame.yview)
    list_album_frame.configure(yscroll=scrollbar.set)

    style = ttk.Style()

    style.configure("Treeview", foreground="black", background=bgcolor,
                    rowheight=30, fieldbackground=bgcolor)
    style.map("Treeview", background=[
        ('selected', activebgcolor)], foreground=[('selected', "black")])
    buttom_style(list_album_frame, "Remover", lambda: delete_treeview_register(list_album_frame),
                 app_height, 200, activebgcolor, bgcolor)
    if pick != 0:
        buttom_style(list_album_frame, "Voltar", lambda: navigation(list_album_frame, search_by_frame, 0),
                     app_height, 200, activebgcolor, bgcolor)
    else:
        buttom_style(list_album_frame, "Voltar", lambda: navigation(list_album_frame, home_frame, 0),
                     app_height, 200, activebgcolor, bgcolor)
    catch_info(pick, list_album_frame, combobox, radio_year)
    return list_album_frame


def main_search_screen():
    global search_screen_frame
    search_screen_frame = Frame(class_screen)
    search_screen_frame.configure(background=bgcolor)
    head(search_screen_frame, "Buscar Álbum")

    search_artist_button = Button(search_screen_frame, text="Por Artista",  width='20',
                                  bg=bgcolor, fg='black', bd=3, font=("Roboto", "14", "bold"), cursor=cursor,  command=lambda: navigation(search_screen_frame, search_by_screen(0), 0), relief="solid", activebackground=activebgcolor, activeforeground="white")
    search_artist_button.pack(pady=int(app_height)/70)

    search_year_button = Button(search_screen_frame, text="Por Ano",  width='20',
                                bg=bgcolor, fg='black', bd=3, font=("Roboto", "14", "bold"), cursor=cursor,  command=lambda: navigation(search_screen_frame, search_by_screen(1), 0), relief="solid", activebackground=activebgcolor, activeforeground="white")
    search_year_button.pack(pady=int(app_height)/70)

    buttom_style(search_screen_frame, "Voltar", lambda: navigation(search_screen_frame, home_frame, 0),
                 app_height, 7, bgcolor, activebgcolor)
    return search_screen_frame


def search_by_screen(pick):
    global search_by_frame, lbl2
    search_by_frame = Frame(class_screen, bg=bgcolor)
    lbl2 = Label(search_by_frame,
                 bg=bgcolor, wraplength=250, width=30)

    if pick == 0:
        head(search_by_frame, "Buscar Por Artista")
        box_artist = ttk.Combobox(search_by_frame, values=catch_info(1, 0, 0, 0),
                                  width="13", font=("Roboto", "10", "bold"))
        box_artist.pack(pady=int(app_height)/70)
        box_artist_button = Button(search_by_frame, text="Pesquisar",
                                   width='8', bg=bgcolor, fg='black', cursor=cursor, font=("Roboto", "9", "bold"), command=lambda: search(pick, box_artist, lbl2, search_by_frame, list_albums_screen, 0), relief="solid", activebackground=activebgcolor, activeforeground="white")
        box_artist_button.pack(pady=int(app_height)/70)

    elif pick == 1:
        global radio_year
        radio_year = IntVar()
        head(search_by_frame, "Buscar Por Ano")
        box_r1 = Radiobutton(search_by_frame, variable=radio_year, width='8', text="Anterior a", font=("Roboto", "10"), cursor=cursor,
                             bg=bgcolor, fg='black', bd=2, relief="groove", value=1, selectcolor="white", highlightcolor="white", activebackground=activebgcolor, activeforeground="white")
        box_r2 = Radiobutton(search_by_frame, variable=radio_year, width='8', text="Igual a", font=("Roboto", "10"), cursor=cursor,
                             bg=bgcolor, fg='black', bd=2, relief="groove", value=2, selectcolor="white", highlightcolor="white", activebackground=activebgcolor, activeforeground="white")
        box_r3 = Radiobutton(search_by_frame, variable=radio_year, width='8', text="Posterior a", font=("Roboto", "10"), cursor=cursor,
                             bg=bgcolor, fg='black', bd=2, relief="groove", value=3, selectcolor="white", highlightcolor="white", activebackground=activebgcolor, activeforeground="white")
        box_r1.pack(pady=int(app_height)/70)
        box_r2.pack(pady=int(app_height)/70)
        box_r3.pack(pady=int(app_height)/70)
        box_r2.select()

        box_year = ttk.Combobox(
            search_by_frame, values=catch_info(2, 0, 0, 0), width="8", font=("Roboto", "11", "bold"))
        box_year.pack(pady=int(app_height)/70)

        box_year_button = Button(search_by_frame, text="Pesquisar",
                                 width='8', bg=bgcolor, fg='black', cursor=cursor, font=("Roboto", "9", "bold"), command=lambda: search(pick, box_year, lbl2, search_by_frame, list_albums_screen, radio_year), relief="solid", activebackground=activebgcolor, activeforeground="white")
        box_year_button.pack(pady=int(app_height)/70)

    lbl2.pack(pady=int(app_height)/70)
    buttom_style(search_by_frame, "Voltar", lambda: navigation(search_by_frame, search_screen_frame, 0),
                 app_height, 15, bgcolor, activebgcolor)
    return search_by_frame


main()
