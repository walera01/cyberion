def calculate(i):
    s = 0
    while i > s:
        s += i/2
        i -= 2
    return s

print(calculate(6))