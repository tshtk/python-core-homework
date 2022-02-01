from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def inner_wrap(*args, **kwargs):
            total_time = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(f"duration of run #{i+1}: {end-start}\n")
                total_time += end - start
            print(f"average run time: {total_time/num}\n")
        return inner_wrap
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
