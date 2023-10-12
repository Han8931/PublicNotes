

def hamming_distance(x, y):
    xor = bin(x^y)
    return xor.count('1')

print(hamming_distance(1, 4))
