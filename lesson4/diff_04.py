import time
from pathlib import Path
import asyncio
import aiohttp

urls = [
    'https://t.me/python3k',
    'https://www.youtube.com/channel/UCQ1YbfMA6jeGamfA1RHMWHQ',
    'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
    'https://docs.python.org/3/library/asyncio.html',
    'https://habr.com/ru/articles/671602/',
]

path_download = Path(Path.cwd(), 'downloaded')
if not path_download.is_dir():
    path_download.mkdir(parents=True, exist_ok=True)


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'async_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            file_path = Path(path_download, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
