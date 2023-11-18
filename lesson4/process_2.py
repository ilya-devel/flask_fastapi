import multiprocessing
import time


def worker(num):
    print(f'Start work of process {num}')
    time.sleep(3)
    print(f'End work of process {num}')


if __name__ == '__main__':
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()
        p.join()

    print('All processes completed work')
