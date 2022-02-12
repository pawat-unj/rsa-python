from users import Sender, Receiver

# run "python3 main.py" in the terminal to test the script
# comment out lines 20 and 26 for a cleaner output

print("Initializing sender and receiver instances")

alice = Sender()
bob = Receiver()

i = input("Enter your message: ")

l = alice.requestKeys(i)

print(f'The sender requests {l} set of key(s) from the receiver)')
print("Generating keys.. This takes a while since primality testing is a computatively intensive process.")

k = bob.generateKeys(l)

print(f"The public key is: {k}")
print("Keys sent to sender")
print("Sender encrypting message..")

e = alice.encryptMessage(k)

print(f"The encrypted message is: {e}")
print("Encrypted message sent to receiver")
print("Receiver decrypting message..")

m = bob.decryptMessage(e)

print(f"The message is: {m}")
