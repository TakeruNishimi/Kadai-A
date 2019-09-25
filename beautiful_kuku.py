def main():
    row = input("行数を入力してください。　＞　")
    col = input("列数を入力してください。　＞　")
    for i in range(1, int(row) + 1):
        for j in range(1, int(col) + 1):
            print_formula(i, j)
        print()


def print_formula(a, b):
    print(f'{a} × {b} = ', end=" ")
    if (len(str(a * b)) == 1):
        print(' ', end="")
    print(f'{a * b} |', end="")


if __name__ == '__main__':
    main()
