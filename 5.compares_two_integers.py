while True:
    try:
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))

        if (x == y):
            print(f"The first number: (x) and second number: (y) are equal.")

        elif (x > y):
            print(f"The first number: (x) is greater than second number: (y).")

        elif (x < y):
            print("The second number: (y) is greater than fisrt number:  (x).")

        break

    except ValueError:
        print("The input is wrong, please input an integer value.")