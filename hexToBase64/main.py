#!/usr/bin/env python
# -*- coding: utf-8 -*-


def to_int(hex_char):
    dic = {'%s' % i: i for i in range(10)}
    dic['a'] = 10
    dic['b'] = 11
    dic['c'] = 12
    dic['d'] = 13
    dic['e'] = 14
    dic['f'] = 15
    return dic[hex_char]


def to_base64(int_value):
    dic = {i: '%s' % (i - 52) for i in range(52, 62)}
    dic_lower = {num: chr(num + 71) for num in range(26, 52)}
    dic_upper = {num: chr(num + 65) for num in range(0, 26)}
    dic.update(dic_lower)
    dic.update(dic_upper)
    dic[62] = '+'
    dic[63] = '/'

    mod = int_value % 64
    dividend = int_value >> 6
    print((int_value, mod, dividend, dic[mod]))
    last_digit = dic[mod]
    if dividend == 0:
        return last_digit
    return to_base64(dividend) + last_digit


def hex_to_base64(hex):
    """
    Takes a hex string of up to three characters and converts it to a 2 digit base64 string
    :param hex: one or two digit long hex string, consisting of 0-9 or a-f
    :return: the value in base 64
    """
    if len(hex) < 3:
        return hex_to_base64('0' + hex)
    int_value = to_int(hex[0]) * 16 ** 2 + to_int(hex[1]) * 16 + to_int(hex[2])
    return to_base64(int_value)


def hex_str_to_base_64_str(hex_str):
    if len(hex_str) == 0:
        return ''
    return hex_str_to_base_64_str(hex_str[:-3]) + hex_to_base64(hex_str[-3:])


string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(hex_str_to_base_64_str(string))
print('Expected String: ', 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
