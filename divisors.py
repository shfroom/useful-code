#!/usr/bin/env python3

def f(n):
    c = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0: c += 2 if i * i != n else 1
    return c

print(f(10))