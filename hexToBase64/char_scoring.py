#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

# TODO: parking lot: Bayes/true probabilities

CHAR_FREQ = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015,
             'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749,
             'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758,
             'v': 0.00978, 'w': 0.02360, 'x': 0.00150, 'y': 0.01974, 'z': 0.00074}


def get_empty():
    return {key: 0 for key in CHAR_FREQ.keys()}


def accumulator(memo, char):
    """
    Helper function for char_score()
    :param memo:
    :param char:
    :return:
    """
    if char in memo:
        memo[char] += 1
    else:
        memo[char] = 1
    return memo


def get_scaled_freq(text):
    freq = functools.reduce(accumulator, text, get_empty())
    total = sum(freq[letter] for letter in freq)
    if total == 0:
        total = 1
    scaled_freq = {letter: freq[letter] / total for letter in freq}
    return scaled_freq


def unnormed_chi_squared(sample, dist=CHAR_FREQ):
    """
    Is not scaled by number of elements because we just choose the best.  Equivalent to Euclidean distance in R^26
    :param sample:
    :param dist:
    :return:
    """
    distance = sum((sample[letter] - CHAR_FREQ[letter]) ** 2 / CHAR_FREQ[letter] for letter in CHAR_FREQ)
    return distance


def clean_alpha(text):
    return ''.join(letter for letter in text.lower() if letter in CHAR_FREQ)
