def analyze_text_file(input_filename="input.txt", output_filename="statistics.txt"):
    """
    Читает текстовый файл, подсчитывает количество строк и слов,
    и записывает результат в другой файл.

    Args:
        input_filename (str): Имя входного текстового файла.
        output_filename (str): Имя выходного файла для записи статистики.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        num_lines = len(lines)
        num_words = 0
        for line in lines:
            # Разбиваем строку на слова, используя пробельные символы как разделители
            words_in_line = line.split()
            num_words += len(words_in_line)

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(f"Количество строк: {num_lines}\n")
            outfile.write(f"Количество слов: {num_words}\n")

        print(f"Анализ файла '{input_filename}' завершен.")
        print(f"Результаты записаны в файл '{output_filename}'.")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    # Создадим пример входного файла для демонстрации
    try:
        with open("../resource/input.txt", "w", encoding="utf-8") as f:
            f.write("Это первая строка.\n")
            f.write("А это вторая строка, содержащая несколько слов.\n")
            f.write("Третья строка.\n")
            f.write("\n") # Пустая строка
            f.write("Еще одна строка с разными словами и числами 123.\n")
    except Exception as e:
        print(f"Не удалось создать пример файла 'input.txt': {e}")
        exit() # Выходим, если не можем создать входной файл

    analyze_text_file()