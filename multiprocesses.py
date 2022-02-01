from time import time
from datetime import datetime

from multiprocessing import Pool, cpu_count


NUM = 5 * (10**6)


def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


def test_no_pools():
    answer = 0
    for i in range(NUM):
        answer += if_prime(i)
    return answer


def test_with_pools(num=None):
    def inner():
        with Pool(num) as pool:
            return sum(pool.map(if_prime, list(range(NUM))))
    return inner


def measure_time(label, func):
    start = time()
    func()
    return label.ljust(10) + str(round(time() - start, 3)).rjust(7) + ' s.'


def main():
    report = [
        'CPU integer performance test.',
        'Function: if_prime().',
        'Input system name: ',
    ]

    system_name = input('\n'.join(report))
    report.append(system_name)
    
    tests = [
        test_no_pools,
        *[test_with_pools(n) for n in range(1, cpu_count() + 1)],
        test_with_pools(),
    ]

    tests = []
    for n in range(1, cpu_count() + 1):
        tests.append((f'Pool({n}):', test_with_pools(n)))

    tests.insert(0, ('Simple:', test_no_pools))
    tests.append(('Pool():', test_with_pools()))
    
    for label, func in tests:
        result = measure_time(label, func)
        report.append(result)
        print(result)

    ftime = datetime.now().strftime('%y%m%d-%H%M%S')
    with open(f'report_{system_name}_{ftime}.txt', 'w') as file:
        file.write('\n'.join(report) + '\n')


if __name__ == '__main__':
    main()
