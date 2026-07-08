import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x, y)
plt.title("My Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show() 

# revision 
1- whats matplotlib?
python lib used creating graphs, charts , and data visualizations 
heps us convert numerical data into visual form so it becomes easier for us to understand the trend 

-line graph 
-bar chart 
- pie chart 

it is used to analyze datasets instead of telling trends in numbers like 80 , 85 , 90 it will show a graph whether the marks are increasing or decreasing 

2. diff between matplotlib and seaborn 
matplotlib - basic plotting library 
-more control over graphs 
- more coding 
- good for custmoization 

seaborn 
- top of matplotlib 
-more attraactive ggraphs 
- easier for statistical plots 
- good for beautiful visualization 

3. where matplotlib is used 
- data science 
- machine learning 
- businness analytics 
-research 

4. pyplot basics 
import matplotlib.pyplot as plt 
- it is a module inside matplotlib 
- provides functions for creating graphs 

5. figure and axes 
- the whole graph window 
blank page 
axes- area whre graphs are drawn 
x asix / yaxis 

6. basic plotting workflow 
create data 
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plot data 
plt.plot(x,y)
display graph 
plt.show ()

7. essential plot functions 
  1. plt.plot()
  - draws a line graph 
  plt.plot(x,y)
  2. plt.show()
  -displays graph 
  3. plt.title()
  -adds a tittle 
  plt.title("student marks" )
  4. plt.xlabel()
  -labels x axis 
  plt.xlabel("test")
  5. plt.ylabel()
  -labels y axis 
  plt.ylabels("marks")
  6. plt.grid()
  displlay grid lines 
  