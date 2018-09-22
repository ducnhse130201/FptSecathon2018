#!/usr/bin/env python2
import re
import os
from Crypto.Cipher import DES


questions = [
    'What does DES stands for?',
    'What is its block size in bytes?',
    '''Why do we need the permutation and substitution steps?
    A. Permutation provides confusion and substitution provides diffusion.
    B. Permutation provides diffusion and substitution provides confusion.
    C. Both provide confusion.
    D. Both provide diffusion.''',
]


def complement(block):
    return bytes(bytearray(b ^ 255 for b in bytearray(block)))


def encrypt(input_block, key):
    return DES.new(key).encrypt(input_block)


def verify_answer(question, expected_answer):
    answer = raw_input(question + '\n>>')
    if re.sub('[ \t]', '', answer).lower() == expected_answer: return True
    else: return False


def main():
    from secret import expected_answers, facts, FLAG
    
    print "\nAre you a DES master? Let's check it out!"
    try:
        # question 1
        assert verify_answer('\nQ1: ' + questions[0], expected_answers[0])
        print 'Correct!', facts[0]

        # question 2
        assert verify_answer('\nQ2: ' + questions[1], expected_answers[1])
        print 'Correct!', facts[1]

        # question 3
        assert verify_answer('\nQ3: ' + questions[2], expected_answers[2])
        print 'Correct!', facts[2]

        # additional information
        print '\nThis information is needed to answer the next 2 questions:'
        key = os.urandom(8)
        input_block = os.urandom(8)
        output_block = encrypt(input_block, key)
        print 'If key = {} and input_block = {}, then output_block = {}'.format(key.encode('hex'), input_block.encode('hex'), output_block.encode('hex'))

        # question 4
        new_key = raw_input('\nQ4: Please provide another key (called new_key) such that encrypt(input_block, new_key) == output_block\n>>').decode('hex')
        if new_key == key or encrypt(input_block, new_key) != output_block:
            raise Exception()
        print 'Correct!', facts[3]

        # question 5
        new_key = raw_input('\nQ5: Please provide a key (called new_key) such that encrypt(complement(input_block), new_key) == complement(output_block)\n>>').decode('hex')
        if encrypt(complement(input_block), new_key) != complement(output_block):
            raise Exception()
        print 'Correct!', facts[4]

        # question 6
        print '\nQ6: Please provide a key (called new_key) and a block (called new_block) such that encrypt(new_block, new_key) == new_block.\n'
        new_block = raw_input('new_block:\n>>').decode('hex')
        new_key = raw_input('new_key:\n>>').decode('hex')
        if encrypt(new_block, new_key) != new_block:
            raise Exception()
        print 'Correct!', facts[5]

        # FLAG award
        print "Congratulations. Here's the FLAG!"
        print FLAG

    except:
        print 'Incorrect!'

if __name__ == '__main__':
    main()
