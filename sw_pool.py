import json
from datetime import datetime, time

with open('pools.json', encoding='utf-8') as file_in:
    data = json.load(file_in)
    right_pool = [0, 0, 'adr']
    for d in data:
        monday_time = d["WorkingHoursSummer"].get("Понедельник").split('-') # Если есть занятия в понедельник, то
        if monday_time:
            hour_s, minute_s = monday_time[0].split(':')
            my_time_s = time(int(hour_s), int(minute_s)) # Время открытия в понедельник
            hour_e, minute_e = monday_time[1].split(':')
            my_time_e = time(int(hour_e), int(minute_e)) # Время закрытия в понедельник
            if my_time_s <= time(hour=10, minute=0) and my_time_e >= time(hour=12, minute=0):
                size_l = d["DimensionsSummer"]["Length"]
                size_w = d["DimensionsSummer"]["Width"]
                address = d["Address"]
                if size_l > right_pool[0]:
                    right_pool = [size_l, size_w, address]
                elif size_l == right_pool[0]:
                    if size_w > right_pool[1]:
                        right_pool = [size_l, size_w, address]
    print(f'{right_pool[0]}x{right_pool[1]}')
    print(right_pool[2])