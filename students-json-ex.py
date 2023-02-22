import csv
import json

with open('students.json', encoding='utf-8') as file_in, open('data.csv', 'w', encoding='utf-8', newline='') as file_out:
    data = json.load(file_in)
    columns = ['name', 'phone']
    writer = csv.writer(file_out)
    writer.writerow(columns)
    out_list = []
    for d in data:
        if d["age"] >= 18 and d["progress"] >= 75:
            out_list.append([d["name"], d["phone"]])
    out_list.sort()
    writer.writerows(out_list)