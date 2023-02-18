import csv

with open('wifi.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    d = {}
    for r in rows[1:]:
        key = r[1]
        value = int(r[-1])
        d[r[1]] = d.get(key, 0) + value
    d_sort = sorted(d.items())
    d_sort_2 = sorted(d_sort, key = lambda x: x[1], reverse=True)
    for i in d_sort_2:
        print(f'{i[0]}: {i[1]}')