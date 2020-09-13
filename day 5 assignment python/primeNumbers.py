
def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True


fltrobj = filter(prime, range(2500))
print("prime numbers between 1-2500:", list(fltrobj))

