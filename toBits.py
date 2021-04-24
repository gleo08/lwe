import math
import base64
import binascii

message = "circles post malone"

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

def toBits(input = []):
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

def bitsToInterger(array = []):
    result = []
    for element in array:
        number = 0
        for i  in range(0, len(element) - 1):
            if (element[i] == 1):
                number = number + pow(2, i)
        result.append(number)
    return result

def showMessage(array = []):
    result = ""
    for i in range(len(array)):
        letter = chr(abs(array[i]))
        result = result + letter
    return result


x = toInteger(message)
y = toBits(x)
print(x)
print(y)
z = bitsToInterger(y)
print(showMessage(z))
