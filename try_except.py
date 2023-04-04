import csv

try:
    with open('fgfgh', 'r', encoding='utf-8') as file:
        data = file.read()
        for i in data.split('\n'):
            print(i)
except:
    print('Файл не найден')