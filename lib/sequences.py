#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  
        return

    result = []
    a, b = 0, 1
    for _ in range(length):
        result.append(a)
        a, b = b, a + b

    print(result)

    length = []