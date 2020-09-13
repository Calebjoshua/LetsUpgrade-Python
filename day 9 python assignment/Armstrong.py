lst = list(range(1, 1000))


def get_armstrong_num(lst):
    for num in lst:
        order = len(str(num))
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum = sum +digit ** order
            temp = temp // 10
        if sum == num:
            yield num


print(list(get_armstrong_num(lst)))