def main():
    a = 4
    b = 5
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print(f'{i * j} ', end="")
        print()


if __name__ == '__main__':
    main()