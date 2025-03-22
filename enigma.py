#!/usr/bin/env python3

# The Enigma machine.
# ===================
# The Enigma machine was a sophisticated encryption device used by Nazi Germany during World War II.
# It employed a series of rotors, a plugboard, and a reflector to scramble and encode messages.
# Its constantly changing settings made decrypting messages without knowledge of the specific settings 
# extremely difficult, contributing to its reputation as one of the most secure encryption 
# machines of its time.

import hashlib
import random
import string

class Enigma:
    # Initialize veriables.
    def __init__(self, reflector, plugboard, charset, limit):
        self.rotors = {"I": 0, "II": 0, "III": 0}
        self.rotor_scramble = random.randint(1, 1000)
        self.reflector = {} if reflector else None
        self.plugboard = {} if plugboard else None
        self.charset = charset
        self.limit = limit
        self.alphabet = list(string.ascii_lowercase)
    
    # Hash a combination of rotor settings and substitute characters in a message 
    # using the resulting cipher.
    def hash_and_sub(self, I, II, III, msg):
        combined_result = str(I) + str(II) + str(III)
        hashed_result = hashlib.sha256(combined_result.encode()).hexdigest()
        random.seed(int(hashed_result, 16))
        # Shuffle the 'self.alphabet' variable with the seed of the previously generated hash
        # and for each character in the 'msg' variable, substitute it for a letter in the shuffled alphabet.
        random.shuffle(self.alphabet)
        sub_cipher = {char: substitution for char, substitution in zip(string.ascii_lowercase, self.alphabet)}
        encrypted_msg = "".join(sub_cipher.get(char, char) for char in msg.lower())
        return encrypted_msg
    
    # For each character in the 'self.alphabet' variable, create a random pair and append it to the
    # 'self.plugboard' variable.
    def initialize_plugboard(self, alphabet, plugboard):
        if plugboard == {}:
            for char in alphabet:
                pair = random.randint(1, 5)
                if not alphabet.index(char) + pair > len(alphabet):
                    plugboard[f"{char}"] = alphabet.index(char) + pair
                else:
                    plugboard[f"{char}"] = alphabet.index(char) - pair
    
    # Encrypt by changing the rotors' value by the 'self.rotor_scramble' variable
    # (scrambled electrical current) and hash the charset corresponding to the value of the rotors.
    def encrypt(self):
        self.rotors["I"] += self.rotor_scramble
        self.rotors["II"] += self.rotor_scramble / self.limit
        self.rotors["III"] += self.rotor_scramble / (self.limit * 10)
        # Add values to reflector.
        if self.reflector == {}:
            self.reflector["Rotors"] = [self.rotors["I"], self.rotors["II"], self.rotors["III"]]
            self.reflector["Limit"] = [self.limit, self.limit * 10]
        # Divide the rotors' value by 10 until its value does not exceed that of
        # the 'self.alphabet' variable.
        while not self.rotors["I"] < len(self.alphabet) and self.rotors["II"] < len(self.alphabet) and self.rotors["III"] < len(self.alphabet):
            divisor = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
            if self.rotors["I"] <= len(self.alphabet):
                divisor[0] = 1
            elif self.rotors["II"] <= len(self.alphabet):
                divisor[1] = 1
            elif self.rotors["III"] <= len(self.alphabet):
                divisor[2] = 1
            self.rotors["I"] /= divisor[0]
            self.rotors["II"] /= divisor[1]
            self.rotors["III"] /= divisor[2]
        # Modify the charset with the 'hash_and_sub' function and set the value
        # of the 'new_charset' to that of the modified charset variable
        new_charset = self.hash_and_sub(self.rotors["I"], self.rotors["II"], self.rotors["III"], self.charset)
        # Call the initialize_plugboard function for decryption if necessary.
        self.initialize_plugboard(self.alphabet, self.plugboard)
        self.reflector["Charset"] = new_charset
        self.reflector["Pairs"] = self.plugboard
        # Further encryption if the plugboard is enabled
        if not plugboard == {}:
            return new_charset
        else:
            for char in new_charset:
                if not char.isalnum():
                    new_charset.replace(char, self.plugboard[char])
    
    # Continually loop over every rotor position that is possible and return a sequence of integers
    # equivalent to the settings of encryption
    def decrypt_brute_force(self, encrypted_msg):
        # Iterate over all possible rotor positions and plugboard settings
        for rotor1 in range(len(self.alphabet)):
            for rotor2 in range(len(self.alphabet)):
                for rotor3 in range(len(self.alphabet)):
                    for plugboard_setting in range(1, 6):
                        # Set the rotor positions
                        self.rotors["I"] = rotor1
                        self.rotors["II"] = rotor2
                        self.rotors["III"] = rotor3
                        
                        decrypted_msg = self.find_plugboard_settings(encrypted_msg)
        return decrypted_msg

    # Find reversed characters (plugboard)
    def find_plugboard_settings(self, encrypted_msg):
            # Perform decryption
            decrypted_msg = ""
            for char in encrypted_msg.lower():
                if char.isalnum():
                    decrypted_msg += str(self.reflector["Pairs"][char])
                else:
                    decrypted_msg += char
            return decrypted_msg
        
    
    
plugboard = True
reflector = True
charset = "Hello, World"
limit = 10
enigma = Enigma(reflector, plugboard, charset, limit)
encrypted_charset = enigma.encrypt()
print(encrypted_charset)
print(enigma.decrypt_brute_force(encrypted_charset))