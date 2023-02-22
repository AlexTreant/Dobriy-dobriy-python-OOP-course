import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    dict_district = {}
    dict_market_series = {}
    for d in data:
        district = d['District']
        name = d['OperatingCompany']
        dict_district[district] = dict_district.get(district, 0) + 1
        if d["IsNetObject"] == "да":
            dict_market_series[name] = dict_market_series.get(name, 0) + 1
    district = sorted(dict_district.items(), key=lambda x: x[1])[-1]
    market = sorted(dict_market_series.items(), key=lambda x: x[1])[-1]
    print(f'{district[0]}: {district[1]}')
    print(f'{market[0]}: {market[1]}')