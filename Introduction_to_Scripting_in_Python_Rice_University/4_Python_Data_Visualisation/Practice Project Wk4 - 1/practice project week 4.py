"""
Week 4 practice project solution for Python Data Visualization
Load a county-level PNG map of the USA and plot cancer-risk data at county centers
"""

import math
import csv
import matplotlib.pyplot as plt
import matplotlib as mpl
#import matplotlib.colorbar as colorbar


# Size of SVG image of USA
USA_SVG_SIZE = [555, 352]


# Provided code for week 4

def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Nested list consisting of the fields in the CSV file
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table


# Code to compute area of plot point for scatter()
#smaller number makes bigger circle
SCATTER_SCALE = math.pi / (200.0 ** 2)

def compute_county_cirle(county_population):
    """
    Given county population as integer,
    Compute area of circle proportional to population for use as option to scatter() in matplotlib
    """
    return  SCATTER_SCALE * county_population


# Part 2 - use colormap to define a function that takes risk and returns an RGB color

MAX_LOG_RISK = math.log(1.50E-04, 10)    # maximum cancer risk in table
MIN_LOG_RISK = math.log(8.60E-06, 10)    # minimum cancer risk in table

def create_riskmap(colormap):
    """
    Initialize the colormap "jet" from matplotlib,
    Return function that takes risk and returns RGB color for use with scatter() in matplotlib
    """
    
    # Note that this code is tricky - remember to return a lambda expression
    risk_norm = mpl.colors.Normalize(vmin = MIN_LOG_RISK, vmax = MAX_LOG_RISK)
    color_mapper = mpl.cm.ScalarMappable(norm = risk_norm, cmap = colormap)
    return lambda risk : color_mapper.to_rgba(math.log(risk, 10))
    # creates a function using a scaled colour, there are a lot of different jets to use
    # using math.log to sclae the number not leaving as the original high number
    


# Part 3 - load CSV file and PNG image of USA and then draw cancer-risk ata county centers

RISK_COLUMN = 4 # data column for cancer data

def draw_cancer_risk_map(joined_csv_name, map_name, num_counties = None):
    """
    Given names of joined CSV file and PNG map of USA, draw cancer-risk data for counties overlaid on USA map
    The optional argument num_counties specifies the number of counties to be drawn
    """
     
    # Load map image, note that using 'rb'option in open() is critical since png files are binary
    with open(map_name, 'rb') as map_file:        # using 'r' causes Python to crash :(
        map_img = plt.imread(map_file) #read map in the png in to binary format
        
    #  Get dimensions of USA map image
    ypixels, xpixels, bands = map_img.shape
    print("dimensions", xpixels, ypixels, bands)
    # not sure what bands is???
    
    # Optional code to resize plot as fixed size figure -
    DPI = 80.0                  # adjust this constant to resize your map
    xinch = xpixels / DPI
    yinch = ypixels / DPI
    plt.figure(figsize=(xinch,yinch))

    # Plot USA map
    implot = plt.imshow(map_img)
    
    # Load joined cancer risk data from CSV file - note that rows of input table are already sorted by cancer-risk
    joined_cancer_risk_table = read_csv_file(joined_csv_name)
    ## joined_cancer_risk_table.sort(key = lambda row: float(row[RISK_COLUMN]), reverse = True)     # Code for sorting by risk if table is not already sorted
    # table has 7 columns. 1 countty code, 2 county name, 3 country FIPS (like zip), 4 population, 5 % cancer risk, 6 x coord, 7 y coord
    
    # Compute function that maps cancer risk to RGB colors, using jet
    #risk_map = create_riskmap(mpl.cm.jet) #original
    risk_map = create_riskmap(mpl.cm.jet)
    
    # Draw cancer-risk data for counties as circles whose color indicates risk and area indicates population
    for row in joined_cancer_risk_table[: num_counties]:
        county_population = int(row[3]) #population
        county_cancer_risk = float(row[4]) #% risk
        county_xcenter = float(row[5]) # x coord
        county_ycenter = float(row[6]) # y coord
        plt.scatter(x = county_xcenter * xpixels / USA_SVG_SIZE[0], # x from file * x from map / plot size
                    y = county_ycenter * ypixels / USA_SVG_SIZE[1], # y from file * y from map / plot size
                    s = compute_county_cirle(county_population), # size of circle based on scaler
                    c = risk_map(county_cancer_risk)) # calculate colour based on size of the risk based on log 10 of the 5 risk
        
        plt.colorbar() #can't get this to work
        #plt.legend()
        
    plt.show()

draw_cancer_risk_map("cancer_risk_joined_solution.csv", "USA_Counties_555x352.png", 200)
#draw_cancer_risk_map("cancer_risk_joined_solution.csv", "USA_Counties_1000x634.png") 
