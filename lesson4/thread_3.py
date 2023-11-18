import threading

counter = 0


def increment(name):
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f'Counter equal by {name}: {counter}')


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=increment, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('All threads completed work')
