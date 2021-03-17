"""
Template - Compute whether an integer is even.
"""

###################################################
# Is even formula
# Student should enter function on the next lines.

def is_even(even_number):
    return (even_number % 2) ==0


###################################################
# Tests
# Student should not change this code.

number = 8
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 3
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 12
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#8 is even.
#3 is odd.
#12 is even.


"""
Template - Compute whether a person is cool.
"""

###################################################
# Is cool formula
# Student should enter function on the next lines.

''' my version
def is_cool(persons_name):
    if persons_name == "Joe":
        return True
    elif persons_name == "John":
        return True
    elif persons_name == "Stephen":
        return True
    else:
        return False'''

'''solution'''
def is_cool(name):
    return (name == "Joe") or (name == "John") or (name=="Stephen")

###################################################
# Tests
# Student should not change this code.

name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe is cool.
#John is cool.
#Stephen is cool.
#Scott is not cool.


"""
Template - Compute whether the given time is lunchtime.
"""

###################################################
# Is lunchtime formula
# Student should enter function on the next lines.
def is_lunchtime(hour, is_am):
    return (hour == 11 and is_am) or (hour == 12 and not is_am)


###################################################
# Tests
# Student should not change this code.

def is_lunchtime_test(hour, is_am):
    """Tests the is_lunchtime function."""
    print(hour, end = "")
    if is_am:
        print(" AM", end = "")
    else:
        print(" PM", end = "")
    if is_lunchtime(hour, is_am):
        print(" is lunchtime.")
    else:
        print(" is not lunchtime.")

is_lunchtime_test(10, True)
is_lunchtime_test(11, True)
is_lunchtime_test(12, True)
is_lunchtime_test(11, False)
is_lunchtime_test(12, False)
is_lunchtime_test(10, False)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#11 AM is lunchtime.
#12 AM is not lunchtime.
#11 PM is not lunchtime.
#12 PM is lunchtime.
#10 PM is not lunchtime.

"""
Template - Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula
# Student should enter function on the next lines.

def is_leap_year(year):
    return ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0))
        


###################################################
# Tests
# Student should not change this code.

year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.

"""
Template - Compute whether two intervals intersect.
"""

###################################################
# Interval intersection formula
# Student should enter function on the next lines.

def interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    return (int2_lower <= int1_upper) and (int1_lower <= int2_upper)

###################################################
# Tests
# Student should not change this code.

int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 1, 2, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 2, 3
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 2, 3, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 3, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Intervals [0, 1] and [1, 2] intersect.
#Intervals [1, 2] and [0, 1] intersect.
#Intervals [0, 1] and [2, 3] do not intersect.
#Intervals [2, 3] and [0, 1] do not intersect.
#Intervals [0, 3] and [1, 2] intersect.


"""
Template - Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula
# Student should enter function on the next lines.

def name_and_age(name, age):
    if age < 0:
        return "Error: Invalid age"
    else:
        return name + " is " + str(age) + " years old"


###################################################
# Tests
# Student should not change this code.

name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", -46
print(name_and_age(name, age))



###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe Warren is 56 years old.
#Scott Rixner is 40 years old.
#Error: Invalid age

"""
Template - Compute instructor's last name, given the first name.
"""

###################################################
# Name lookup formula
# Student should enter function on the next lines.

def name_lookup(first_name):
    if first_name == "Joe":
        return "Warren"
    elif first_name == "Scott":
        return "Rixner"
    elif first_name == "John":
        return "Greiner"
    elif first_name == "Stephen":
        return "Wong"
    else:
        return "Error: Not an instructor"

###################################################
# Tests
# Student should not change this code. 
    
first_name = "Joe"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Scott"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "John"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Stephen"
print(first_name + "'s last name is", name_lookup(first_name))
      
first_name = "Mary"
print(first_name + "'s last name is", name_lookup(first_name))
      

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#Joe's last name is Warren
#Scott's last name is Rixner
#John's last name is Greiner
#Stephen's last name is Wong
#Mary's last name is Error: Not an instructor

"""
Template - Compute a (simplified) Pig Latin version of a word.
"""

###################################################
# Pig Latin function
def pig_latin(word):
    """
    Returns the (simplified) Pig Latin version of the word.
    """

    # Partial code for body
    first_letter = word[0]
    rest_of_word = word[1 : ]

    # Student should complete function on the next lines
    
    if (first_letter == "a" or first_letter == "e" or first_letter == "i" or
        first_letter == "o" or first_letter == "u"):
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"

###################################################
# Tests
# Student should not change this code.
    
word = "pig"
print(pig_latin(word))

word = "owl"
print(pig_latin(word))

word = "python"
print(pig_latin(word))

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#igpay
#owlway
#ythonpay


"""
Template - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.

def smaller_root(coeff_a, coeff_b, coeff_c):
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant < 0 or coeff_a == 0:
        print("Error: No real solutions")
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if coeff_a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-coeff_b + smaller) / (2 * coeff_a)

###################################################
# Tests
# Student should not change this code.

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None



##### collatz sequence
'''
The Collatz conjecture is an example of a simple computational process
whose behavior is so unpredictable that the world's best mathematicians still don't understand it.
Consider the simple function f(n)f(n) (as defined in the Wikipedia page above) that
takes an integer nn and divides it by two if nn is even and multiplies nn by 33
and then adds one to the result if nn is odd. The conjecture involves studying
the value of expressions of the form f(f(f(...f(f(n)))))f(f(f(...f(f(n))))) as the
number of calls to the function ff increases. The conjecture is that, for any
non-negative integer nn, repeated application of ff to nn yields a sequence of
integers that always includes 11.

Your task for this question is to implement the Collatz function ff in Python.
The key to your implementation is to build a test that determines whether nn is
even or odd by checking whether the remainder when nn is divided by 22 is either
zero or one. Hint: You can compute this remainder in Python using the remainder
opertor \color{red}{\verb|%|}% via the expression \color{red}{\verb|n % 2|}n % 2.
Note you will also need to use integer division \color{red}{\verb|//|}// when computing ff.

Once you have implemented ff, test the your implementation on the expression
f(f(f(f(f(f(f(674)))))))f(f(f(f(f(f(f(674))))))).
This expression should evaluate to 190190. Finally, compute the value of the
expression f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
and enter the result below as an integer. Remember to use copy and paste when moving
the expressions above into your Python environment. Never try to retype expressions by hand.
'''

def f(n):
    return n // 2 if n % 2 == 0 else 3*n + 1


print (f(f(f(f(f(f(f(674))))))))
print (f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))

def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """
    
    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True


bool1 = True
bool2 = False
nand(bool1 , bool2)
