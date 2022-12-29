'''
Подвиг 9. Из входного потока читаются строки данных с помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
добавить два метода:

select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно) по их индексам 
(не id, а индексам списка); также учесть, что граница b может превышать длину списка.
insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;

Каждая запись в списке lst_data должна быть представлена словарем в формате:

{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}

Например:

{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.

P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200

'''


# здесь объявите класс TriangleChecker
class TriangleChecker:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not all(map(lambda x: type(x) in (int, float), (a, b, c))):
            return 1
        if not all(map(lambda x: x > 0, (a, b, c))):
            return 1
        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        return 3

a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())