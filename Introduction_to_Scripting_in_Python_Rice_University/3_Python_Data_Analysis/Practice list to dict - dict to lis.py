def convert_list2dict(gpalist):
    """
    Input: gpalist - list of (student name, gpa) tuples
    Output: a dictionary mapping student names to their gpa
    """
    result = {}
    for item in gpalist:
        result[item[0]] = item[1]
    return result

def convert_dict2list(gpadict):
    """
    Input: gpadict dict of studen with gpa
    Output: a list of tuples student name, gpa
    """
    return [(key,values) for key,values in dict.items()]
    

dict = convert_list2dict([("Tamika Barker", 3.9), ("Elmer Brasher", 2.8), ("Raymond Hathaway", 3.3), ("Rebekah Bailey", 3.5)])
print("dict ",dict)

list = convert_dict2list(dict)
print("list", list)