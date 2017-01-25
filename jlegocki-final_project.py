#import modules for later use, some parts of modules may not be used
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, save
from bokeh.charts import Line, output_file, save, Bar 
import csv 


#use college scorecard csv data file to get info on sat scores during the 2014-2015 school year 
#download csv file for data
#read from file to get info on scores 
#trim down file to only information that is wanted (SAT scores, can also use admission percentages)

#create a data frame using the csv file
df = pd.read_csv("Sorted_Trimmed_List.csv")

#get values for the x and y axis of the graph
#for this graph, use admission rates vs average SAT scores 
x = (df["ADM_RATE_ALL"]*100)
y = df["SAT_AVG_ALL"]

#create a html file for the output
output_file("averagesatscores.html")

#create a figure for the scatterplot along with the representation for the data on the plot (circles)
#edit sizes and colors for better visuals 
graph1 = figure(width = 1000, height = 1000, x_axis_label = "Acceptance Rate", y_axis_label = "Average SAT Score")
graph1.circle(x, y, line_color = "black", fill_color = "blue", size=10)
#use save to create the plot 
save(graph1)


############################


# for the second graph, get the top 20 schools and their average SAT scores 

#create a new data frame to have the top 20 values 
top = df.head(20)


#create a bar graph using the top20 data, edit sizes and presentation to make graph look better 
graph2 = Bar(top, "INSTNM", values = "SAT_AVG_ALL", title = "Top Twenty Schools by Average SAT Score", bar_width = 0.4, legend = False, xlabel = "School Name", ylabel = "Average SAT Score", height = 2000, width = 2000)

#make an output file for the graph
output_file("toptwentysatscores.html")

#save the second graph 
save(graph2)


############################


# for the third graph, get the top 20 schools and their acceptance rates  
#use the "top" data frame for the 20 values 

#create a bar graph using the top20 data, edit sizes and presentation to make graph look better 
graph3 = Bar(top, "INSTNM", values = "ADM_RATE_ALL", title = "Top Twenty Schools by Acceptance Rate", bar_width = 0.4, legend = False, xlabel = "School Name", ylabel = "Acceptance Rate (in decimal form)", height = 2000, width = 2000, color = "lightskyblue")

#make an output file for the graph
output_file("hardesttogetinto.html")

#save the third graph 
save(graph3)





