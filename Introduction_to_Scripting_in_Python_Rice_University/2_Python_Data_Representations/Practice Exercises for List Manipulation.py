"""
Template - Update an item in a list
"""
print()
print("update")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

example_list[2] =  0
print(example_list)

# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 0, 7, 11, 13]

"""
Template - Update a slice of a list
"""
print()
print("slice")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

#example_list[1]=0
#example_list[2]=0
#example_list.insert(2,0)
example_list[1:3]=[0,0,0]
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]

"""
Template - Append an item to a list
"""
print()
print("append")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

example_list.append(0)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0]

"""
Template - Extend a list with another list
"""
print()
print("extend")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

#lst=[0,0,0]
#example_list.extend(lst)

example_list.extend([0,0,0])
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

"""
Template - Concatenate one list onto another
"""
print()
print("concatenate")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

#lst=[0,0,0]
#new_list = list(example_list)
#new_list.extend(lst)

new_list = example_list + [0,0,0]

print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

"""
Template - Append several item to a list
"""
print()
print("loop")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

for num in range(3):
    example_list.append(0)

#or
#for number in [0, 0, 0]:
    #example_list.append(number)
    
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

"""
Template - Convert a list to a tuple
"""
print()
print("tuple")
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

example_tuple = tuple(example_list)
    
print(example_tuple)


# Output
#[2, 3, 5, 7, 11, 13]
#(2, 3, 5, 7, 11, 13)

"""
Template - Shuffle the items in a list
"""
print()
print("shuffle")
import random
example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

random.shuffle(example_list)
   
print(example_list)


# Output - note that order of second list may vary due to randomness
#[2, 3, 5, 7, 11, 13]
#[11, 2, 7, 5, 13, 3]

"""
Template - Flatten a nested list
"""
print()
print("flatten")
def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    newlist=[]
    for item in nested_list:
        newlist.extend(item)
    
    return newlist

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

"""
Template - Remove duplicates from a list while preserving the order of items
"""

print()
print("duplicates")
def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """

    no_duplicates = []
    for item in items:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return no_duplicates

# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']