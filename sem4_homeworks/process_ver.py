import multiprocessing
from pathlib import Path
from time import time
import click

import requests

download_dir = Path(Path.cwd(), 'download', 'process')
if not download_dir.is_dir():
    download_dir.mkdir(parents=True, exist_ok=True)
start_time = time()


def download_image(url):
    file_name = url.split('?')[0].split('/')[-1]
    result = requests.get(url)
    if result.status_code == 200:
        with open(Path(download_dir, file_name), 'wb') as f:
            f.write(result.content)
    else:
        print(f'Возникла ошибка {result.status_code} в процессе загрузки файла по ссылке {url}')


def is_valid_data(file, url):
    if file is None and len(url) < 1:
        raise RuntimeError("Требуется указать данные для скачивания")


def get_list_urls(data):
    if isinstance(data, str) and Path(data).is_file():
        with open(data, 'r', encoding='utf-8') as f:
            return [url.strip() for url in f.readlines() if url.strip().startswith('http')]
    if isinstance(data, tuple) and len(data) > 0 and isinstance(data[0], str):
        return [url.strip() for url in data if url.strip().startswith('http')]
    if isinstance(data, str) and data.startswith('http'):
        return [data]


def main(urls):
    processes = []
    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url.strip(),))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Download complete! Total time for {len(processes)} equal: {time() - start_time:0.2f} seconds')


@click.command()
@click.option('--file', help='Путь к файлу с URL адресами')
@click.option('--url', multiple=True, help='Указать URL адрес, если их несколько, \
то ключ указывается перед каждым адресом')
def run(file=None, url=None):
    """
    Загружает файлы из интернета по полученным адресам. Список адресов можно передать файлом или отдельными строками
    """
    try:
        is_valid_data(file, url)
    except RuntimeError as err:
        print(f'{err}. Запустите с ключом --help для подробностей')
        return -1
    urls = []
    if file is not None:
        urls += get_list_urls(file)
    if url is not None and len(url) > 0:
        urls += get_list_urls(url)
    main(urls)


if __name__ == '__main__':
    run()
