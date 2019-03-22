import asyncio


async def print_hello():
    print("hello")


async def print_world():
    await asyncio.sleep(1)
    print("world")


async def print_from():
    await asyncio.sleep(2)
    print("from")


async def print_mandar():
    await asyncio.sleep(3)
    print("Mandar")


async def main():
    task_list = list()
    task_list.append(asyncio.create_task(print_mandar()))
    task_list.append(asyncio.create_task(print_from()))
    task_list.append(asyncio.create_task(print_world()))
    task_list.append(asyncio.create_task(print_hello()))

    # prints "hello world from Mandar", regardless of the sequence in list
    for item in task_list:
        await item

if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(asyncio.gather(main()))
