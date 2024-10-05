# Чтение и запись из/в хранилище (база данных)
import json


def ReadFilmsFromDB() -> list:
    global DATA_BASE_FILE_NAME
    data = ""
    with open("films.txt", "r", encoding="utf-8") as file:
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

def ReadFilmsFromJsonFile(file_name : str) -> any:
    with open(file_name, 'r', encoding='utf-8') as file:
       return json.load(file)
    pass


def WriteFilmsInJsonFile(file_name : str, films : any) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(films, file, ensure_ascii=False, indent=4)
    pass
            

if __name__ == "__main__":
    data = ReadFilmsFromDB()
    normal_data = []
    for f in data:
        if len(f) != 3:
            continue
        film_dict = dict()
        film_dict["name"] = f[0]
        film_dict["fanre"] = f[1]
        film_dict["rating"] = int(f[2])
        normal_data.append(film_dict)
    print(data) 
    print()
    print(normal_data)
    WriteFilmsInJsonFile("films.json", normal_data)