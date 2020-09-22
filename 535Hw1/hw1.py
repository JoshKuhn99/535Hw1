import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

#1
#using pandas to put the csv into a dataframe called tips
tips = pd.read_csv("tips.csv")


#2
#iterating and outputting the columns
for col in tips.columns:
    print(col)

#3
#renaming the columns accordingly
tips.rename(columns = {'time' : 'meal', 'size' : 'party size'}, inplace = True)
print("\nAfter changing the column names:")
for col in tips.columns:
    print(col)

#4
#using head function to view parts of data
print("\n",tips.head())

#5
#retrieving information using .loc[] from row 2 and 3
firstLoc = tips.loc[0]
#row 2 in the csv
secondLoc = tips.loc[1]
#row 3 in the csv
print("\n\n", firstLoc, "\n\n", secondLoc)

#5 cont.
#retrieving infromation using .iloc from row 2 and 3
result_iloc = tips.iloc[[0,1]]
print("\n\n", result_iloc)

#6
getBilldata = tips['total_bill']
getTipdata = tips['tip']
#print("\n\n", getBilldata)
#print("\n\n", getTipdata)

#6 cont.
billHead = getBilldata.head(3)
tipHead = getTipdata.head(3)
print("\n\n", billHead, "\n\n", tipHead)

#7
dataIntersect = tips.iloc[1,2]
print("\n\nThe sex of the customer in the second row, third column (C3) is: " , dataIntersect)

#8
#getting the total number of observations in the dataset
totalRecordsPerCol = tips.count()
#multiplying the number of columns by number of rows using .shape[]
totalRecords = tips.shape[1]*tips.shape[0]
print("\n\nTotal Records per column:\n", totalRecordsPerCol)
print("\n\nTotal Records for the entire DataFrame:\n", totalRecords)

#9
#using the describe() function to get statistics about numerical data using numpy
tipsStats = tips.describe(include = np.number)
print("\n\nThe generated numerical statstics of the DataFrame Tips are:\n", tipsStats)

#10
#using the describe() function to get statstics about all data using numpy
tipsStatsAll = tips.describe(include = 'all')
print("\n\nThe generated statstics of the DataFrame Tips of object and numeric type are:\n", tipsStatsAll)

#11
#finding the average tip amount
avgTipamnt = tips['tip'].mean()
print("\n\nThe average tip amount is:\n", avgTipamnt)
print("The rounded average tip amount is:\n", round(avgTipamnt,2))

#12
#using the describe function to get statistics about the tip column
tipColStats = tips['tip'].describe()
print("\n\nThe following are statistics generated about the 'tip' column:\n", tipColStats)
#13
#drawing a boxplot for the tip column using matplotlib
plt.boxplot(tipColStats)
plt.ylim(0,11, .05)
plt.show() #******works but don't know if this is the amount of detail he wants******


#14
#plotting tip outliers >=6



#15
#use group by func to find avg tip amount per sex.
groupByTip = tips.groupby('sex')

print("\n\nThe average tip left by each gender is as follows:\n",groupByTip['tip'].agg(np.mean))

#16
#creating a new dataframe from the males column and drawing a random sample of 10


males = tips.loc[groupByTip.groups['Male']]
print('\n\n', males)
