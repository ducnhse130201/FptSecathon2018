#!/usr/bin/env python2
import re, os
def encrypt(plaintext, key): return bytes(bytearray([x^y for x,y in zip(bytearray(plaintext), bytearray(key))]))

def main():
    from secret import secret_messages, FLAG
    assert FLAG == 'FuSecAthon{' + secret_messages[-1] + '}'
    PATTERN = "^[ a-zA-Z,.\-()!']+$"
    for msg in secret_messages: assert re.match(PATTERN, msg)

    max_len = max(map(len, secret_messages))
    pad = os.urandom(max_len)

    with open('ciphertexts.txt', 'w') as f:
        for msg in secret_messages:
            print >>f, encrypt(msg, pad).encode('hex')

if __name__ == '__main__':
    main()
