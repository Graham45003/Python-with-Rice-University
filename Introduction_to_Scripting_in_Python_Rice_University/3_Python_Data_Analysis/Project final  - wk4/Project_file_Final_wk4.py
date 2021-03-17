"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

##
## Provided code from Week 3 Project
##

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table


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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


##
## Part 1: Functions to compute top batting statistics by year
##

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    
    filtered = []
    filtered = list(filter(lambda x: x[yearid] == str(year), statistics))
    
    return(filtered)



def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    
    formulacalc = []
    for row in range(0, len(statistics)):
        playerid = statistics[row][info["playerid"]]
        stat = (formula(info, statistics[row]))
        if stat == 0:
            pass
        else:
            formulacalc.append((playerid, stat))
    
    #sorts by second field which is the number
    formulacalc.sort(key=lambda pair: pair[1], reverse=True)
    
    #reduces the list by the number required
    finallist = formulacalc[0:numplayers]
    
    return finallist


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    
    #reads in names
    mastfile = read_csv_as_list_dict(info["masterfile"], info["separator"], info["quote"])
    
    new_list = []
    
    for idx in range(0, len(top_ids_and_stats)):
        for mastrow in range(0, len(mastfile)): #findsmatches in playerid
            if top_ids_and_stats[idx][0] == mastfile[mastrow][info["playerid"]]: 
                playername = mastfile[mastrow][info["firstname"]] + " " \
                             + mastfile[mastrow][info["lastname"]]
                stat = top_ids_and_stats[idx][1]
                # f is used to restrict number of characters after decimal place
                new_list.append((str(f'{stat:.3f}') + ' --- ' + playername))
                 
    return new_list


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    
    # read the csv for stats
    statistics = read_csv_as_list_dict(info["battingfile"], info["separator"], info["quote"])
    #filter by year
    stat_by_year = filter_by_year(statistics, year, info["yearid"])
    #calcualte the stat and filter by numplayers
    topplayers = top_player_ids(info, stat_by_year, formula, numplayers)
    #matches the names in master file to the player id
    topplayers_names = lookup_player_names(info, topplayers)
   
    return topplayers_names


##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    

    new_list = {}
    for row in range(0, len(statistics)):
        if statistics[row][playerid] in new_list.keys():
            for col in fields:
                #once matching stat found converts to int for calc
                player = statistics[row][playerid]
                value = int(new_list[player][col])
                value += int(statistics[row][col])
                new_list[player][col] = int(value)
                value = 0
            #if player is not in new list adds new row and copies in columns      
        else:
            newplayer = statistics[row][playerid]
            new_list[newplayer] = {}
            new_list[newplayer][playerid] = newplayer
            for newcol in fields:
                new_list[newplayer][newcol] = int(statistics[row][newcol])    
    
    return new_list


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    
    statistics = read_csv_as_list_dict(info["battingfile"], \
                                       info["separator"], info["quote"])
    
    #calculate the sum of each stat for each player
    player_career_stats = aggregate_by_player_id(statistics, \
                                       info["playerid"], info["battingfields"])
    
    #had a bit of trouble.  owl list wanted the agregate list in a weird way
    #ended up having to bring the dict down to lists that the top_player_ids
    #and the lookup_player_names would work with
    
    career_list = []
    final_list = []
    
    for row in player_career_stats:
        career_list = [player_career_stats[row]]
        final_list.append(career_list)
        
    career_stats = []
    for key in range(0, len(final_list)):
        #temp = final_list[key][0]
        career_stats.append(final_list[key][0])
        
    #print(career_stats)    
    
    career_stats = top_player_ids(info, career_stats, formula, numplayers)
    
    #career_stats.sort(key=lambda pair: pair[1], reverse=True)
    
    topplayers_names = lookup_player_names(info, career_stats)
    
    #return []
    return topplayers_names
    



##
## Provided testing code
##

def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}
    
    baseballdatainfo = {"masterfile": "master1.csv",   # Name of Master CSV file
                        "battingfile": "batting1.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "player",            # Player ID field name
                        "firstname": "firstname",          # First name field name
                        "lastname": "lastname",            # Last name field name
                        "yearid": "year",                # Year field name
                        "atbats": "atbats",                    # At bats field name
                        "hits": "hits",                       # Hits field name
                        "doubles": "doubles",                   # Doubles field name
                        "triples": "triples",                   # Triples field name
                        "homeruns": "homers",                  # Home runs field name
                        "walks": "walks",                     # Walks field name
                        "battingfields": ["atbats", "hits", "doubles", \
                                          "triples", "homers", "walks"]}
    

    # test functions on batting1.csv
    print("Top 5 batting averages in 2020")
    top_batting_average_2020 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 2020)
    for player in top_batting_average_2020:
        print(player)
    print("")

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 4)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

#test_baseball_statistics()