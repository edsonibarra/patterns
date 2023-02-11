def pattern_one(n):
    s = "*" * n
    for i in range(n):
        print(s)


def pattern_one_sol_2(n):
    for i in range(n):
        s = ''
        for j in range(n):
            s += '*'
        print(s)


def pattern_two(n):
    for i in range(1, n + 1):
        s = '*' * i
        print(s)


def pattern_two_sol_2(n):
    for i in range(n):
        s = ''
        for j in range(i + 1):
            s += '*'
        print(s)


def pattern_three(n):
    for i in range(1, n + 1):
        s = ''
        for j in range(1, i + 1):
            s += str(j)
        print(s)


def pattern_four(n):
    for i in range(1, n + 1):
        s = ''
        for j in range(1, i + 1):
            s += str(i)
        print(s)


def main():
    pattern_one(5)
    print()
    pattern_two(5)
    print()
    pattern_two_sol_2(5)
    print()
    pattern_three(5)
    print()
    pattern_four(5)
main()
