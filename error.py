'''
Первая задача:
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит
обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset".
Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл
в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

'''
'''
Вторая задача:
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например,
на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и
через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для
строк).
В качестве ответа укажите вывод программы, а не саму программу.
Слова, написанные в разных регистрах, считаются одинаковыми.

'''
'''
Третья задача:
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём
предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом,
последней строкой в файл с ответом.

В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём
предметам.

'''



with open(r'C:\Users\AlexN\Desktop\Dobriy-dobriy-python-OOP\Dobriy-dobriy-python-OOP-course\dataset_3363_4.txt', encoding='utf-8') as input_s:
    s = input_s.read().lower()

work_space = s.split('\n')


def return_shifre(s_in): # Функция для первой задачи
    lst = []
    while len(s_in) > 0:
        x = s_in[0]
        s_in = s_in[1:]
        n = ''
        while s_in[0].isdigit():
            n += s_in[0]
            s_in = s_in[1:]
            if len(s_in) == 0:
                break
        lst.append(tuple([x, n]))
    s_out = ''
    for i in lst:
        s_out += i[0] * int(i[1])
    return s_out


def ret_str(s_in): # Функция для второй задачи
    workspace_2 = [x.lower() for x in ' '.join(work_space).split()]
    d = []
    while workspace_2:
        for_del = workspace_2[0]
        n = workspace_2.count(for_del)
        d.append((for_del, n))
        while for_del in workspace_2:
            workspace_2.remove(for_del)
    kostil = sorted(d, key=lambda x: x[1], reverse=True)
    x = kostil[0][1]
    output_list = [i[0] for i in kostil if i[1] == x]
    answer = sorted(output_list)[0]
    return answer, x


def ex_3(s_in): # Функция для третьей задачи
    lst_work = [[int(x) for x in i.split(';')[1:]] for i in s_in]
    midle = []
    for i in range(3):
        s = 0
        for j in range(len(lst_work)):
            s += lst_work[j][i]
        midle.append(str(s/len(lst_work)))
    kostil = []
    for i in lst_work:
        kostil.append(sum(i)/3)
    return kostil, midle

answr = ex_3(work_space)

with open(r'C:\Users\AlexN\Desktop\Dobriy-dobriy-python-OOP\Dobriy-dobriy-python-OOP-course\text_out.txt', 'w', encoding='utf-8') as output_s:
    for i in answr[0]:
        output_s.write(f'{i}\n')
    k = " ".join(answr[1])
    output_s.write(f'{k}\n')
# print(ret_str(work_space))
r"""
work_space_out = []
for i in work_space:
    work_space_out.append(return_shifre(i))

print(work_space_out)
with open(r'C:\Users\AlexN\Desktop\Dobriy-dobriy-python-OOP\Dobriy-dobriy-python-OOP-course\text_out.txt', 'w', encoding='utf-8') as output_s:
    for i in work_space_out:
        output_s.write(f'{i}\n')
"""
