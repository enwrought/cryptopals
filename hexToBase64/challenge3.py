import char_scoring
import crypto_base64
import binascii


def decryptor(encoded, value):
    hex_value = crypto_base64.to_hex(value)
    hex_value = '0' + hex_value if len(hex_value) == 1 else hex_value

    length = len(encoded) // 2
    xor = crypto_base64.xor_hex_strs(encoded, hex_value * length)
    return '0' * (len(encoded) - len(xor)) + xor


def to_ascii(xor):
    return ''.join(chr(i) for i in binascii.unhexlify(xor) if i in range(65, 91) or i in range(97, 123))


def choose_best(encoded):
    texts = (char_scoring.clean_alpha(to_ascii(decryptor(encoded, i))) for i in range(255))
    filtered_texts = (text for text in texts if len(text) > 0)
    shift_values = sorted(((char_scoring.unnormed_chi_squared(char_scoring.get_scaled_freq(text)), text) for text
                           in filtered_texts),
                          key=lambda tup: tup[0])
    return shift_values
