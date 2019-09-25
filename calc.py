def main():
    numbers = "1 3 4 5"
    number_list = map(int, numbers.split())
    print(sum_calc(number_list))


def sum_calc(list):
    sum = 0
    for num in list:
        sum += num
    return sum


if __name__ == '__main__':
    main()
