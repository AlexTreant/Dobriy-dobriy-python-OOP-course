import csv

with open('salary_data.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    rows = sorted(rows[1:])
    d = {}
    for r in rows:
        if r[0] not in d:
            d[r[0]] = [int(r[1])]
        else:
            d[r[0]] += [int(r[1])]
    for company, salary in d.items():
        d[company] = sum(salary)/len(salary)
    sorted_d = sorted(d.items(), key=lambda i: i[1])
    for i in sorted_d:
        print(i[0])