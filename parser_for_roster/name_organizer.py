###########################################################################
##########################      LIBRARY            ########################
###########################################################################

import datetime, xlrd 
import csv
from itertools import takewhile
import os
from os import system
import sys

###########################################################################
##########################       CLASS             ########################
###########################################################################

class Alum:
    def __init__(self, name, email, netid, semester):
        self.name = name
        self.email = email
        self.netid = netid
        self.year = year
    def access(self):
        return self

###########################################################################
##########################      OPEN FILE          ########################
###########################################################################    

# filename to open
# filename = 'Rosters.xlsx'

system('clear')
cwd = os.getcwd()
list_of_files = os.listdir(cwd)

wrong_filename = True
wrong_counter = 0
while(wrong_filename):
    try:
        print('')
        filename = input("Please enter the filename to parse: ")
        
        print("You entered: " + filename)
        print('')
        print('reading the file.......................................')
        print('.......................................................')
        wb = xlrd.open_workbook(filename) 
        print('finished reading file!.................................')
        print('.......................................................')
     
        wrong_filename = False
    except OSError as e:
        system('clear')
        wrong_counter = wrong_counter + 1
        print('The file you input is not recognized')
        if ('.' not in filename):
            print('make sure you include the file extension')
        if (wrong_counter > 2):
            print('')
            print('here are the files in your folder')
            print(list_of_files)
            print('make sure your file is in the folder,')
            print('or that you are spelling it correctly')


output = []
sheets = wb.sheet_names()


###########################################################################
##########################        HELPERS          ########################
###########################################################################  

def get_year_from_semester(semester):
    return [int(s) for s in semester.split() if s.isdigit()][0]

def column_len(sheet):
    col_values = sheet.col_values(1)
    col_len = len(col_values)
    for _ in takewhile(lambda x: not x, reversed(col_values)):
        col_len -= 1
    return col_len

###########################################################################
##########################      GET NAME AND INFO  ########################
###########################################################################  

for sheet_index in range(0,wb.nsheets):
    semester = sheets[sheet_index]
    sheet  = wb.sheet_by_index(sheet_index) 
    labels = [str(x).lower().replace('text:','').replace("'","").replace(" ",'') \
        for x in sheet.row(0)]
    year = get_year_from_semester(semester)

    for i in range(1,column_len(sheet)-1):
        system('clear')
        # NAME
        # get name based on if name label
        if ('name' in labels):
            name_index = labels.index('name')
            name = sheet.cell_value(i, name_index)
        # get name based on first and last label
        elif ('first' in labels and 'last' in labels):
            first_index = labels.index('first')
            last_index = labels.index('last')
            name = sheet.cell_value(i, first_index) + ' ' + sheet.cell_value(i, last_index)
       
        # EMAIL
        if ('email' in labels):
            email_index = labels.index('email')
            email = sheet.cell_value(i, email_index)
        
        # NETID
        if ('netid' in labels):
            netid_index = labels.index('netid')
            netid = sheet.cell_value(i, netid_index)
        else:
            netid = 'netid not given'

        # parse their email here
        email = email.lower().replace(" ",'')

        alumni = Alum(name, email, netid, year)
        print(name, email, netid, year)
        # if their email already exists on the list, do not add them
        already_in_list = False
        for i in output:
            if email in i:
                already_in_list = True
        if already_in_list == False:
            output.append([alumni.name, alumni.email, alumni.netid, alumni.year])

system('clear')
print('successfully finished!.................................')
print('.......................................................')
print('')
print('')
print('download the output.csv file!')


###########################################################################
##########################      PUT INTO A CSV     ########################
###########################################################################  

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "email", "netid", "semester"])
    for row in output:
        [a,b,c,d] = row
        writer.writerow([a,b,c,d])
