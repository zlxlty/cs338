# A = g^a mod p
# B = g^b mod p

Public = {
    'p': 61,
    'g': 7,
    'A': 30,
    'B': 17
}

def break_brute_force(p, g, A, B):
    
    a = b = None
    
    for i in range(p):
        if g**i % p == A:
            print(f'Found a: {i}')
            a = i
            break
        
    for i in range(p):
        if g**i % p == B:
            print(f'Found b: {i}')
            b = i
            break
        
    return a, b

if __name__ == '__main__':
    break_brute_force(**Public)