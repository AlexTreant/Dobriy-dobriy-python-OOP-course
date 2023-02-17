import csv

with open('domains.csv', encoding='utf-8') as file, open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_out:
    rows = list(csv.reader(file))
    columns = ['domain', 'count']
    d = {}
    for r in rows[1:]:
        domain = r[-1][r[-1].index('@')+1:]
        d[domain] = d.get(domain, 0) + 1
    d_srt = sorted(d.items())
    writer = csv.writer(file_out)
    writer.writerow(columns)
    for i in sorted(d_srt, key=lambda x: x[1]):
        writer.writerow(i)