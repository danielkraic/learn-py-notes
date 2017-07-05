import asyncio

async def ola(msg, sec):
    print(f"Ola beg {msg}")
    await asyncio.sleep(sec)
    print(f"Ola end {msg}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait([
        ola("1", 1),
        ola("2", 2),
        ola("3", 3),
        ola("4", 2),
        ola("5", 1)
    ]))
    loop.close()
