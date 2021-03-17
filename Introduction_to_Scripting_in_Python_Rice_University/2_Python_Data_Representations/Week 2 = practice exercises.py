"""
Template- Create a list of the first six primes and print the 2nd, 4th, and 6th
"""

# Enter code here

primelist = [1, 3, 5, 7, 11, 13]

# two solutions

print (primelist[1], primelist[3], primelist[5])

for num in range(len(primelist),2):
    print(primelist[num])

# Output
#3 7 13

"""
Template - Create a list formed by the first and last items of example_list
"""

example_list = [2, 3, 5, 7, 11, 13]

# Uncomment and complete

firstlast_list = [example_list[0], + example_list[-1]]
print(firstlast_list)


# Output
#[2, 13]

"""
Template - Create a list formed by excluding the first and last items of example_list
"""

# Enter code here

example_list = [2, 3, 5, 7, 11, 13]

# Uncomment and complete
middle_list = example_list[1:5]
print(middle_list)
middle_list = example_list[1:-1]
print(middle_list)

# Output
#[3, 5, 7, 11]

"""
Template - Create a list formed by 8 copies of True and 8 copies of False
"""

# Uncomment and enter code here

truefalse_list = [True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]
print(truefalse_list)

#answer
truefalse_list = 8 * [True] + 8 * [False]
print(truefalse_list)

# Output
#[True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]

"""
Template - Create a list of words form a string consisting of words separated by spaces
"""

# Uncomment and enter code here

quote = "Bring me a shrubbery"
word_list = quote.split(" ")
print(word_list)


# Output
#['Bring', 'me', 'a', 'shrubbery']

"""
Template - Count the number of times that a word appears in string of text
"""

def word_count(text, word):
    """
    Given a string text consist of words separate by spaces and a string word
    (with no spaces), return the number of times that word appears in the text
    """
    
    #answer
    word_list = text.split(" ")
    return (word_list.count(word))
    
    #return (text.count(word)) - deoesn't work
    
# Tests

print(word_count("this pigdog is a fine pigdog", "pigdog"))
print(word_count("this pigdog is not a dog", "dog"))
print(word_count("this pigdog is not a pig", "pigdog"))

# Output
#2
#1
#1


"""
Template - Analyze another example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)

# Explain what happens to list1 in a comment

# Answer - list1 and list2 are two references to distinct lists
# Updating an item in one list does not affect the second list


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]


"""
Template - Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    maxnum = 0
    
    for num in numbers[0:]:
        if num > maxnum:
            maxnum = num
    return maxnum       

# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))

"""
Template - Take a list of integers and concatenate their digits
"""

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    digits = ""
    for number in int_list:
        digits += str(number)
    return int(digits)

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000


# Output
#4
#4
#7
#5