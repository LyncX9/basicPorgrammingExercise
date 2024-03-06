while True:
    try:
        age = int(input("Enter your age: "))

        if (age >= 21):
            print("You're passed")

        else:
            print(f"sorry, you didn't pass. Your age {age} is less than 21.")

        break
    except ValueError:
        print("Wrong input. Please input number")