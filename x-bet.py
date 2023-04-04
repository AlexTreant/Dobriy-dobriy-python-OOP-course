import csv

with open('data_x_bet.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    next(line_values)
    true_values = (int(x[1]) for x in line_values if x[2] == 'a')
    print(sum(true_values))