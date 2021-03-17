"""
Template - Initialize a dictionary my_dict to be empty
"""

# Add code here

my_dict= {}

# Tests
print(type(my_dict))
print(my_dict)

# Output
#<class 'dict'>
#{}

"""
Template - Create a dictionary my_dict that contains 
two specified value/pairs 
"""

# Add code here

my_dict = {"Joe" : 1,"Scott" : 2}

# Tests
print(type(my_dict))
print(my_dict["Joe"])
print(my_dict["Scott"])
print(my_dict)

# Output - note that order of key/values pairs in output is unimportant
#<class 'dict'>
#1
#2
#???

"""
Template - Add the specified key/value pair to an
existing dictionary my_dict
"""

# Initialize dictionary
my_dict = {"Joe" : 1, "Scott" : 2}

# Add key/value pair "John" : 3

my_dict["John"]= 3

# Tests
print(type(my_dict))
print(my_dict["Joe"])
print(my_dict["Scott"])
print(my_dict["John"])
print(my_dict)

# Output - note that order of key/values pairs in output is unimportant
#<class 'dict'>
#1
#2
#3
#{'Scott': 2, 'John': 3, 'Joe': 1}

"""
Template - Write an expression that determines whether
a key is in a dictionary
"""

# Initialize dictionary
my_dict = {"Joe" : 1, "Scott" : 2, "John" : 3}

# Print True/False depending on whether the key "Joe" is in my_dict
print("Joe" in my_dict)

# Print True/False depending on whether the key "John" is in my_dict
print("John" in my_dict)

# Print True/False depending on whether the key "Stephen" is in my_dict
print("Stephen" in my_dict)

# Output
#True
#True
#False

"""
Solution - Write a function is_empty(my_dict) that
returns True if a dictionary is empty and False otherwise
"""


def is_empty(my_dict):
    """
    Given a dictionary my_dict, return True if the 
    dictionary is empty and False otherwise
    """
    # quiz answer was
    # return len(my_dict) == 0
    return not my_dict

# Testing code
print(is_empty({}))
print(is_empty({0 : 1}))
print(is_empty({"Joe" : 1, "Scott" : 2}))

# Output
#True
#False
#False

"""
Template - Write a function value_sum(my_dict) that
returns the sum of the values in a dictionary
"""


def value_sum(my_dict):
    """
    Given a dictionary my_dict whose values are numbers, return 
    the sums of the values in my_dict
    """
    
    total = 0
    
    # Enter code here
    for key in my_dict:
        total += my_dict[key]
        
    return total

# Testing code
print(value_sum({}))
print(value_sum({0 : 1}))
print(value_sum({"Joe" : 1, "Scott" : 2, "John" : 4}))

# Output
#0
#1
#7


"""
Template - Write a function make_dict(key_value_list) that
takes a list of tuples (key, value) and returns a 
dictionary with these keys and values
"""


def make_dict(key_value_list):
    """
    Given a list of tuples of the form (key, value), 
    return a dictionary with the corresponding keys and values
    """
    
    #quiz answer
    
    # Enter code here
    #answer = {}
    #for key, value in key_value_list:
    #    answer[key] = value
    #return answer
    new_dict = dict(key_value_list)
    
    return new_dict

# Testing code
print(make_dict([]))
print(make_dict([(0, 1)]))
print(make_dict([("Joe", 1), ("Scott", 2), ("John", 4)]))

# Output
#{}
#{0: 1}
#{'John': 4, 'Joe': 1, 'Scott': 2}

"""
Template for part 1
Using substitution ciphers to encrypt and decrypt plain text
"""


# Part 1 - Use a dictionary that represents a substition cipher to 
# encrypt a phrase

# Example of a cipher dictionary 26 lower case letters plus the blank
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def encrypt(phrase, cipher_dict):
    """
    Take a string phrase (lower case plus blank) 
    and encypt it using the dictionary cipher_dict
    """
    new_phrase=""
    for char in phrase:
        new_phrase += cipher_dict[char]
    
    return new_phrase

# Tests
print("Output for part 1")
print(encrypt("pig", CIPHER_DICT))
print(encrypt("hello world", CIPHER_DICT))
print()

# Output for part 1
#vif
#hunnybtygnd


# Part 2 - Compute an inverse substitution cipher that decrypts
# an encrypted phrase

def make_decipher_dict(cipher_dict):
    """
    Take a cipher dictionary and return the cipher
    dictionary that undoes the cipher
    """    
    
    decrypt={}
    for char in cipher_dict:
        decrypt[cipher_dict[char]] = char       

    return decrypt

DECIPHER_DICT = make_decipher_dict(CIPHER_DICT)

# Tests - note that applying encrypting with the cipher and decipher dicts
# should return the original results
print("Output for part 2")
print(DECIPHER_DICT)
print(encrypt(encrypt("pig", CIPHER_DICT), DECIPHER_DICT))			      # Uncomment when testing
print(encrypt(encrypt("hello world", CIPHER_DICT), DECIPHER_DICT))	# Uncomment when testing
print()

# Output for part 2 - note order of items in dictionary is not important
#{'p': 'f', 'n': 'l', 'm': 'a', 'i': 'i', 'd': 'd', 'x': 'k', 'b': ' ', 'l': 'v', 'f': 'g', 'o': 's', 'u': 'e', 'a': 'n', 'c': 'y', 'r': 'q', 'e': 'z', 'k': 'c', 'w': 'm', 'g': 'r', 'y': 'o', ' ': 't', 'h': 'h', 'v': 'p', 'j': 'x', 'q': 'u', 't': 'w', 's': 'b', 'z': 'j'}
#pig
#hello world



# Part 3 - Create a random cipher dictionary

import random

def make_cipher_dict(alphabet):
    """
    Given a string of unique characters, compute a random 
    cipher dictionary for these characters
    """
    
    letters = list(alphabet)
    rand_letters = list(alphabet)    
    random.shuffle(rand_letters)
    rand_dict={}
        
    for char in range(len(alphabet)):
        letter = letters[char]
        shuffled_letter = rand_letters[char]
        rand_dict[letter] = shuffled_letter
    return rand_dict
    
# Tests
print("Output for part 3")
print(make_cipher_dict(""))
print(make_cipher_dict("cat"))
print(make_cipher_dict("abcdefghijklmnopqrstuvwxyz "))

# Output for part 3 -  note that answers are randomized
#{}
#{'a': 'a', 't': 'c', 'c': 't'}
#{'a': 'h', 'l': 'u', 'u': 'q', 'b': 'v', 'y': 'a', 'm': 'r', 'p': 'j', 'k': 'e', 'n': 'p', 't': 'x', 'd': 'o', 'c': 'c', 'w': ' ', 'f': 'd', 'r': 'z', 'v': 'l', 's': 'y', 'e': 'b', 'o': 'i', 'x': 'm', 'h': 's', 'i': 'w', 'q': 'g', 'g': 'n', 'j': 'f', 'z': 'k', ' ': 't'}

def count_letters(word_list):
    
    ''' count letters in a dictionary and returns one most appeared'''
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    # enter code here
    for idx in range(len(word_list)):
        for letter in range(len(word_list[idx])):
            letter_found = (word_list[idx][letter])
            #print(word_list[idx][letter])
            letter_count[letter_found] += 1
    
    #print(list(letter_count.keys())[list(letter_count.values()).index(3)]) 
    print("answer is: ", max(letter_count, key=letter_count.get))   
    
    print(letter_count) 

print("")
print("quiz")
count_letters(["hello", "world"])

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
count_letters(monty_words)