#!/usr/bin/env python
# -*- coding: utf-8 -*-


def to_int(hex_char):
    """
    equivalent to `int(hex_char, 16)`
    :param hex_char: {str} single hex digit
    :return: {int} value in base 10
    """
    dic = {'%s' % i: i for i in range(10)}
    dic['a'] = 10
    dic['b'] = 11
    dic['c'] = 12
    dic['d'] = 13
    dic['e'] = 14
    dic['f'] = 15
    return dic[hex_char]


# TODO: refactor to_hex and to_base64 to base function with error handling
def to_hex(int_value):
    """
    Uses dictionary to do conversion for each digit
    :param int_value:
    :return:
    """
    dic = {i: '%s' % i for i in range(10)}
    dic_a_to_f = {num: chr(num + 87) for num in range(10, 16)}
    dic.update(dic_a_to_f)

    mod = int_value % 16
    dividend = int_value >> 4
    last_digit = dic[mod]
    if dividend == 0:
        return last_digit
    return to_hex(dividend) + last_digit


def to_base64(int_value):
    """
    Uses a dictionary to do conversion for each digit
    :param int_value: {int} arbitrary integer value in base 10
    :return: {str} value in base 64
    """
    dic = {i: '%s' % (i - 52) for i in range(52, 62)}
    dic_lower = {num: chr(num + 71) for num in range(26, 52)}
    dic_upper = {num: chr(num + 65) for num in range(0, 26)}
    dic.update(dic_lower)
    dic.update(dic_upper)
    dic[62] = '+'
    dic[63] = '/'

    mod = int_value % 64
    dividend = int_value >> 6
    last_digit = dic[mod]
    if dividend == 0:
        return last_digit
    return to_base64(dividend) + last_digit


def hex_to_base64(hex_str):
    """
    Takes a hex string of up to three characters and converts it to a 2 digit base64 string
    :param hex_str: {str} one or two digit long hex string, consisting of 0-9 or a-f
    :return: {str} the value in base 64
    """
    if len(hex_str) < 3:
        return hex_to_base64('0' + hex_str)
    elif len(hex_str) > 3:
        raise ValueError('The `hex_str` arg for hex_to_base64() must be <= 3 chars')
    int_value = to_int(hex_str[0]) * 16 ** 2 + to_int(hex_str[1]) * 16 + to_int(hex_str[2])
    return to_base64(int_value)


def hex_str_to_base_64_str(hex_str):
    """
    Recursively converts every 3 hex string chars to 2 base64 string chars, depth first
    :param hex_str: {str} the hex string
    :return: {str} the base64 representation of a hex string
    """
    if len(hex_str) == 0:
        return ''
    return hex_str_to_base_64_str(hex_str[:-3]) + hex_to_base64(hex_str[-3:])


def xor_hex_strs(hex_str1, hex_str2):
    """
    converts both hex_strs to int and do a bitwise int operations
    A XOR B = ~((A & B) | ~(A | B))
    :param hex_str1: {str}
    :param hex_str2: {str}
    :return: {str} XOR of the two hex_str, as a hex_str
    """
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)
    int_and = int1 & int2
    int_neither = ~(int1 | int2)
    return to_hex(~(int_and | int_neither))
