import matplotlib.pyplot as plt
import json
from matplotlib.ticker import AutoMinorLocator, FixedLocator

def get_data_plot():
    with open('my_studie_file.json', encoding='utf-8') as fl:
        data = json.load(fl)
        return data

def data_plot():
    data = get_data_plot()
    x_list = []
    y_list = []
    for k, v in data.items():
        x_list.append(k)
        y = sum(v.values())
        y_list.append(y)
    return x_list, y_list

plt.figure(figsize=(15, 40))
plt.title("График моей учёбы", fontsize=14, fontweight='bold', color='red')
plt.xlabel('Календарь', fontsize=12, fontweight='bold', color='black')
plt.ylabel('Время учёбы', fontsize=12, fontweight='bold', color='black')
plt.barh(*data_plot(), label='Моё обучение')

plt.legend()
plt.grid()
plt.savefig('test_saved_figure.png')
# plt.show()