a = int(input("Enter a: "))
b = int(input("Enter b: "))

def add():
       print("Sum:", a + b)

def subtract():
       print("Difference:", a - b)

def multiply():
    print("Product:", a * b)

def divide():
    print("Product:", a / b)

def percent():
    print("Product:", a/100*b)

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percent")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        subtract()
    elif choice == "3":
        multiply()
    elif choice == "4":
        divide()
    elif choice == "5":
       percent()
    elif choice>="6":
        break
    else:
        print("Invalid choice")
