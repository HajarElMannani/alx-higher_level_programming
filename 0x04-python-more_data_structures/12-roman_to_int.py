#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {"i": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    if len(roman_string) == 1:
        return numbers.get(roman_string)
    if type(roman_string) is not str or roman_string is None:
        return 0
    sum = 0
    for i in range(len(roman_string)):
        if len(roman_string) == i + 1:
            sum = sum + numbers.get(roman_string[i])
        elif numbers.get(roman_string[i]) < numbers.get(roman_string[i + 1]):
            sum = sum - numbers.get(roman_string[i])
        else:
            sum = sum + numbers.get(roman_string[i])
    return sum
