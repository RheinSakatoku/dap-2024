roman_counts = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def encode(s):
    if s == "":
        return 0

    if len(s) > 1 and roman_counts[s[0]] < roman_counts[s[1]]:
        return -roman_counts[s[0]] + encode(s[1:])
    else:
        return roman_counts[s[0]] + encode(s[1:])

s = input("Введи число римскими цифрами капсом: ")
print("Десятичное значение:", encode(s))
