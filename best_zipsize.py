from zipfile import ZipFile

with ZipFile('workbook.zip') as zp_file:
    info = zp_file.infolist()
    answer = ['name', 0]
    for i in range(len(info)):
        if not info[i].is_dir():
            filename = info[i].filename.split('/')[-1]
            k = (info[i].compress_size/info[i].file_size)*100
            if k > answer[1]:
                answer = [filename, k]
    print(answer)