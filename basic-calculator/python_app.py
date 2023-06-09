def add(first_number, second_number):
    answer = first_number + second_number
    print(f'{first_number} + {second_number} = {answer}')


def sub(first_number, second_number):
    answer = first_number - second_number
    print(f'{first_number} - {second_number} = {answer}')


def mul(first_number, second_number):
    answer = first_number * second_number
    print(f'{first_number} * {second_number} = {answer}')


def div(first_number, second_number):
    answer = first_number // second_number
    print(f'{first_number} / {second_number} = {answer}')


contador = 0

while True:
    if contador > 0:
        print("\n")
    print("[A]ddition")
    print("[S]ubstraction")
    print("[M]ultiplication")
    print("[D]ivision")
    print("[E]xit")

    choice = input("Input your choice: ")

    choice = choice.upper()

    if choice == "A":
        print("Addition")
        first_number = int(input("input your first number: "))
        second_number = int(input("input your second number: "))

        add(first_number, second_number)

    elif choice == "S":
        print("Substraction")
        first_number = int(input("input your first number: "))
        second_number = int(input("input your second number: "))

        sub(first_number, second_number)

    elif choice == "M":
        print("Multiplication")
        first_number = int(input("input your first number: "))
        second_number = int(input("input your second number: "))

        mul(first_number, second_number)

    elif choice == "D":
        print("Division")
        first_number = int(input("input your first number: "))
        second_number = int(input("input your second number: "))

        div(first_number, second_number)
    
    elif choice == "E":
        print("program ended")
        quit()

    contador += 1
