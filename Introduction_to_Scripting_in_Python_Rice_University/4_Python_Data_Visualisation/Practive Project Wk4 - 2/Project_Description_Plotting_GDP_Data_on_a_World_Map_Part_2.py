"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table[row[keyfield]] = row
    return table

        

def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary
    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """

    country_codes = read_csv_as_nested_dict(codeinfo['codefile'], codeinfo['plot_codes'],\
                                  codeinfo['separator'], codeinfo['quote'])

    table = {}

    for country in country_codes:
        table[country] = country_codes[country][codeinfo['data_codes']]
        
    return table



def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data
    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.
      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    code_dict = build_country_code_converter(codeinfo)
    country_dict = {}
    country_set_1 = set()
    
    for key, value in plot_countries.items(): 
        for keycode, valcode in code_dict.items(): #codes in codeinfo
            if key.lower() == keycode.lower() and value != "" and valcode != "":
                for key1, value1 in gdp_countries.items():
                    if key1.lower() == valcode.lower() and value1 != "":
                        country_dict[key] = key1 #add to dict if code exists in codeinfo + pygal

    # check which pygal countries are not in country_dict
    for key, value in plot_countries.items():
        for keycode, valcode in code_dict.items():
            if key.lower() == keycode.lower() and valcode.upper() not in gdp_countries:
                country_set_1.add(key)
                
    print(country_dict, set(country_set_1))
    return country_dict, set(country_set_1)

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
        Inputs:
          gdpinfo        - A GDP information dictionary
          codeinfo       - A country code information dictionary
          plot_countries - Dictionary mapping plot library country codes to country names
          year           - String year for which to create GDP mapping
        Output:
          A tuple containing a dictionary and two sets.  The dictionary
          maps country codes from plot_countries to the log (base 10) of
          the GDP value for that country in the specified year.  The first
          set contains the country codes from plot_countries that were not
          found in the GDP data file.  The second set contains the country
          codes from plot_countries that were found in the GDP data file, but
          have no GDP data for the specified year.
        """

    country_dict_1 = {} #country code and gdp
    country_set_1 = set() # countries in plot but not gdp
    country_set_2 = set() # country codes in plots but no gdp
    
    #read gdp data file
    country_codes = read_csv_as_nested_dict(gdpinfo["gdpfile"], gdpinfo["country_code"],\
                            gdpinfo["separator"], gdpinfo["quote"])
    
    # read codeinfo file
    country_dict = reconcile_countries_by_code(codeinfo,\
                                        plot_countries, country_codes)

    #test for countries in codeinfo and pygal
    val = ""
    for key, value in plot_countries.items(): #pygal dict
        for codekey, codeval in country_dict[0].items(): #codeinfo dict
            if key in country_dict[0]:  #if pygal in dict
                if key.lower() == codekey.lower(): 
                    val = codeval
                else:
                    val = ""
            else:
                country_set_1.add(key)
        if val != "" and val not in country_codes:  #if code not in gdp add to set
            country_set_1.add(key)

    # test for countries in pygal with/without no gdp
    for key, value in country_dict[0].items(): #codeinfo dict
        for codekey, codeval in country_codes.items(): #gdp dict
            if value.lower() == codekey.lower(): #check code
                if codeval[year] != '': #check for gdp
                    country_dict_1[key] = math.log(float(codeval[year]), 10)
                else:
                    country_set_2.add(key)

    return country_dict_1, set(country_set_1), set(country_set_2)

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name
    Output:
      Returns None.
    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """    
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP by country for ' + year + ' (log scale), unified by common' + \
                           ' country Code'
                           
    gdp_datas = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    
    worldmap_chart.add('GDP For ' + year, gdp_datas[0])
    worldmap_chart.add('Missing from World Bank Data', gdp_datas[1])
    worldmap_chart.add('No GDP Data', gdp_datas[2])
     
    worldmap_chart.render_in_browser()          #renders the world map on default browser
#    worldmap_chart.render_to_file(map_file)    #saves the file with the given name


# def test_render_world_map():
#     """
#     Test the project code for several years
#     """
#     gdpinfo = {
#         "gdpfile": "isp_gdp.csv",
#         "separator": ",",
#         "quote": '"',
#         "min_year": 1960,
#         "max_year": 2015,
#         "country_name": "Country Name",
#         "country_code": "Country Code"
#     }
# 
#     codeinfo = {
#         "codefile": "isp_country_codes.csv",
#         "separator": ",",
#         "quote": '"',
#         "plot_codes": "ISO3166-1-Alpha-2",
#         "data_codes": "ISO3166-1-Alpha-3"
#     }
# 
#     # Get pygal country code map
#    pygal_countries = pygal.maps.world.COUNTRIES
# 
#     # 1960
#    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")
# 
#     # 1980
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")
# 
#     # 2000
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")
# 
#     # 2010
#     render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")
# 
# 
# # Make sure the following call to test_render_world_map is commented
# 
#test_render_world_map()