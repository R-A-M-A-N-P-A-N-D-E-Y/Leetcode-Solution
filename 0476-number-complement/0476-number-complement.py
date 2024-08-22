class Solution:
    def findComplement(self, num: int) -> int:
        return binary_to_int(complement_binary(int_to_binary(num)))

def int_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    
    return binary


def binary_to_int(binary_str):
    integer_value = 0
    length = len(binary_str)
    
    for i in range(length):
        bit = int(binary_str[length - i - 1])
        integer_value += bit * (2 ** i)
    
    return integer_value


def complement_binary(binary_str):
    complemented_str = ""
    
    for bit in binary_str:
        if bit == '0':
            complemented_str += '1'
        else:
            complemented_str += '0'
    
    return complemented_str
