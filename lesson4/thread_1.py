import threading
import time


def worker(num):
    print(f'Start work of thread {num}')
    time.sleep(3)
    print(f'End work of thread {num}')


if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('All threads completed work')
