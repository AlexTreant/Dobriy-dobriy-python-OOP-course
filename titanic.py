import csv

with open('titanic.csv', 'r', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    male = []
    female = []
    for r in rows[1:]:
        if float(r[-1]) < 18 and int(r[0]) == 1:
            if r[-2] == 'male':
                male.append(r[1])
            elif r[-2] == 'female':
                female.append(r[1])
    print(*male, sep='\n')
    print(*female, sep='\n')