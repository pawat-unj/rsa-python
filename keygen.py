import random

# generate a list of key sets based on the requested length
def keysGen(length):
    keylst = []
    for i in range(length):
        keylst.append(keyGen())
    return keylst

# generate a key set in the format (N, public key, private key)
#integer i is only used as input so it can be mapped in keysGen
def keyGen():
    # generate 2 512-bit prime numbers 
    prime1 = random.getrandbits(512)
    while not isPrime(prime1):
        prime1 = random.getrandbits(512)
    prime2 = random.getrandbits(512)
    while not isPrime(prime2):
        prime2 = random.getrandbits(512)
    # generate e that is coprime to (prime1 - 1)(prime2 - 1)
    e = random.getrandbits(16)
    while not isCoprime((prime1 - 1) * (prime2 - 1), e):
        e = random.getrandbits(16)
    # calculate inverse of e (mod(prime1 - 1)(prime2 - 1))
    d = pow(e, -1, (prime1 - 1) * (prime2 - 1))
    return (prime1 * prime2, e, d)

# checks whether an integer is prime
def isPrime(i):
    if not lowLevelIsPrime(i):
        return False
    # highLevelIsPrime has an accuracy of 75%. 
    # In order to achieve an error probabilty of <= 1/2**128 (commercial application standards), 
    # 64 trials need to be performed
    HIGHLEVELTRIALS = 64
    if not highLevelIsPrime(i, HIGHLEVELTRIALS):
        return False
    return True

# low level primality test
def lowLevelIsPrime(i):
    basic_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in basic_prime_list:
        if i % prime == 0:
            return False
    return True

# high level primality test (Miller Rabin)
def highLevelIsPrime(i, numberOfRabinTrials):
   
    maxDivisionsByTwo = 0
    evenComponent = i - 1
   
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2 ** maxDivisionsByTwo * evenComponent == i - 1)
   
    def trialComposite(round_tester):
        if pow(round_tester, evenComponent, i) == 1:
            return False
        for j in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** j * evenComponent, i) == i - 1:
                return False
        return True

    for k in range(numberOfRabinTrials):
        round_tester = random.randrange(2, i)
        if trialComposite(round_tester):
            return False
    return True

# check coprimality with the Euclid's theorem
def isCoprime(no1, no2):
    def gcd(no1, no2):
        while no2 != 0:
            no1, no2 = no2, no1 % no2
        return no1
    return gcd(no1, no2) == 1