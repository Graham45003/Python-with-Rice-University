"""
Template - String examples
"""

# Fix the four string definitions below.

string1 = "It's just a flesh wound"
string2 = "It's just a flesh wound"	
string3 = "It's just a flesh wound"	
string4 = "'It's just a flesh wound'"

print(string1)
print(string2)
print(string3)
print(string4)

"""
Template - Item selection for lists
"""

# Create a string formed by selecting the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[0] + example_string[-1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#Id

"""
Template - Slice selection for lists
"""

# Create a string formed by selecting all but the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[1:-1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#t's just a flesh woun

"""
Template - Another example of slice selection for lists
"""

# Create a string formed by selecting the first three characters of example_string
# plus the last three characters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[:3] + example_string[-3:]
print(solution_string)

# Output should be 
#It's just a flesh wound
#It'und

"""
Template - Echo a string multiple times to the console
"""

def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    
    print((call + "\n") * repeats)


# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye

"""
Template - Function that tests for substring
"""


def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    """

    # enter one line of code for substring test here
    
    return test_string in example_string

# Tests

example_string = "It's just a flesh wound."

print(is_substring(example_string, "just"))
print(is_substring(example_string, "flesh wound"))
print(is_substring(example_string, "piddog"))
print(is_substring(example_string, "it's"))
print(is_substring(example_string, "It's"))

# Output

#True
#True
#False
#False
#True


"""
Template - Function that uses format to create a nametag
"""


def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name 
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    
    # enter code here
    
    return "Hi my name is {}. This lecture cover {}.".format(first_name, topic)

    
# Tests

print(make_nametag("Scott", "Python"))
print(make_nametag("Joe", "games"))
print(make_nametag("John", "programming tips"))


# Output

#Hi! My name is Scott. This lecture covers Python.
#Hi! My name is Joe. This lecture covers games.
#Hi! My name is John. This lecture covers programming tips.


"""
Solution - Function that checks whether a string can be converted to an integer
"""


def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all 
    digits are decimal digits.  Other return -1.
    """
    
    if int_string.isdigit():
        return int(int_string)
    else:
        return -1
    
# Test

print(make_int("123"))
print(make_int("00123"))
print(make_int("1.23"))
print(make_int("-123"))


# Output

#123
#123
#-1
#-1


"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    
    '''
    my way
    first = name_string.split()[0]
    last = name_string.split()[-1]
    return str.title(last + " " + first)
    '''
    
    '''
    coursera
    '''
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()
    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John


def count_vowels(word):
       
    a_string = "a"
    e_string = "e"
    i_string = "i"
    o_string = "o"
    u_string = "u"
    
    return word.count(a_string) + word.count(e_string)+ word.count(i_string)+ word.count(o_string)+ word.count(u_string)


print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

def demystify(l1_string):

    new_string = l1_string.replace("1", "b")
    new_string = new_string.replace("l", "a")
    return new_string

    
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
