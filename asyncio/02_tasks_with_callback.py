import asyncio

async def ola(future: asyncio.Future, msg: str, sec: int) -> None:
    print(f"Ola beg {msg}")
    await asyncio.sleep(sec)
    print(f"Ola end {msg}")
    future.set_result(f'ola result {msg}')

def print_result(future: asyncio.Future) -> None:
    print('result: ', future.result())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    f1 = asyncio.Future()
    f2 = asyncio.Future()
    f3 = asyncio.Future()

    f1.add_done_callback(print_result)
    f2.add_done_callback(print_result)
    f3.add_done_callback(print_result)

    loop.run_until_complete(asyncio.wait([
        ola(f1, "1", 1),
        ola(f2, "2", 2),
        ola(f3, "3", 3),
    ]))
    loop.close()
