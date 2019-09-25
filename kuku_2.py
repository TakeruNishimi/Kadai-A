def main():
    row = input("行数を入力してください　＞")
    col = input("列数を入力してください　＞")
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(f'{i * j} ', end="")
        print()


if __name__ == '__main__':
    main()