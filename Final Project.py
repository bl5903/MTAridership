"""
Name: Bill Leung
Email: bill.leung73@myhunter.cuny.edu
Resources: https://new.mta.info/agency/new-york-city-transit/subway-bus-ridership-2020
Title: The Pandemic That Caused a Decline in Ridership
URL: https://bl5903.github.io/MTAridership/
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ridership = pd.read_csv("mtaridership.csv") #this part reads my csv file
#ridership['Percent Change'] = ridership['Percent Change'].astype(float)

sort2020Rank = ridership.sort_values(by="2020 Rank") #this part sorts the column "2020 Rank" least to greatest and
popular2020 = sort2020Rank.head(10) #displays the top 10 results

sortleast2020Rank = ridership.sort_values(by="2020 Rank",ascending = False)#this part sorts the column "2020 Rank" greatest to least and
leastpop2020 = sortleast2020Rank.head(10) #displays the top 10 results

highpercentchangeRank = ridership.sort_values(by="Percent Change")#this part sorts the column "Percent Change" least to greatest and
highPercent = highpercentchangeRank.head(10) #displays the top 10 results

leastpercentchangeRank = ridership.sort_values(by="Percent Change",ascending = False)#this part sorts the column "Percent Change" greatest to least and
leastPercent = leastpercentchangeRank.head(10) #displays the top 10 results

#print(ridership.dtypes) #prints the dataframe type
#mta = ridership.plot()

popular2020.plot(x='Route',y= ['2020'],kind = "bar",figsize=(9,9)) #plot the routes by the ridership
plt.xticks(np.arange(0, 10, 1),rotation = 26) #set x tick marks and rotate tick marks 26 degrees
plt.yticks(np.arange(1000, 50000, 4000))#set y tick marks
plt.xlabel('Routes')#x axis label
plt.ylabel('Riders')# y axis label
plt.title('Top 10 Routes from 2020')#graph title
plt.savefig('Popular2020') #save fig to outputfile
plt.show()#display graph

leastpop2020.plot(x='Route',y= ['2020'],kind = "bar",figsize=(9,9)) #plot the routes by the ridership
plt.xticks(np.arange(0, 10, 1),rotation = 26)#set x tick marks and rotate tick marks 26 degrees
plt.yticks(np.arange(100, 400, 25))#set y tick marks
plt.xlabel('Routes')#x axis label
plt.ylabel('Riders')# y axis label
plt.title('10 Least Popular Routes in NYC from 2020')#graph title
plt.savefig('leastpop2020') #save fig to outputfile
plt.show()#display graph

graph = highPercent.plot(x='Route',y= ['Percent Change'],kind = "bar",figsize=(9,9)) #plot the routes by the ridership
graph.invert_yaxis()# invert y axis(flipped the bar graph)
plt.xticks(np.arange(0, 10, 1),rotation = 26)#set x tick marks and rotate tick marks 26 degrees
plt.yticks(np.arange(-0.1, -0.75, -0.05))#set y tick marks
plt.xlabel('Routes') #x axis label
plt.ylabel('Percent Change')# y axis label
plt.title('10 Routes with the Most Change from 2019-2020')#graph title
plt.savefig('highchange') #save fig to outputfile
plt.show()#display graph

graph = leastPercent.plot(x='Route',y= ['Percent Change'],kind = "bar",figsize=(9,9))#plot the routes by the ridership
plt.xticks(np.arange(0, 10, 1),rotation = 26)#set x tick marks and rotate tick marks 26 degrees
plt.yticks(np.arange(-0.35, 0.35, 0.05))#set y tick marks
plt.xlabel('Routes') #x axis label
plt.ylabel('Percent Change')# y axis label
plt.title('10 Routes with the Least Change from 2019-2020')#graph title
plt.savefig('leastchange') #save fig to outputfile
plt.show()#display graph

print(popular2020) #displays popular 2020 routes
print(leastpop2020)#displays least popular 2020 routes
print(highPercent) #displays routes that had the most change in ridership
print(leastPercent)#displays routes that had the least change in ridership

