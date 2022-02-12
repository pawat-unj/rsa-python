# converts an integer, i, into an encrypted integer
def encryptInt(i, N, publicKey):
    return pow(i, publicKey, N)

# converts an encrypted integer, j, into the orginal integer
def decryptInt(j, N, privateKey):
    return pow(j, privateKey, N)

# converts a string, s, into a list of ASCII values
def toASCII(s):
    ASCII_lst = []
    for character in s:
        ASCII_lst.append(ord(character))
    return ASCII_lst

# converts a list of ASCII values, lst, to string
def toString(lst):
    return ''.join(map(chr, lst))
