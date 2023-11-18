"""
Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
Используйте процессы
"""
import os
import multiprocessing
from pathlib import Path

file_dir = Path(Path.cwd(), 'downloaded')


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f'Количество слов в файле {str(file_path).split("/")[-1]} равно: {len(f.read().split())}')


if __name__ == '__main__':
    processes = []
    for file in os.listdir(file_dir):
        if Path(file_dir, file).is_file():
            process = multiprocessing.Process(target=count_words, args=(Path(file_dir, file),))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()
