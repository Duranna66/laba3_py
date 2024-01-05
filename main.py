import re

def is_valid_snils(snils):
    snils = re.sub(r'\D', '', snils)

    if len(snils) != 11:
        return False

    number = int(snils[:9])
    control_sum = int(snils[9:])
    calculated_control_sum = calculate_control_sum(number)

    return control_sum == calculated_control_sum

def calculate_control_sum(number):
    control_sum = 0
    for i in range(9, 0, -1):
        control_sum += int(str(number)[(9 - i)]) * i

    if control_sum > 101:
        control_sum %= 101
    if control_sum < 100:
         return control_sum
    elif control_sum == 100 or control_sum == 101:
        control_sum = 0
    print(control_sum)
    return control_sum

snils = input("Введите СНИЛС для проверки: ")
if is_valid_snils(snils):
    print("СНИЛС является корректным.")
else:
    print("СНИЛС является некорректным.")