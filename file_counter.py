from zipfile import ZipFile

with ZipFile('workbook.zip') as zp_file:
    info = zp_file.infolist()
    answer = len([x for i, x in enumerate(info) if info[i].is_dir() == False])
    zp_file.printdir()