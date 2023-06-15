from datetime import datetime
import json

with open('studie_time.txt', 'r', encoding='utf-8') as file, open('my_studie_file.json', 'w', encoding='utf-8') as w_file:
    data = file.read().split('\n\n') # Получили список строк, где сначала дата-строка, потом временные промежутки
    d = {}
    for s in data:
        new_s = s.split('\n')
        dt = new_s[0][2:]
#        dt = datetime.strptime(new_s[0], '__%Y-%m-%d,%A') Дата не подходит для ключа словаря в json
        d_time = {}
        for t in new_s[:-1]:
            if t[0].isdigit():
                h, m = t.split(',')[2].split(':')
                all_t = int(h) * 60 + int(m)
                subj = t.split(',')[-1]
                d_time[subj] = d_time.get(subj, 0) + all_t
        d[dt] = d_time
    json.dump(d, w_file)