def palindrome(string):
    string = string.replace(" ", "").lower()


    return string == string[::-1]


input_string = "Кит на морі романтик"
if palindrome(input_string):
    print(f"'{input_string}' є паліндромом.")
else:
    print(f"'{input_string}' не є паліндромом.")

input_string = "Пон за пон"
if palindrome(input_string):
    print(f"'{input_string}' є паліндромом.")
else:
    print(f"'{input_string}' не є паліндромом.")