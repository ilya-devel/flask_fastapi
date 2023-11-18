from pathlib import Path
from time import time
import click
import asyncio
import aiohttp

download_dir = Path(Path.cwd(), 'download', 'async')
if not download_dir.is_dir():
    download_dir.mkdir(parents=True, exist_ok=True)
start_time = time()


async def download_image(url):
    file_name = url.split('?')[0].split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as result:
            if result.status == 200:
                with open(Path(download_dir, file_name), 'wb') as f:
                    f.write(await result.read())
            else:
                print(f'Возникла ошибка {result.status} в процессе загрузки файла по ссылке {url}')


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


async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

    print(f'Download complete! Total time for {len(tasks)} equal: {time() - start_time:0.2f} seconds')


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
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))


if __name__ == '__main__':
    run()
