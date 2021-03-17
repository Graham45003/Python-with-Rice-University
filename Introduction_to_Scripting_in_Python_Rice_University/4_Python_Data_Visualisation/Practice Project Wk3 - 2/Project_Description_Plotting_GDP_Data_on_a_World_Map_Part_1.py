"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of country
    """

    table = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in reader:
            rowid = row[keyfield]
            table[rowid] = row
    return table
    
def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
  
    country_dict = {}
    country_set = set()  
      
    for country in plot_countries: #checks against pygal list
        if plot_countries[country] in gdp_countries: #if pygal in dict
            country_dict[country] = plot_countries[country] 
        else:
            country_set.add(country) #pygal not in dict

    return country_dict, country_set


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    
    #imports dict with name as keyfield
    gdp_dict = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_name"],\
                            gdpinfo["separator"], gdpinfo["quote"])
    
    # results dict with code, name and set of codes not in dict
    country_dict = reconcile_countries_by_name(plot_countries, gdp_dict)
    
    #countries found in dict that are in pygal library
    valid_countries = country_dict[0]
    
    #print(valid_countries)
    
    nogdp = set() #set of country codes with no gdp but in dict
    gdp_plot = {} #dict of codes and gdp at log 10
    
    for country in valid_countries:
        #print(valid_countries[country])
        if gdp_dict[valid_countries[country]][year] == '': #checks for 0 gdp
            nogdp.add(country) #adds to set if no gdp fpr the year
        else:
            #adds log 10 gdp to dict with code as key
            #print(country, gdp_dict[valid_countries[country]][year])
            gdp_plot[country] = math.log10(float(gdp_dict[valid_countries[country]][year]))
    
    print("gdp", gdp_plot, "in", country_dict[1], "no", nogdp)
    return gdp_plot, country_dict[1], nogdp


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    
    map_dict = build_map_dict_by_name(gdpinfo, plot_countries, year)
    
    #print(map_dict[0])
    
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP by country for ' + year + ' (log scale),\
                                            unified by common country NAME'
    #worldmap_chart.add('World', ['gb'])
    worldmap_chart.add('GDP for ' + year, map_dict[0]) #gdp data for the year
    worldmap_chart.add('Missing from pygal', map_dict[1]) #country name not in pygal list
    worldmap_chart.add('No GDP data', map_dict[2])#no gdp data fo rthat year
    #worldmap_chart.render_in_browser()
    #worldmap_chart.render_to_file('mine_' + map_file)

def test_render_world_map():
    """
    Test the project code for several years.
    """

    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }
    
#     gdpinfo = {
#         "gdpfile": "gdptable1.csv",
#         "separator": ",",
#         "quote": '"',
#         "min_year": 2000,
#         "max_year": 2005,
#         "country_name": "Country Name",
#         "country_code": "Code"
#     }

    
    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES
    
    #test
    #render_world_map(gdpinfo, pygal_countries, "2002", "isp_gdp_world_name_1960.svg")

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    #render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    #render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    #render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

test_render_world_map()