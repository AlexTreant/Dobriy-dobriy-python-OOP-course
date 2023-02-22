import json
import csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as file_in, open('best_scores.json', 'w', encoding='utf-8') as file_out:
    rows = sorted(list(csv.reader(file_in))[1:], key=lambda x: x[-1])
    list_out = [{"name": '',"surname": '',"best_score": 0,"date_and_time": '',"email": ''}]
    for r in rows:
        d = {"name": r[0],"surname": r[1],"best_score": int(r[2]),"date_and_time": r[3],"email": r[4]}
        flag = True
        for i in list_out:
            if i['name'] == d['name'] and i['surname'] == d['surname'] and i["best_score"] < d["best_score"]:
                list_out.remove(i)
                list_out.append(d)
                flag = False
            elif i['name'] == d['name'] and i['surname'] == d['surname'] and i["best_score"] == d["best_score"]:
                i["date_and_time"] = d["date_and_time"] if datetime.strptime(d["date_and_time"], '%Y-%m-%d %H:%M:%S') > datetime.strptime(i["date_and_time"], '%Y-%m-%d %H:%M:%S') else i["date_and_time"]
                flag = False
            elif i['name'] == d['name'] and i['surname'] == d['surname'] and i["best_score"] > d["best_score"]:
                flag = False
        if flag:
            list_out.append(d)
    list_out = list_out[1:]
    json.dump(list_out, file_out)