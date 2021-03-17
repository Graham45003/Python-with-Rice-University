"""
Template - Create a list nested_list consisting of five empty lists
"""

# Add code here
nested_list = [[],[],[],[],[]]

# Tests
print(nested_list)

# Output
#???

"""
Template - Create a list nested_list of length 5 whose items 
are themselves lists consisting of 3 zeros
"""

# Add code here
nested_list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# Tests
print(nested_list)

# Output
#???

"""
Template- Create a list zero_list consisting of 3 zeroes using a list comprehension
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

As a challenge, redo the previous problem using a nested list comprehension
https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
"""

print("zero_list")

# Add code here for a list comprehension
zero_list = [0 for dummy_idx in range(3)]
    
# Add code here for nested list comprehension
nested_list = [[0 for dummy_idx1 in range(3)] for dummy_idx2 in range(5)]


# Tests
print(zero_list)
print(nested_list)

# Output
#[0, 0, 0]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

"""
Template - Select a specific item in a nested list
"""

# Define a nested list of lists
nested_list = [[col + 3 * row for col in range(3)] for row in range(5)]
print(nested_list)

# Add code to print out the item in this nested list with value 7
print(nested_list[2][1])

# Output
#[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14]]
#7

"""
Solution - Analyze a reference issue involving a nested list
"""

# Create a nested list
zero_list = [0, 2, 0]
nested_list = []
for dummy_idx in range(5):
    # nested_list.append(zero_list)
    nested_list.append(list(zero_list))    # Corrected code
print(nested_list)
    
# Update an entry to be non-zero
nested_list[2][1] = 7
print(nested_list)


# Erroneous output
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

# Desired output
# [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
# [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]


# Explanation

# Line 13 is unintentionally updating all 5 entries in nested_list due to a referencing issue.

# Line 9 is creating five references to the SAME onject (the list zero_list) in nested_list.
# Thus, updating one reference to zero_list in nested_list in line 13 updates 
# the other four references to zero_list in nested_list simultaneously. 

# To visualize this reference issue in Python Tutor, visit the URL https://goo.gl/hT4MM3.
# Note the entries in nested_list all refer to SAME list.  

# The solution to this problem is to make a NEW copy of zero_list each  time append()
# is executed. To do this, simply replace zero_list by list(zero_list) in line 9

# To visualize corrected code in Python Tutor, visit the URL https://goo.gl/4nifEg.
# Note that each entry in nested_list now refers to a DISTINCT list.  As a result,
# updates to one item in nested_list do not affect any other part of nested_list.

# Erroneous output
#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0], [0, 7, 0]]

# Desired output
# [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]]
# [[0, 2, 0], [0, 2, 0], [0, 7, 0], [0, 2, 0], [0, 2, 0]]


"""
Template - Create a list list_dicts of 5 empty dictionaries
"""

# Add code here
list_dicts = [{},{},{},{},{}]

# Tests
print(list_dicts)


# Output
#???

"""
Template - Write a function dict_copies(my_dict, num_copies) that 
returns a list consisting of num_copies copies of my_dict
"""


# Add code here
def dict_copies(my_dict, num_copies):
    """
    Given a dictionary my_dict and an integer num_copies, 
    returns a list consisting of num_copies copies of my_dict.
    """
    
    dict_answer = []
    for idx in range(num_copies):
        dict_answer.append(dict(my_dict))    # Corrected code
    return dict_answer


# Tests
print(dict_copies({}, 0))
print(dict_copies({}, 1))
print(dict_copies({}, 2))

test_dict = dict_copies({'a' : 1, 'b' : 2}, 2)
print(test_dict)

# Check for reference problem
test_dict[1]["a"] = 3
print(test_dict)



# Output
#[]
#[{}]
#[{}, {}]
#[{'a': 1, 'b': 2}, {'b': 2, 'a': 1}]
#[{'b': 2, 'a': 1}, {'b': 2, 'a': 3}]

# Note that you have a reference issue if the last line of output is
#[{'a': 3, 'b': 2}, {'b': 2, 'a': 3}]


"""
Solution - Write a function make_dict_lists(length) that returns a dictionary whose keys are in range(length) and whose
corresponding values are lists of zeros with length matching the key
"""


# Add code here
def make_dict_lists(length):
    """
    Given an integer length, return a dictionary whose keys
    lie in range(length) and whose corresponding values are 
    lists of zeros with length matching the key
    """
    dict_answer = {}
    for idx in range(length):
        dict_answer[idx] = [0] * idx
    return dict_answer

# Tests
print(make_dict_lists(0))
print(make_dict_lists(1))
print(make_dict_lists(5))


# Output
#{}
#{0: []}
#{3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}

"""
Template - Create a dictionary grade_table whose keys are provided
student names and values are associated list of grades
"""


# Add code here
grade_table = {"Joe":[100,98,100,13],
               "Scott":[75,59,89,77],
               "John":[86,84,91,78],
               }


# Tests
print(grade_table["Joe"])
print(grade_table["Scott"])
print(grade_table["John"])


# Output
#[100, 98, 100, 13]
#[75, 59, 89, 77]
#[86, 84, 91, 78]

"""
Template - Create a function make_grade_table(name_list, grades_list) 
whose keys are the names in names and whose values are the
lists of grades in grades
"""


# Add code here

def make_grade_table(name_list, grades_list):
    """
    Given a list of name_list (as strings) and a list of grades
    for each name, return a dictionary whose keys are
    the names and whose associated values are the lists of grades
    """

    items = dict(zip(name_list, grades_list))
    
    return items
    
# Tests
print(make_grade_table([], []))

name_list = ["Joe", "Scott", "John"]
grades_list = [100, 98, 100, 13], [75, 59, 89, 77],[86, 84, 91, 78] 
print(make_grade_table(name_list, grades_list))


# Output
#{}
#{'Scott': [75, 59, 89, 77], 'John': [86, 84, 91, 78], 'Joe': [100, 98, 100, 13]}


my_dict = {0 : 0, 5 : 10, 10 : 20, 15 : 30, 20 : 40}
#my_dict[25]
my_dict.get(25)

NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
for row in my_matrix:
    print(row)

print(my_matrix[1][4])

sum_trace=0
for i in range(25):
    sum_trace += my_matrix[i][i]
    
print(sum_trace)

NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)
 
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end = " ")
    print()
    
for key,value in my_dict.items():
    value = my_dict[key]
    print(value)