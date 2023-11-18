"""
�Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
�Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
�Массив должен быть заполнен случайными целыми числами
от 1 до 100.
�При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
�В каждом решении нужно вывести время выполнения
вычислений.
"""
from random import randint
import asyncio
import time

count = 0

# main_lst = [randint(1, 101) for _ in range(1_000_000)]
main_lst = [i for i in range(1_000_000)]


async def increment(lst_num):
    global count
    for num in lst_num:
        count += num
    print(count)


async def main():
    lsts_nums = [main_lst[i:i + 100000] for i in range(10)]
    tasks = [asyncio.create_task(increment(lst)) for lst in lsts_nums]
    asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'All processes completed work. Time: {time.time() - start_time:0.02f} seconds')
