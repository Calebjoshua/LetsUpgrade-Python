def smart_divide(func):
    def inner(a, b):
        print("divide ", a, " and ", b)
        if b == 0:
            print("cannot divide")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(20, 10)