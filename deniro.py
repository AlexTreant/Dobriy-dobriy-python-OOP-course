import csv
n = int(input())
with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file))
    for i, x in enumerate(rows):
        for j, y in enumerate(x):
            if y.isdigit():
                rows[i][j] = int(y)

    rows = sorted(rows, key=lambda i: i[n-1])
    for i in rows:
        print(*i, sep=',')
