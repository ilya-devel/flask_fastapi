import multiprocessing

counter = multiprocessing.Value('i', 0)


def increment(cnt, name):
    for _ in range(1_000_000):
        with cnt.get_lock():
            cnt.value += 1
    print(f'Counter equal by {name}: {cnt.value:_}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter, i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'\nAll threads completed work, counter equal: {counter}')
