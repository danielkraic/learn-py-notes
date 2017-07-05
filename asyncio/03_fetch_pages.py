import asyncio
import aiohttp

async def fetch_page(url: str) -> None:
    print(f'fetching: {url}')

    res = await aiohttp.request(method='HEAD', url=url)
    print(f'url: {url}, status: {res.status}')

    data = await res.read()
    print('url: {}, data size: {}'.format(url, data))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        fetch_page('http://subway.som.sk'),
        fetch_page('http://skoncil.som.sk'),
        fetch_page('http://nasraty.som.sk'),
    ]))
    loop.close()
