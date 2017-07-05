import asyncio

async def countdown(name: str, secs: int) -> None:
    n = secs
    while n > 0:
        print(f'{name}: {n}')
        n -= 1
        await asyncio.sleep(0.5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        countdown('A', 4),
        countdown('B', 5),
        countdown('C', 2),
    ]))

    loop.run_until_complete(asyncio.wait([
        countdown('D', 4),
        countdown('E', 5),
        countdown('F', 2),
    ]))

    loop.run_until_complete(asyncio.wait([
        countdown('G', 4),
        countdown('H', 5),
        countdown('I', 2),
    ]))
    loop.close()

