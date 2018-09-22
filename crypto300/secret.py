FLAG = 'FLAG{Th3_n3xt_ch4113ng3_w1ll_b3_n4m3d_<P14y1ng_w1th_AES>}'

expected_answers = [
    'dataencryptionstandard',
    '8',
    'b'
]

facts = [
    'Although DES is outdated, it influences the design of many modern block ciphers.',
    'DES takes an 8-byte block as input to produce another 8-byte block.',
    'Confusion is the complexity in the relationship between the output block and the key. Diffusion means that changing a single bit of the plaintext results in the flips of about half of the bits in the ciphertext. Both are important properties of a secure cryptosystem.',
    'There are 8 (out of 64) bits of the key were originally used for parity checking. For many DES implementations (include pycrypto), those bits are simply ignored.',
    'If we complement the key and the input, we would also complement the output.',
    'This challenge is inspired by the challenge DM-COLLISION at Google CTF Quals 2018.'
]
