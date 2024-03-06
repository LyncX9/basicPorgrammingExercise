while True:
    try:
        num = int(input("Enter any number to test whether it is odd or even and greater than 10: "))
        if (num % 2) == 0:
            if num > 10:
                print(f"The number {num} is even and greater than 10.")
            else:
                print(f"The number {num} is even and not greater than 10.")
        else:
            if num > 10:
                print(f"The number {num} is odd and greater than 10.")
            else:   
                print(f"The number {num} is odd and not greater than 10.")
                
        break

    except ValueError:
        print("The input is wrong, please input a number.")