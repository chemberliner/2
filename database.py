# Чтение и запись из/в хранилище (база данных)

DATA_BASE_FILE_NAME = "films.txt"


def ReadFilmsFromDB() -> list:
    global DATA_BASE_FILE_NAME
    data = ""
    with open(DATA_BASE_FILE_NAME, "r", encoding="utf-8") as file:
        data = file.read()
    data = data.split("\n")
    data = [line for line in data if line != '']
    res = []
    for s in data:
        if "'" in s:
            s = s.split("'")
            a = s[2].split()
            a = [x for x in a if x != ""]
            s = [x for x in s if x != ""]
            ss = [s[0], a[0], a[1]]
            res.append(ss)
        else:
            res.append(s.split())
    return res
    



def WriteFilmsInDB(films : list) -> None:
    """
    Функция записывает список фильмов в текстовый файл
    films - двойной список
    """
    # global DATA_BASE_FILE_NAME
    
    res_file = "add_film.txt" # запись внутрь этого файла data в формате, как и в файле films.txt

    with open(res_file, 'w', encoding="utf-8") as file:
        for f in films: # каждая строка. общий список без кавычек. инфа про каждый фильм  
            film_str = ""
            if len(f[0].strip().split()) > 1:
                film_str = f"'{f[0]}' {f[1]} {f[2]}\n"
            else:
                film_str = f"{f[0]} {f[1]} {f[2]}\n"
            file.write(film_str)
    pass
            

if __name__ == "__main__":
    data = ReadFilmsFromDB()
    data.append(["Стражи галактики", "Комедия", "10"])
    print(data)
    WriteFilmsInDB(data)