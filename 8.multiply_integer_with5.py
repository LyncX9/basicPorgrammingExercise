while True:
    try:
        num = int(input("input an integer value to multiply it by 5:"))
        print("The result is:", int(num * 5))
        break
    except ValueError:
        print("The input is wrong, please input an integer value.")