import mdl as calculator


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(num1, "+", num2, "=", calculator.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", calculator.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", calculator.multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", calculator.divide(num1, num2))

        
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")