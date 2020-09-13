lst = list(range(1042000, 702648265))
print(list(lst))

def get_armstrong():
    for num in lst:
        order = len(str(num))
        temp = num
        sum = 0
        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** order
            temp = temp//10
        if sum == num:
            result = num


print(get_armstrong())
