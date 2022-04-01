


def main():
    p = 82589933 
    b = 5

    bSecret = 7893
    aSecret = 2348

    bPub = pubKey(p, b, bSecret)
    aPub = pubKey(p, b, aSecret)

    print(f'Bob\'s public key: {bPub}')
    print(f'Alice\'s public key: {aPub}')

    bK = computeK(p, aPub, bSecret)
    aK = computeK(p, bPub, aSecret)

    print(f'Bob\'s K: {bK}')
    print(f'Alice\'s K: {aK}') 

def pubKey(prime, base, secret):
    return base ** secret % prime 
    
def computeK(prime, pubKey, secret):
    return pubKey ** secret % prime

if __name__ == '__main__':
    main()
