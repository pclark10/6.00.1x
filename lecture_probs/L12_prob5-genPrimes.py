def genPrimes():
    yield 2
    yield 3
    x = 3
    p = [2,3]
    while True:
        x += 2
        if all(x % i != 0 for i in p):
            yield x
            p.append(x)