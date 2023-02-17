import pandas as pd

lst = [1, 34, 52, 23, 71, 66, 12, 22, 22, 98]
a = pd.Series(lst)
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(d.values(), index=d.keys())
print(a)
print(a.argmax())