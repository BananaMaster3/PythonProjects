# Python Class 2710
# Lesson 1 Problem 7
# Author: isaiah08 (595367)
import math

def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    
#This is a test.
#2
#hssesTi i a tt.
#hsi  etTi sats.
    pt_list = list(plaintext)
    encoded = []
    current_rail = []
    
    for rail in range(numRails):
        for x in range(0, len(pt_list)):
            letter = pt_list[x]

            if x % numRails == rail:
                current_rail.append(letter) 
        encoded.insert(0, ''.join(current_rail))
        current_rail = []
    return ''.join(encoded)

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    
    remainder = len(ciphertext) % numRails
    correct_text = []

    rails = []
    rail_indecies = []
    rail_length = int(math.floor(len(ciphertext)//numRails))
    for x in range(0, numRails):
        if x == 0:
            rail_indecies.append(0)
        else:
            if x > numRails - remainder:
                rail_indecies.append((rail_indecies[x-1]) + rail_length + 1)
            else:
                rail_indecies.append(rail_indecies[x-1] + rail_length)
        
    for num in rail_indecies:
        # If num isn't the last item in the rail_indecies list:
        if num != rail_indecies[-1]:
            y =rail_indecies[rail_indecies.index(num)+1]
            rails.insert(0, ciphertext[num : y])
        else:
            rails.insert(0, ciphertext[num : ])

            
    for x in range(rail_length+1):
        for rail in rails:
            if x < len(rail):
                correct_text.append(rail[x])
    return ''.join(correct_text)
        
            
            
            
        
    
            
        
        

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    words = []
    best_num_of_valid_words = 0
    best_sentence = ''
    for line in open('wordlist.txt', 'r'):
        words.append(line.replace('\n', ''))
    for numRails in range(1, 11):
   
        possible_text = decipher_fence(ciphertext, numRails)
        
        x = possible_text.replace('.', '').replace("'", "")
        current_num_of_valid_words = 0
        for word in x.split():
            if word in words:
                current_num_of_valid_words += 1
        if current_num_of_valid_words > best_num_of_valid_words:
            best_num_of_valid_words = current_num_of_valid_words
            best_sentence = possible_text
    return best_sentence
        

    
    
# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
