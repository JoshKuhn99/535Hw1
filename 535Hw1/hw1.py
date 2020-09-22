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
boolTip = np.where(tips['tip'] >= 6)
print("tips >=6 at indexes: ", boolTip)
print(boolTip[0])

#15
#use group by func to find avg tip amount per sex.
groupByTip = tips.groupby('sex')
print("\n\nThe average tip left by each gender is as follows:\n",groupByTip['tip'].agg(np.mean))

#16
#creating a new dataframe from the males column and drawing a random sample of 10
males = tips.loc[groupByTip.groups['Male']]
print('\n\n', males)

#17 
#create a df named females and call sample(frac = 0.1, replace=True)
females = tips.loc[groupByTip.groups['Female']]
print(females.sample(frac = 0.1, replace = True))

#18 
#find number of male and female customers
maleCount = males['sex'].value_counts()
femaleCount = females['sex'].value_counts()
print("The number of male customers are: ", maleCount[0],"\n",
      "and the number of female customers: \n", femaleCount[0])

#19 
#create a bar chart comparing males and females 
count = [maleCount[0], femaleCount[0]]
index = ['Male', 'Female']
boxPlotDF = pd.DataFrame({'count': count}, index = index)
boxPlot = boxPlotDF.plot.bar(rot = 0)

#20 JK Version of 20
#create a scatter plot comparing male and female tips
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(males['tip'], males['total_bill'], 'o', c = 'r', label = 'male')
ax.scatter(females['tip'], females['total_bill'], 's', c = 'b', label = 'female')
plt.show()

#20 AW Version of 20
#drawing scatter plot of tips given by male compared to tips given by female
#x = tips['total_bill']
#y = tips['tip'].loc[2]


#plt.scatter(x,y, color='b', marker='+', label='Female')
#plt.scatter(x,y, color='r', marker='s', label='Male')
#plt.legend(loc='upper left')
#plt.show()

#22
#describe function on the day columns of tips
dayDescribe = tips['day'].describe()
print("\n\nQuestion 22\n", dayDescribe)

#23
#grouby to form groups based on days of the week and # of customers that were served daily
dinnerDayGroup = tips.groupby(by='day')['party size'].count()
print("\n\nQuestion 23\n", dinnerDayGroup)

#24
#line plot the results of #23
tips.groupby(by='day')['party size'].count().plot(kind='line')
plt.xticks([0.0,1.0,2.0,3.0],["Thursday",'Friday',"Saturday","Sunday"])
plt.grid(True)
plt.show()
#not working properly yet (data seems off)

