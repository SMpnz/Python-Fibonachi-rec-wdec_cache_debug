import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        # 1 группа арг
        args_repr = [repr(a) for a in args]
        # 2 группа арг, использование !r -repr(object).__format__()
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"{wrapper_count_calls.num_calls}"
        f" вызов функции {func.__name__!r}({signature})") 
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} возвращает {value!r}")
        return value
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

def cache(func):
    """Кэширует предыдущие вызовы функции"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

def main():
    @cache #применение кеша дает возможность не высчитывать заново 
    #вызовы правой младшей половины формулы
    @count_calls #подсчет кол-ва вызовов функций 
    #и расчета значения - для наглядной оптимизации
    def fibonacci(num):
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)

    n=4
    print(f"Результат вызова функции поиск {n} числа Фибоначчи в последовательности: {fibonacci(n)}")

if __name__ == "__main__":
    main()