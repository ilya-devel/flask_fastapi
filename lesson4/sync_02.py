import time


def slow_func():
    print('Start func')
    time.sleep(5)
    print('Finish func')


if __name__ == '__main__':
    print('Start app')
    slow_func()
    print('Finish app')
