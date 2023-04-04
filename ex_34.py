import csv
import json


def show_sum(rows, price):
    s = 0
    for i in rows:
        key = i[0]
        s += sum([int(x) for x in i[1:]]) * price[key]
    return s


with open('quarter1.csv', 'r', encoding='utf-8') as file1, open('quarter2.csv', 'r', encoding='utf-8') as file2, open('quarter3.csv', 'r', encoding='utf-8') as file3, open('quarter4.csv', 'r', encoding='utf-8') as file4, open('prices.json', 'r', encoding='utf-8') as file_json:
    files = [file1, file2, file3, file4]
    price = json.load(file_json)
    s = 0
    for f in files:
        rows = list(csv.reader(f))[1:]
        s += show_sum(rows, price)
    print(s)
