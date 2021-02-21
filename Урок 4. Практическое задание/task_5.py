"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
from timeit import timeit


def simple(i):  # O(n**2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def sieve(q):  # O(n)
    """Этот цикл я нашел в интернете и чуть подогнал к требованиям"""
    n = q ** 2
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:  # O(n)
            ps.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False  # O(n)
                j = j + 2 * i + 3
        i += 1
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1
        p += 2
        if len(ps) == q:
            break
    return ps[q - 1]


def my_func(c):  # O(n)
    """Этот придумал я но он не сказать чтобы был оптимальный, но я смог его сделать быстрее остольных"""
    result = [2]
    end = 20
    while len(result) < c:  # O(1)
        counter = 0
        list_numb = [i for i in range(1, end, 2)]  # O(n)
        list_numb[0] = 0
        while counter < end // 2:  # O(1)
            cur_numb = list_numb[counter]  # O(n)
            if cur_numb and cur_numb not in result:  # O(n)
                result.append(cur_numb)
                for f in range(counter + 1, len(list_numb)):  # O(n)
                    if list_numb[f] % cur_numb == 0:  # O(n)
                        list_numb[f] = False
            counter += 1
            if len(result) == c:
                break
        end += c
    return result[-1]


print('Время выполнения моей функции для 10:', timeit('my_func(10)', globals=globals(), number=100))
print('Время выполнения решето функции для 10:', timeit('sieve(10)', globals=globals(), number=100))
print('Время выполнения перебора функции для 10:', timeit('simple(10)', globals=globals(), number=100))
print('Время выполнения моей функции для 100:', timeit('my_func(100)', globals=globals(), number=100))
print('Время выполнения решето функции для 100:', timeit('sieve(100)', globals=globals(), number=100))
print('Время выполнения перебора функции для 100:', timeit('simple(100)', globals=globals(), number=100))
print('Время выполнения моей функции для 1000:', timeit('my_func(1000)', globals=globals(), number=100))
print('Время выполнения решето функции для 1000:', timeit('sieve(1000)', globals=globals(), number=100))
print('Время выполнения перебора функции для 1000:', timeit('simple(1000)', globals=globals(), number=100))

'''
Алгоритм эростофера быстрее обычного перебора но на малых значениях перебор может быть быстрее
'''

