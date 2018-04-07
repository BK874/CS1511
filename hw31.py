# Notes:
# The Hadamard of '101' is '01011010'


# The outer product of 101 and 101 is:
# 1 0 1
# 0 0 0
# 1 0 1
# or : 101000101

from random import randint

def coin_flip():
    return randint(0, 1)

def n_random_bits(n):
    return ''.join(str(coin_flip())
                   for _ in range(n))

def randomly_include_from(sequence):
    return [element
            for element in sequence
            if coin_flip()]

def verify(QUADEQ_instance, number_of_variables, bitlength, proof_string):
    random_equations = randomly_include_from(QUADEQ_instance)
    f, g = proof_string[:2**bitlength + 1], proof_string[2**bitlength + 1:]





def verify_f(bitlength):
    for _ in range(10):
        query_f(f, 10)

def verify_g_encodes_u(u, g, bitlength):
    for _ in range(10):
        x, y = n_random_bits(bitlength), n_random_bits(bitlength)

        
