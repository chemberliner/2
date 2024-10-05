import database


def print_title() -> None:
    title = "|{:<22}|{:<14}|{:<9}|".format("Название", "Жанр", "Рейтинг")
    print(f"+{'':-<22}+{'':-<14}+{'':-<9}+")
    print(title)
    print(f"+{'':-<22}+{'':-<14}+{'':-<9}+")


def print_format_film(film : list) -> None:
    f = "{:<25}{:<15}{:<10}".format(film[0].capitalize(), film[1].capitalize(), film[2])
    print(f)


def print_all_films(films_arg):
    print_title()
    for f in films_arg:
        print_format_film(f)


def print_films_by_rating(films : list) -> None:
    rating = int(input('Введите рейтинг:'))
    print_title()
    res_films = [f for f in films if int(f[2]) >= rating ]
    res_films.sort(key=lambda f : int(f[2]), reverse=True)
    for f in res_films:
        print_format_film(f)


def print_films_by_genre(films : list) -> None:
    genre = input("Введите жанр фильма:").strip()
    genre = genre.lower()
    print_title()
    for f in films:
        if f[1].lower().strip() == genre:
            print_format_film(f)


def logo():
    print('''

          
            ██████╗ ██╗███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
            ██╔══██╗██║████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
            ██████╔╝██║██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝ 
            ██╔═══╝ ██║██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗ 
            ██║     ██║██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
            ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝                

                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⣠⣴⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣵⣄⠀⠀⠀
                        ⠀⠀⢾⣻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡀⠀
                        ⠀⠸⣽⣻⠃⣿⡿⠋⣉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣏⡟⠉⡉⢻⣿⡌⣿⣳⡥⠀
                        ⠀⢜⣳⡟⢸⣿⣷⣄⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣠⣼⣿⣇⢸⢧⢣⠀
                        ⠀⠨⢳⠇⣸⣿⣿⢿⣿⣿⣿⣿⡿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡟⢆⠀
                        ⠀⠀⠈⠀⣾⣿⣿⣼⣿⣿⣿⣿⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣽⣿⣿⠐⠈⠀⠀
                        ⠀⢀⣀⣼⣷⣭⣛⣯⡝⠿⢿⣛⣋⣤⣤⣀⣉⣛⣻⡿⢟⣵⣟⣯⣶⣿⣄⡀⠀
                        ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣶⣶⣴⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿⣧
                        ⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⡿
          
                    ''')


def read_command():
    cmd = -1
    print()
    print("Доступные команды:")
    commands = [
        "Вывести все фильмы",
        "Вывести фильмы по жанру",
        "Вывести фильмы по рейтингу",
        "Записать фильмы в файл",
        "Добавить фильм",
        "Выйти"
    ]
    for i in range(len(commands)):
        print(f"{i + 1}. {commands[i]}")
    while True:
        try:
            cmd = int(input("Введите команду:"))
            if 1 <= cmd <= len(commands):
                break
            else:
                print("[ERROR] Неизвестная команда")
        except:
            print("[ERROR] Введите число")
        
    return cmd


def read_film() -> list:
    film_name = input("Введите название фильма:")
    film_genre = input("Введите жанр фильма:")
    r = -1
    while True:
        try:
            r = int(input("Введите рейтинг фильма (от 1 до 10):"))
            if 1 <= r <= 10:
                break
            else:
                print("Рейтинг должен быть от 0 до 10")
        except:
            print("[ERROR] Введите число")
    return [film_name, film_genre, r]


def main(films):
    logo()

    while True:
        cmd = read_command()
        if cmd == 1: # Вывести все фильмы
            #print(films)
            print_all_films(films)
        elif cmd == 2: # Вывести фильмы по жанру
           print_films_by_genre(films)
        elif cmd == 3: # Вывести фильмы по рейтингу
           print_films_by_rating(films)
        elif cmd == 4: # Запись в файл
            database.WriteFilmsInJsonFile(films, 'temp.json')
        elif cmd == 5: # Добавить фильм
            films.append(read_film())   
        elif cmd == 6: # Выйти
            break
        else:
            print(f"[!] Команда '{cmd}' не существует")
    pass



if __name__ == "__main__":
    films = database.ReadFilmsFromJsonFile("films.json")
    main(films)
