"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    
    
    if len(line1) != len(line2):
        if len(line1) > len(line2):
            maxlength = (line1)
            linelength = len(line2)
        else:                    
            maxlength = len(line2)
            linelength = len(line1)
    else:
        maxlength = len(line1)
        linelength = len(line1)
        
    lineindex = 0
    
    for idx in range(linelength):
        if line1[idx] == line2[idx]:
            lineindex = idx
        else:
            lineindex = idx
            return lineindex
        
    if linelength == maxlength:
        return IDENTICAL
    else:
        if linelength == 0:
            return lineindex
        else:
            return lineindex + 1
        
#print(singleline_diff("line2", "lne2"))
    
def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx < 0 or idx > len(line2) or idx > (len(line1)+1):
        return ""
     
    newline = "\n"
    equals = ("=" * idx) + "^"
    return line1 + newline + equals + newline + line2 + newline

#print(singleline_diff_format("abc", "abcd", 3))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
        
    #find length of two lists and which one smallest   
    len1 = len(lines1)
    len2 = len(lines2)
    small = min(len1, len2) 
    
    #tracks if identical or what idx list is not
    score = []
    idenscore = -1
    
    #checks lines and stores score
    for idx1 in range(small): 
        result = singleline_diff(lines1[idx1], lines2[idx1])
        if result == -1:
            score.append([idx1, IDENTICAL])
        else:
            idenscore = 0
            score.append([idx1, result])
    
    #firstly checks if all identical if not returns score
    if idenscore == -1:
        if len1 == len2:
            return (IDENTICAL, IDENTICAL)
        else:
            return (max(len1, len2) -1, 0)
    else:
        for idx2 in range(small):
            if score[idx2][1] != -1:
                return (idx2, score[idx2][1])
    
    
            
#print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
        
    with open(filename, 'r') as opened_file:
        filelist = opened_file.read().splitlines()
    
    opened_file.close()
    
    return filelist

#print(get_file_lines("file1.txt"))

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
        
    returnvalue = ""
    file1 = get_file_lines(filename1)
    file2 = get_file_lines(filename2)
    
    if len(file1) == 0 and len(file2) == 0:
        return "No differences\n"
    elif len(file1) == 0:
        return "Line 0"  ":\n" + str(file2[0]) + "\n^\n\n"
    elif len(file2) == 0:
        return "Line 0"  ":\n" + str(file1[0]) + "\n^\n\n" 
    else:
        pass
    
    file_diff = multiline_diff(file1, file2)
    
    idx1, idx2 = file_diff
    
    if idx1 == idx2 == -1:
        returnvalue = "No differences\n"
    else:
        returnvalue = "Line " + str(idx1) + ":\n"
        returnvalue += singleline_diff_format(file1[idx1], file2[idx1], idx2)
    
    return returnvalue

#print(file_diff_format("file1.txt", "file3.txt"))