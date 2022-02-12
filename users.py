from keygen import keysGen
from encryptdecrypt import encryptInt, decryptInt, toASCII, toString

# in reality, one could be both the sender and receiver but for the sake of simplicity, the algorithm is
# demonstrated for separate senders and receivers

class Sender:
    def __init__(self):
        self.message = ""
        self.asciiMessage = []
        self.encryptedMessage = []

    # loops through the message and encrypts each char with a unique key
    def encryptMessage(self, keys):
        for i in range(len(self.asciiMessage)):
            self.encryptedMessage.append(encryptInt(self.asciiMessage[i], keys[i][0], keys[i][1]))
        return self.encryptedMessage

    # request {number of chars in the message} sets of keys from the receiver
    def requestKeys(self, message):
        self.asciiMessage = toASCII(message)
        return len(self.asciiMessage)

class Receiver:
    def __init__(self):
        self.allKeys = []
        self.length = 0
        self.decryptedMessage = ""

    # loops through the encrypted message and decrypts each char with a unique private key

    def decryptMessage(self, encryptedMessage):
        asciiMessage = []
        for i in range(self.length):
            asciiMessage.append(decryptInt(encryptedMessage[i], self.allKeys[i][0], self.allKeys[i][2]))
        self.decryptedMessage = toString(asciiMessage)
        return self.decryptedMessage
    
    # generate a list of keys as requested by the sender. The private keys are stored in an instance var and the public keys are sent to receiver

    def generateKeys(self, length):
        self.length = length
        self.allKeys = keysGen(length)
        publicKey = []
        for i in range(length):
            publicKey.append((self.allKeys[i][0], self.allKeys[i][1]))
        return publicKey
