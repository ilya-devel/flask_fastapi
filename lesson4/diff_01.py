import requests
import time
from pathlib import Path

urls = [
    'https://t.me/python3k',
    'https://www.youtube.com/channel/UCQ1YbfMA6jeGamfA1RHMWHQ',
    'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
    'https://docs.python.org/3/library/asyncio.html',
    'https://habr.com/ru/articles/671602/',
]

start_time = time.time()

if __name__ == '__main__':
    path_download = Path(Path.cwd(), 'downloaded')
    if not path_download.is_dir():
        path_download.mkdir(parents=True, exist_ok=True)
    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
        file_path = Path(path_download, filename)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')
