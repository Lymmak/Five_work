def get_numbers():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    return num1, num2
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

if __name__ == '__main__':
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")

    choice = input("Введите выбор (1/2/3): ")

    num1, num2 = get_numbers()

    if choice == '1':
        print("Результат сложения:", add(num1, num2))
    elif choice == '2':
        print("Результат вычитания:", subtract(num1, num2))
    elif choice == '3':
        print("Результат умножения:", multiply(num1, num2))
    else:
        print("Введен недопустимый выбор")