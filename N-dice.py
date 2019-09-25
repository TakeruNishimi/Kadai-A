def main():
    import random as rd
    n = int(input('面の数を入力してください。　＞　'))
    m = int(input('ふる回数を入れてください。　＞　'))
    results = []
    for i in range(0, m):
        results.append(rd.randint(1, n))
    print(results)


if __name__ == '__main__':
    main()
