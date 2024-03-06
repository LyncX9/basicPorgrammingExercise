def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

while True:
    try:
        num = int(input("Enter a number: "))
        print(f"the sum of digits in {num} is {sum_of_digits(num)}")

        break

    except ValueError:
        print("The input is wrong, please input some number.")