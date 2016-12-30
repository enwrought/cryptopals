"""
Run all tests at once
"""
import unittest


def load_tests(loader, tests, pattern):
    test_suite = unittest.TestSuite()
    # TODO: pattern match
    return test_suite

if __name__ == 'main':
    # TODO: take in args and pattern match
    pass
