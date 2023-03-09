import json
from zipfile import ZipFile

def is_correct_json(string):
    answer = True
    try:
        json.loads(string)
    except ValueError:
        answer = False
    return answer

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    name_list = []
    for i, x in enumerate(info):
        path = info[i].filename # Строка - полный путь к файлу и название файла
        if not info[i].is_dir() and path[-5:] == '.json': # Если это файл json
            with zip_file.open(path) as file: # 
                s = file.read() # Словарь или абракадабра в формате json
                if is_correct_json(s):
                    data = json.loads(s)
                    if data['team'] == 'Arsenal':
                        name_list.append(f"{data['first_name']} {data['last_name']}")
    print(*sorted(name_list), sep='\n')