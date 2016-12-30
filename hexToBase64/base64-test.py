import unittest
import base64


class Challenge1Methods(unittest.TestCase):
    def test_to_int(self):
        self.assertEqual(base64.to_int('0'), 0)
        self.assertEqual(base64.to_int('f'), 15)

    def test_to_base64_singledigit(self):
        self.assertEqual(base64.to_base64(0), 'A')
        self.assertEqual(base64.to_base64(26), 'a')
        self.assertEqual(base64.to_base64(52), '0')
        self.assertEqual(base64.to_base64(62), '+')
        self.assertEqual(base64.to_base64(63), '/')

    def test_to_base64_multidigit(self):
        self.assertEqual(base64.to_base64(64), 'BA')
        self.assertEqual(base64.to_base64(4096), 'BAA')
        self.assertEqual(base64.to_base64(4096 * 15 + 64 * 62 + 27), 'P+b')

    def test_hex_to_base64(self):
        pass

    def test_challenge1(self):
        string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        string_in_base64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(base64.hex_str_to_base_64_str(string), string_in_base64)

if __name__ == '__main__':
    unittest.main(verbosity=2)
