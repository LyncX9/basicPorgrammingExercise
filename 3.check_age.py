while True:
    try:
        age = int(input("Enter your age: "))
        if(age >= 18 and age <= 65):
            print(f"your age {age} is eligible to vote")

        else:
            print(f"your age {age} is not eligible to vote")

        break
    except ValueError:
        print("wrong input. Please input number.")