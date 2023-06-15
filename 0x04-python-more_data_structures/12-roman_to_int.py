#!/usr/bin/python3
# File: 12-roman_to_int.py
# Author: Oluwatobiloba Light


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string
        to be converted.

    Returns:
        int: The equivalent integer value of the Roman numeral.

    Raises:
        None.

    Notes:
        - The function assumes the input Roman numeral
           will be between 1 to 3999.
        - If the roman_string is not a string or None,
           the function returns 0.
    """
    if (not isinstance(roman_string, str)) or roman_string is None:
        return 0
    roman_num_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_num = 0
    for i in range(len(roman_string)):
        if roman_num_dict.get(roman_string[i], 0) == 0:
            return 0
        if i != (len(roman_string) - 1) and roman_num_dict[roman_string[i]]\
           < roman_num_dict[roman_string[i + 1]]:
            roman_num += roman_num_dict[roman_string[i]] * -1
        else:
            roman_num += roman_num_dict[roman_string[i]]

        return roman_num
