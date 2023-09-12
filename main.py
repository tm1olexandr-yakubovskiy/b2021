def adder(x, y):
    result = x + y
    return result


def додавання(x, y):
    result = x + y
    return result

def віднімання(x, y):
    result = x - y
    return result

def множення(x, y):
    result = x * y
    return result

def ділення(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    result = x/y
    return result


print("Оберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

select = input("Введіть номер операції (1/2/3/4):")
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))

if select == '1':
    print("Результат:", додавання(x, y))
elif select == '2':
    print("Результат:", віднімання(x, y))
elif select == '3':
    print("Результат:", множення(x, y))
elif select == '4':
    print("Результат:", ділення(x, y))
else:
    print("Невірний вибір операції")

