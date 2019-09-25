def main():
    row = 9
    col = 9
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print_formula(i, j)
        print()


def print_formula(a, b):
    print(f'{a} × {b} = ', end=" ")
    if (len(str(a * b)) == 1):
        print(' ', end="")
    print(f'{a * b} |', end="")


if __name__ == '__main__':
    main()
