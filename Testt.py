import json

with open('data.json', 'r', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8', newline='') as w_file:
    data = json.load(file)
    out_list = []
    for d in data:
        if type(d) == str:
            out_list.append(f'{d}!')
        elif type(d) == int or type(d) == float:
            out_list.append(d + 1)
        elif type(d) == bool:
            out_list.append(not d)
        elif type(d) == list:
            out_list.append(d * 2)
        elif type(d) == dict:
            d['newkey'] = None
            out_list.append(d)
        elif type(d) == None:
            continue
    json.dump(out_list, w_file)