"""
Demonstration of defining functions.
"""

def sayhello():
    """
    Prints "hello".
    """
    print("hello")

# Call the function
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
#result = double(6)
#print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2
    prod = prod * value3
    return prod

# Call the function and assign the result to a variable
#result = product(7, 13.3, -1.2)
#print(result)

"""
Demonstration of parameters and variables within functions.
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Return celsius temperature that corresponds to fahrenheit
    temperature input.
    """
    offset = 32
    multiplier = 5 / 9
    celsius = (fahrenheit - offset) * multiplier
    print("inside function:", fahrenheit, offset, multiplier, celsius)
    return celsius

"""
Template - Compute the number of feet corresponding to a number of miles.
"""

###################################################
# Miles to feet conversion formula
# Student should enter function on the next lines.

def miles_to_feet(miles):
    feet = 5280 * miles    
    return feet

###################################################
# Tests
# Student should not change this code.


'''miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
'''

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#13 miles equals 68640 feet.
#57 miles equals 300960 feet.
#82.67 miles equals 436497.6 feet.

"""
Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter function on the next lines.
def total_seconds(hours, minutes, seconds):
    total_seconds = ((hours*3600) + (minutes*60)+ seconds)
    return total_seconds

###################################################
# Tests
# Student should not change this code.
'''
hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")'''

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.

"""
Solution - Compute the length of a rectangle's perimeter, given its width and height.
"""

###################################################
# Rectangle perimeter formula
# Student should enter function on the next lines.
def rectangle_perimeter(width, height):
    """
    Returns the perimeter of a rectangle with the given width and height.
    """
    perimeter = ((2*width)+(2*height))
    return perimeter


###################################################
# Tests
# Student should not change this code.


'''width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")
'''

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
#A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
#A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.


"""
Template - Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula
# Student should enter function on the next lines.

def rectangle_area(width,height):
    area = (width * height)
    return area


###################################################
# Tests
# Student should not change this code.

'''width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
'''
    
###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
#A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
#A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.


"""
Template - Compute the area of a circle, given the length of its radius.
"""

# Import the math module to access the exact value of pi
def circle_area(radius):
    import math
    PI = math.pi
    area = (PI*(radius**2))
    return area

###################################################
# Circle area formula
# Student should enter function on the next lines.




###################################################
# Tests
# Student should not change this code.
'''
radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")
'''

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A circle with a radius of 8 inches has an area of 201.06192983 square inches.
#A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
#A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.

"""
Template - Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function
# Student should enter function on the next lines.

''' my solution 
def print_digits(number):
    tens = int(number /10)
    ones = number - int(tens*10)
    print ("The tens digit is " + str(tens) + ", and the ones digit is " + str(ones) + ".")

course solution'''
def print_digits(number):
    """
    Prints the tens and ones digit of an integer in [0,100).
    """
    
    print("The tens digit is " + str(number // 10) + ", and the ones digit is " + 
          str(number % 10) + ".")
    
###################################################
# Tests
# Student should not change this code.

print_digits(42)
print_digits(99)
print_digits(5)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The tens digit is 4, and the ones digit is 2.
#The tens digit is 9, and the ones digit is 9.
#The tens digit is 0, and the ones digit is 5.


"""
Template - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    import random
    num1 = random.randrange(1,60)
    num2 = random.randrange(1,60)
    num3 = random.randrange(1,60)
    num4 = random.randrange(1,60)
    num5 = random.randrange(1,60)
    powerball = random.randrange(1,36)
    print ("Today's numbers are " + str(num1) +", " + str(num2)+", " + str(num3)+", " + str(num4)+", " + str(num5)+", and the Powerball is " + str(powerball))

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)

project_to_distance(2, 7, 4)

def do_stuff():
    """
    Example of print vs. return
    """
    print("Hello world")
    return "Is it over yet?"
    print("Goodbye cruel world!")

print(do_stuff())


##########################################
#answer to quiz question

def quiz_function1(x):
    f = ((-5*(x**5)) + (67*(x**2))) - 47
    print (f)

quiz_function1(0)
quiz_function1(1)
quiz_function1(2)
quiz_function1(3)

def quiz_function2(present_value, annual_rate, periods_per_year, years):
    """
    Input: the numbers present_value, annual_rate, periods_per_year, years
    Output: future value based on formula given in question
    """
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Put your code here.
    final_yield = present_value*((1+rate_per_period)**periods)
    return final_yield

print("$1000 at 2% compounded daily for 4 years yields $", quiz_function2(1000, .02, 365, 4))   
print("$500 at 4% compounded daily for 10 years yields $", quiz_function2(500, .04, 10, 10))   

def quiz_function3(side):
    import math
    area = ((math.sqrt(3)/4)*side**2)
    print (area)


quiz_function3(2)
quiz_function3(5)


def max_of_2(val1, val2):
    if val1 > val2:
        return val1
    else:
    return val2

def max_of_3(val1, val2, val3):
    return max_of_2(val1, max_of_2(val2, val3))
