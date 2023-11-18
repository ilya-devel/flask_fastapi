import random
import time


def long_running_task():
    for i in range(5):
        print(f'Running task {i}')
        time.sleep(random.randint(1, 3))


def main():
    print('Run app')
    long_running_task()
    print('Finish app')


if __name__ == '__main__':
    main()