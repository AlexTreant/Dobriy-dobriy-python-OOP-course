import csv
from datetime import datetime

with open('name_log.csv', 'r', encoding='utf-8') as file, open('new_name_log.csv', 'w', encoding='utf-8', newline='') as w_file:
    row = list(csv.reader(file))
    columns = row[0]
    d = {}
    for r in row[1:]:
        key = r[1]
        value = r[0]
        date = datetime.strptime(r[2], '%d/%m/%Y %H:%M')
        if key not in d:
            d[key] = [value, date]
        else:
            if date > d[key][1]:
                d[key][0] = value
                d[key][1] = date
    d_srt = sorted(d.items(), key=lambda x: x[0])
    writer = csv.writer(w_file)
    writer.writerow(columns)
    for i in d_srt:
        lst = [i[1][0], i[0], i[1][1].strftime('%d/%m/%Y %H:%M')]
        writer.writerow(lst)