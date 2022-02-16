def syracuse(n):
    print("n : ", n)
    if (n == 1):
        return 0
    if (n % 2):
        return syracuse(3 * n + 1) + 1
    else:
        return syracuse(n // 2) + 1

number = int(input())
flightTime = syracuse(number)
print("The flight time for {} is {}".format(number, flightTime))