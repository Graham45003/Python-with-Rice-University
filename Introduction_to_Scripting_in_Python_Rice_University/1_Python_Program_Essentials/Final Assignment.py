"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
 
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    
    date1 = datetime.date(year, month, 1)
    next_month = date1.month % 12 + 1
    
    if next_month == 1:
        date2 = datetime.date(year + 1, next_month, 1)
    else:
        date2 = datetime.date(year, next_month, 1)
    
    return (date2 - date1).days
        
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    if (year >= datetime.MINYEAR) and (year <= datetime.MAXYEAR):
        if (month >= 1 and month <= 12):
            if (day >= 1 and day <= 31):
                if month == 2 and day > 28:
                    if year == ((year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
    
    
    
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):
        if datetime.date(year1, month1, day1) < datetime.date(year2, month2, day2):
            return ((datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days)
        else:
            return 0    
    else:
        return 0

    
    
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    today = datetime.date.today()
    
    if is_valid_date(year, month, day):  
        if datetime.date(year, month, day) < today:
            return ((today - datetime.date(year, month, day)).days)
        else:
            return 0
    else:
        return 0
