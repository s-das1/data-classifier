import re
import csv

#checks if a string in a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#calculates the percentage of the rows in a column that are numeric
def account_balance_match_percentage(column_array):
    i = 1 #This is to ignore header of the CSV data
    t = 0
    f = 0
    while i < len(column_array):
      if (is_number(column_array[i].strip()) == True) and (float(column_array[i].strip()) < 10000000):
        t += 1
      else:
        f += 1    
      i += 1  
    
    return round((float(t)/(len(column_array)-1))*100, 2)

#calculates the percentage of rows in a column that are a TIN
def TIN_match_percentage(column_array):
    i = 1 #This is to ignore header of the CSV data
    t = 0
    f = 0
    while i < len(column_array):
      if (re.match("^(9\d{2})([ \-]?)([7]\d|8[0-8])([ \-]?)(\d{4})$", column_array[i].strip())) != None:
        t += 1
      else:
        f += 1    
      i += 1  
    
    return round((float(t)/(len(column_array)-1))*100, 2)

#calculates the percentage of rows in a column that are first names  
def name_match_percentage(column_array, source):
    i = 1 #This is to ignore header of the CSV data
    t = 0
    f = 0
    
    #Opening the txt file and storing in an array for performance benefits
    with open(source, 'r', encoding="utf-8") as file:
      temp_db = []
      for line in file:
        temp_db.append(line.lower())  
    
    #Stripping all elements (e.g. '/n' after the string) in this list and converting it to a set for faster search
    temp_db = set([s.rstrip() for s in temp_db])
    
    while i < len(column_array):
      #checks if a string is a first name by matching against a database of names 
      if (column_array[i].strip().lower() in temp_db and len(column_array[i].strip()) >= 3):
        t += 1
      else:
        f += 1    
      i += 1  
    
    return round((float(t)/(len(column_array)-1))*100, 2)
  
def FATCA_codes_match_percentage(column_array):
    i = 1 #This is to ignore header of the CSV data
    t = 0
    f = 0
    FATCA_codes = ['FATCA101', 'FATCA102', 'FATCA103', 'FATCA104']
    while i < len(column_array):
      #checks if a string is a first name by matching against a database of names 
      if (column_array[i].strip().upper() in FATCA_codes): 
        t += 1
      else:
        f += 1    
      i += 1  
    
    return round((float(t)/(len(column_array)-1))*100, 2)
