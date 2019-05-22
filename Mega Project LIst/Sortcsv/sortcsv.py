"""
Reads a file of records, sorts them, and then writes them back to the file. 
Allow the user to choose various sort style and sorting based on a particular field.
Note: Ensure that the csv file is in the same directory
"""
import numpy as np
import pandas as pd

filename = input("Please enter the csv file that you want to sort: \n")
try:
    df = pd.read_csv(filename)
except:
    print("You have entered an invalid csv file. Make sure you typed it correctly or make sure its in the same directory")
else:
    col = True
    while col:
        print("What would you like to sort by?")
        for i in df.columns:
            print(i)
        column = input("Please enter column name exactly: \n")
        if column in df.columns:
            col = False
    
    ascending = input("Ascending or descending? (Enter A/D): \n")
    if ascending.upper() == 'D':
        new_df = df.sort_values(by=column,ascending=False)
    else:
        new_df = df.sort_values(by=column)

    newfile = input("What do you want your new csv filename to be? \n")
    new_df.to_csv(newfile,index_label=False)

