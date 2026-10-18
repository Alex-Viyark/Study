# функция, которая перезаписывает содержимое питоновского файла, удаляя комментарии
def no_comments(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in lines:
            original = line.rstrip('\n')
            pos = original.find('#')
            if pos != -1:
                code_part = original[:pos]
                # Если после удаления комментария нет кода (только пробелы) – пропускаем
                if not code_part.strip():
                    continue
                f_out.write(code_part + '\n')
            else:
                # Строка без комментария – записываем (включая пустые)
                f_out.write(original + '\n')
# no_comments('tuple.py','tuple.py')
