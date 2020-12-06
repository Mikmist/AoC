data = ''
with open('./data') as f:
    for line in f.read().split(','):
        data += line.strip() + '\n'
        print(line.strip())

with open('./data_formatted', 'w') as f:
    f.write(data)

with open('./csv_list.csv') as f:
    for line in f.read().split('\n'):
        print(line.strip())

