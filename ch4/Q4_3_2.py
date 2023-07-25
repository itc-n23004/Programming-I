def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = list(range(100))
s = func_square(*numbers)
print(s)
