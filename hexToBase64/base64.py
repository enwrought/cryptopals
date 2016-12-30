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


def to_base64(int_value):
    """
    Uses a dictionary to
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
