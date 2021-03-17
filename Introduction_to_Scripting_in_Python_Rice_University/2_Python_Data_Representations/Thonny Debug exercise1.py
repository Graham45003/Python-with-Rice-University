"""
Simple program illustrating the debugger in Thonny
"""

## Under Run menu in Thonny
##    Select "Debug current script" to start debugger
##    Select "Step over" to evaluate currently highlighted code
##    Select "Step into" to evaluate pieces of highlighted code
##    Select "Step out" to complete evaluation of enclosing code
##    Select "Run to cursor" to step evaluation to the current cursor location (breakpoint)
##    Select "Interrupt/Reset" to exit debugger

print('Hello' + ' ' + 'Thonny' + '!')

print()

print("The secret number is ", 1 + 2 * 3)

"""
Example of program that use a loop to compute the minimum number in a list
"""


def list_minimum(numbers):
    """
    Compute the minimum of a list of numbers
    """
    
    min_num = float("inf") #infinity
    for num in numbers:
        if num < min_num:
            min_num = num  # Set "Run to cursor" on this line
    return min_num

def run_example():
    """
    Run an example using list_minimum
    """
    example_list = [4.6, 5.9, 2.1, 5.7, 1.1, 8.3]
    print("An example list is", example_list)
    print()
    minimum_number = list_minimum(example_list)
    print("The minimum of this example list is", minimum_number)

run_example()