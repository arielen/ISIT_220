""" 7.	Числа Фибоначчи определяются по формуле: fn=f(n-1)+f(n-2), при n=2, 3,.. (f0=f1=1).
Найти 40-е число Фибоначчи. """

fib0 = 1
fib1 = 1
n = 40

i = 0
while i < n - 2:
    fib_n = fib0 + fib1
    fib0 = fib1
    fib1 = fib_n
    i += 1

print(n, 'число Фибоначчи равно: ', fib1)