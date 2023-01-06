
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


def ex_3(s_in):
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
