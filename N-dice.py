def main():
    import random as rd
    n = 6
    m = 10
    results = []
    for i in range(0, m):
        results.append(rd.randint(1, n))
    print(results)


if __name__ == '__main__':
    main()
