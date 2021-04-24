import math
import random
import base64
import binascii

def genPublicKey(q, amount, s):
    e = []
    B = []
    A = random.sample(range(q), amount)
    print("Public key A: \t", A)
    for x in range(0, len(A)):
        e.append(random.randint(1, 3))
    print ("Error e: \t\t", e)
    for x in range(0, len(A)):
        B.append((A[x] * s + e[x]) % q)
    print("Public key B: \t", B)
    return A, B

def getUV(A, B, amount, q, m):
    sample = random.sample(range(amount - 1), amount // 4)
    UV = []
    u = 0
    v = 0
    for x in range(len(sample)):
        u = u + (A[sample[x]])
        v = v + (B[sample[x]])
    v = v + math.floor(q // 2) * m
    v = v % q
    u = u % q
    UV.append(u)
    UV.append(v)
    return UV

def toInteger(m):
    encoded = []
    for character in m:
        encoded.append(base64.b64encode(bytes(character, "utf-8")))
    binary = []
    for i in range(len(encoded)):
        binary.append(binascii.a2b_base64(encoded[i]))
    intMessage = []
    for i in range(len(encoded)):
        intMessage.append(int.from_bytes(binary[i], byteorder='little'))
    return intMessage


def toBits(input=[]):
    result = []
    for i in range(0, len(input)):
        l = [0]*(8)
        l[0] = input[i] & 0x1
        l[1] = (input[i] & 0x2) >> 1
        l[2] = (input[i] & 0x4) >> 2
        l[3] = (input[i] & 0x8) >> 3
        l[4] = (input[i] & 0x16) >> 4
        l[5] = (input[i] & 0x32) >> 5
        l[6] = (input[i] & 0x64) >> 6
        l[7] = (input[i] & 0x128) >> 7
        result.append(l)  
    return result

def bitsToInterger(array=[]):
    result = []
    for element in array:
        number = 0
        for i in range(0, len(element) - 1):
            if (element[i] == 1):
                number = number + pow(2, i)
        result.append(number)
    return result

def showMessage(message):
    print("------------------MESSAGE-----------------")
    for i in range(len(message)):
        letter = chr(abs(message[i]))
        print(letter, end="")
    print()

def encrypt(A, B, q, message, amount):
    cypher = []
    for element in message:
        result = []
        for x in element:
            UV = getUV(A, B, amount, q, x)
            result.append(UV)
        cypher.append(result)
    return cypher

def decrypt(cypher, q, s):
    result = []
    for element in cypher:
        C = []
        for x in element:
            tmp = (x[1] - s * x[0]) % q
            if (tmp > q // 2):
                C.append(1)
            else:
                C.append(0)
        result.append(C)
    return result    

amount = 20
q = 97
s = 5
message = "So tell me, what is it that you truly desire?"
integers = toInteger(message)
print(integers)
bits = toBits(integers)
print(bits) 
publicKey = genPublicKey(q, amount, s)
print("-----------------------------------------CYPHER-----------------------------------------------------")
print()
cypher = encrypt(publicKey[0], publicKey[1], q, bits, amount)
print(cypher)
plainBits = decrypt(cypher, q, s)
print(plainBits)
plainIntegers = bitsToInterger(plainBits)
print(plainIntegers)
showMessage(plainIntegers)
