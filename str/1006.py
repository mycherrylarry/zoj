#!/usr/bin/env python
class Cryptography:
    def __init__(self, key, n):
        self.key = key
        self.plaintext  = []
        self.plaincode  = [-1] * n
        self.ciphertext = []
        self.ciphercode = [-1] * n
    
    def convertCharToInt(self, c):
        if c == '_': return 0
        if c == '.': return 27
        return ord(c) - ord('a') + 1
    
    def convertIntToChar(self, i):
        if i == 0: return '_'
        if i == 27: return '.'
        return chr(i + ord('a') - 1)

    def convertCodeToText(self, li):
        return map(self.convertIntToChar, li)

    def convertTextToCode(self, li):
        return map(self.convertCharToInt, li)

    def decryption(self, ciphertext):
        ciphercode = self.convertTextToCode(ciphertext)
        key = self.key
        plaincode = self.plaincode
        n = len(ciphertext)
        for i in range(n):
            plaincode[(key * i) % n] = (ciphercode[i] + i) % 28
        return self.convertCodeToText(plaincode)

line = raw_input()
while(line != '0'):
    content = line.split()
    cryptography = Cryptography(int(content[0]), len(content[1]))
    print "".join(cryptography.decryption(list(content[1])))
    line = raw_input()
