import csv
import time

#test1
#test2
#t0 = time.time()

from utils import account_balance_match_percentage
from utils import TIN_match_percentage
from utils import name_match_percentage
from utils import FATCA_codes_match_percentage

import_dataset = 'test_data2.txt'

#Reading input data in to get the number of columns
with open(import_dataset, 'r', encoding="utf-8") as f:
  reader = csv.reader(f)
  first_row = next(reader)
  n = len(first_row)
  
#Creating unique array variables for each column
data = dict()
for i in range(1, n+1):
  col_name = 'column%d' % (i,)
  data[col_name]=[]
   
for name, value in data.items():
  globals()[name] = value

#Reading data from CSV
with open(import_dataset, 'r', encoding="utf-8") as f:
  reader = csv.reader(f)
    
#Inserting each column into a unique array 
  for row in reader:
    for i in range(1, n+1):
      data['column%d' % (i,)].append(row[i-1]) #Inserts each column of data into an array

#t1 = time.time()

#Prints test results
print ('\n' + 'Test type: Account Balance')
for i in range(1, n+1): print (data['column%d' % (i,)][0],':', account_balance_match_percentage(data['column%d' % (i,)]), '%') 
#t2 = time.time()

print('\n')
print ('Test type: TIN')
for i in range(1, n+1): print (data['column%d' % (i,)][0],':', TIN_match_percentage(data['column%d' % (i,)]), '%')
#t3 = time.time()

print('\n')
print ('Test type: First name')
for i in range(1, n+1): print (data['column%d' % (i,)][0],':', name_match_percentage(data['column%d' % (i,)], 'first_names.txt'), '%')
#t4 = time.time()

print('\n')
print ('Test type: Last name')
for i in range(1, n+1): print (data['column%d' % (i,)][0],':', name_match_percentage(data['column%d' % (i,)], 'last_names.txt'), '%')
#t5 = time.time()

print('\n')
print ('Test type: FATCA codes')
for i in range(1, n+1): print (data['column%d' % (i,)][0],':', FATCA_codes_match_percentage(data['column%d' % (i,)]), '%')
#t6 = time.time()    

'''
print('\n' + 'Time log:')
print ('Import:', t1-t0, 's')
print ('Account Balance:', t2-t0, 's')
print ('TIN:', t3-t0, 's')
print ('First name:', t4-t0, 's')
print ('Last name:', t5-t0, 's')
print ('FATCA:', t6-t0, 's')
'''