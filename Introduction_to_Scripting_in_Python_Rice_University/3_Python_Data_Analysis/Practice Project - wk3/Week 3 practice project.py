"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""


import csv



#########################################################
# Part 1 - Week 3



def print_table(table):
    """
    Echo a nested listto the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    
    ## my answer
    #import_list = []
    #with open(file_name, "r") as csvfile:
    #    for line in csvfile:
    #        line = line.rstrip()
    #        columns = line.split(',')
    #        import_list.append(columns)
    #return import_list

    # course answer
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table
    

def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)
    
    pass

        
def test_part1_code():
    """
    Run examples that test the functions for part 1
    """
    
    # Simple test for reader
    test_table = read_csv_file("test_case.csv")  # create a small CSV for this test
    print_table(test_table)
    print()

    # Test the writer
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
    cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")
      
    # Test whether two tables are the same

    # Test whether two tables are the same
    for row in range(len(cancer_risk_table)):
        for col in range(len(cancer_risk_table[0])):
            if cancer_risk_table[row][col] != cancer_risk_copy[row][col]:
                print("Difference at", row, col, cancer_risk_table[row][col], cancer_risk_copy[row][col])
            
            

test_part1_code()

