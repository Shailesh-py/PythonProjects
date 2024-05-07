def celsius_to_fahrenheit(a):
    result = (9 / 5) * a + 32
    return result


def fahrenheit_to_celsius(b):
    result = (b - 32) * 5 / 9
    return result


while True:
    print("Enter your choice: \n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n3. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        fahrenheit = float(input("Enter the Fahrenheit temperature: "))
        print(fahrenheit_to_celsius(fahrenheit))
    elif choice == 2:
        celsius = float(input("Enter the Celsius temperature: "))
        print(celsius_to_fahrenheit(celsius))
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
