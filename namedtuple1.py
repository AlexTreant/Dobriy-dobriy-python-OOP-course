from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
    for k in obj:
        name, family, sex, color = k
        print(f'name: {name}')
        print(f'family: {family}')
        print(f'sex: {sex}')
        print(f'color: {color}')
        print()
