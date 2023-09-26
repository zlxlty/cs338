import math

CACHED = True

Public = {
    'e_Bob': 17,
    'n_Bob': 170171,
}

cipher_text = [65426, 79042, 53889, 42039, 49636, 66493, 41225, 58964,
126715, 67136, 146654, 30668, 159166, 75253, 123703, 138090,
118085, 120912, 117757, 145306, 10450, 135932, 152073, 141695,
42039, 137851, 44057, 16497, 100682, 12397, 92727, 127363,
146760, 5303, 98195, 26070, 110936, 115638, 105827, 152109,
79912, 74036, 26139, 64501, 71977, 128923, 106333, 126715,
111017, 165562, 157545, 149327, 60143, 117253, 21997, 135322,
19408, 36348, 103851, 139973, 35671, 93761, 11423, 41336,
36348, 41336, 156366, 140818, 156366, 93166, 128570, 19681,
26139, 39292, 114290, 19681, 149668, 70117, 163780, 73933,
154421, 156366, 126548, 87726, 41418, 87726, 3486, 151413,
26421, 99611, 157545, 101582, 100345, 60758, 92790, 13012,
100704, 107995]

def get_prime(max_limit):
    prime = [True for _ in range(max_limit + 1)]
    
    p = 2
    while p * p <= max_limit ** 2:
        if prime[p]:
            for i in range(p * p, max_limit + 1, p):
                prime[i] = False
                
            yield p
        p += 1
        
def factorize(n):
    factors = []
    for prime in get_prime(math.ceil(n)):
        while n % prime == 0:
            factors.append(prime)
            n //= prime
            
    return factors

def get_d(e, phi):
    d = 0
    while (d * e) % phi != 1:
        d += 1
        
    return d

def decrypt(cipher_text, d, n):
    return [(c ** d) % n for c in cipher_text]



def encrypt(plain_text, e, n):
    return [(p ** e) % n for p in plain_text]

def decimal_to_bytestring(plain_text_integers):
    bytestring = []
    for i in plain_text_integers:
        binary = bin(i)[2:]
        bytestring.append(binary[:-8])
        bytestring.append(binary[-8:])
        
    return bytestring

def bytestring_to_ascii(bytestring):
    return ''.join([chr(int(b, 2)) for b in plain_text_bytestring])

if __name__ == '__main__':
    factors = factorize(Public['n_Bob']) # impractical for large n
    if len(factors) != 2:
        raise Exception('n_Bob is not the product of two primes')
    
    if CACHED:
        plain_text_integers = [18537, 8258, 28514, 11808, 18727, 27936, 30561, 27755, 26990, 26400, 26226, 28525, 8302, 28535, 8303, 28206, 8281, 28533, 29216, 28769, 27692, 8257, 27753, 25445, 11808, 26740, 29808, 29498, 12079, 26223, 30062, 25697, 29801, 28526, 11885, 28538, 26988, 27745, 11887, 29287, 12133, 28207, 28786, 26998, 24931, 31086, 28532, 26990, 25452, 30052, 25956, 12129, 29300, 26979, 27749, 29487, 26996, 29485, 28518, 26217, 25449, 24940, 11619, 24946, 29485, 24946, 25901, 29800, 25901, 30575, 29299, 29741, 28786, 28516, 30051, 29741, 25441, 29797, 26479, 29305, 11639, 25901, 26721, 30309, 11621, 30309, 29229, 29285, 30313, 25975, 25956, 11622, 28530, 11632, 29289, 30305, 25465, 12032]    
    else:
        p, q = factors
        phi = (p - 1) * (q - 1)
        
        d = get_d(Public['e_Bob'], phi) # impractical if don't know p and q
        print(f'd: {d}')
        plain_text_integers = decrypt(cipher_text, d, Public['n_Bob'])
    
    print(plain_text_integers)
    # Encrypt again to check the correctness of d.
    print(encrypt(plain_text_integers, Public['e_Bob'], Public['n_Bob']))
    
    plain_text_bytestring = decimal_to_bytestring(plain_text_integers)
    
    plain_text = bytestring_to_ascii(plain_text_bytestring)
    print(plain_text)