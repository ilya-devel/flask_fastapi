import asyncio


async def count():
    print('Start running')
    await asyncio.sleep(1)
    print('Get out 1 second')
    await asyncio.sleep(2)
    print('Get out 2 seconds too')
    return 'Complete'


async def main():
    result = await asyncio.gather(count(), count(), count())
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
