from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as file:
    info = file.infolist()
    d = []
    for i in range(len(info)):
        if not info[i].is_dir():
            name = info[i].filename.split('/')[-1]
            dt = datetime(*info[i].date_time)
            size = info[i].file_size
            compr_size = info[i].compress_size
            d.append([name, dt, size, compr_size])
    for i, k in enumerate(sorted(d, key=lambda x: x[0])):
        print(k[0])
        print(f"  Дата модификации файла: {k[1].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f'  Объем исходного файла: {k[2]} байт(а)')
        print(f'  Объем сжатого файла: {k[3]} байт(а)')
        if i != len(d) - 1:
            print()