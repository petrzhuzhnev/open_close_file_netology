#Необходимо объединить их в один по следующим правилам:
# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
with open('1.txt') as text_1, open('2.txt') as text_2, open('3.txt') as text_3, open('file.txt', 'w') as output_text:
    file_1 = '1.txt'
    file_2 = '2.txt'
    file_3 = '3.txt'
    file_4 = 'file.txt'
    dict_file = {
            text_1: [len(text_1.readlines()), file_1],
            text_2: [len(text_2.readlines()), file_2],
            text_3: [len(text_3.readlines()), file_3]
        }

    dict_file_sort = dict(sorted(dict_file.items(), key=lambda item: item[1][0]))


    for keys, values in dict_file_sort.items():
        output_text.writelines(f'{values[1]}\n')
        output_text.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            output_text.writelines(f'{line}')
        output_text.writelines('\n')
