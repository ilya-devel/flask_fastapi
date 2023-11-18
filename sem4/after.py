import os
import concurrent.futures

PATH = 'data'

def parser_url(filename):
    with open(filename, "r", encoding="utf-8") as f:
        count_words = len(f.read().split())
        print(count_words)

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        file_paths = [os.path.join(root, file_name) for root, dirs, files in os.walk(PATH) for file_name in files]
        executor.map(parser_url, file_paths)