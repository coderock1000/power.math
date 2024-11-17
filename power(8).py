def power_of_8(num):
    if num <= 0:
        return False
    while num % 8 == 0:
        num //= 8
    return num == 1

number = int(input("Enter a number: "))
if power_of_8(number):
    print(number," is a power of 8.")
else:
    print(number," is not a power of 8.")
