#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    value = 0
    prev_digit = 0

    if type(roman_string) is not str or roman_string is None:
        return 0

    for digit in reversed(roman_string):
        digit_value = roman_numerals[digit]
        if digit_value >= prev_digit:
            value += digit_value
            prev_digit = digit_value
        else:
            value -= digit_value
    return value
