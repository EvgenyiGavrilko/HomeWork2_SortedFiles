files = ['1.txt', '2.txt', '3.txt']
dict_files = {}

for file in files:
    quantity_lines = 0
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            if line != 0:
                quantity_lines += 1
    #print(f'Название файла - {file.name} количество сторок - {quantity}') #КОД ДЛЯ ПРОВЕРКИ
    dict_files[file.name] = quantity_lines

dict_files_sorted = dict(sorted(dict_files.items(), key=lambda item: item[1]))
#print(dict_files) #КОД ДЛЯ ПРОВЕРКИ
#print(dict_files_sorted) #КОД ДЛЯ ПРОВЕРКИ


for file_name, quantity_lines in dict_files_sorted.items():
    with open(file_name, 'r', encoding='utf-8') as file:
        new_file = f'{file_name}\n{str(quantity_lines)}\n{file.read()}\n'
        with open('NEW.txt', 'a', encoding='utf-8') as file:
            file.write(new_file)











