# Notes:
# The Hadamard of '101' is '01011010'


# The outer product of 101 and 101 is:
# 1 0 1
# 0 0 0
# 1 0 1
# or : 101000101

from itertools import product

def create_pcp(quadeq_solution):
    '''Given a quadeq solution of the form '0010101',
    where the ith bit represents u_i = 0 or 1,
    return the bitstring of the probablistically checkable proof'''

    return hadamard_encoding_of(quadeq_solution) \
           + hadamard_encoding_of(tensor_product(quadeq_solution, quadeq_solution))

def hadamard_encoding_of(bitstring):
    bitlength = len(bitstring)

    return ''.join(inner_product(bitstring, i)
                   for i in all_bitstrings_of_length(bitlength))

def inner_product(bitstring_x, bitstring_y):
    result = 0
    for bit_x, bit_y in zip(bitstring_x, bitstring_y):
        if bit_x == '1' and bit_y == '1':
            result += 1

    return str(result % 2)

def tensor_product(bitstring_x, bitstring_y):
    return ''.join('1' if bit_x == '1' and bit_y == '1' else '0'
                   for bit_x, bit_y in product(bitstring_x, bitstring_y))

def all_bitstrings_of_length(bitlength):
    '''When bitlength = 3, returns ['000', '001', '010', ... '111']'''
    return [to_bitstring(i, bitlength)
            for i in range(2 ** bitlength)]


def to_bitstring(x, bitlength):
    return bin(x)[2:].rjust(bitlength, '0')

