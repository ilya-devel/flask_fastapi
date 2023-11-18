import multiprocessing

counter = 0


def increment(name):
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f'Counter equal by {name}: {counter}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'\nAll threads completed work, counter equal: {counter}')
