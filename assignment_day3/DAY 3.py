# question 1
altitude = input('enter the altitude')
altitude = int(altitude)
if altitude < 1000:
    print("land the plane")
elif altitude > 1000 and altitude < 5000 :
    print("come down to 1000ft")
else:
    print("go around and try later")

# prime numbers
num = input('enter the number')
num = int(num)
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print(num, "is not prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
