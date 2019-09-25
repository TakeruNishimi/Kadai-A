def main():
    numbers = input("スペースで区切って数字を複数入力してください。　＞　")
    number_list = [int(i) for i in numbers.split()]

    # 合計
    print(sum_calc(number_list))

    # 最大値
    print(max_calc(number_list))

    # 最小値
    print(min_calc(number_list))

    # 平均値
    print(mean_calc(number_list))


def sum_calc(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def max_calc(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max


def min_calc(list):
    min = list[0]
    for num in list:
        if num < min:
            min = num
    return min


def mean_calc(list):
    sum = sum_calc(list)
    average = sum / len(list)
    return average



if __name__ == '__main__':
    main()
