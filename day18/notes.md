# customizing line plots 
1. line customization 
- customize the apppearance of a line plot using different parameters 
a) colour 
channges colour of a lline 
plt.plot (x,y, colour ="red")
we can use short forms also for colours - "r" , "b" ,"g"
b) linestyle 
changes the style of a line 
plt.plot(x,y, linestyle="--")
c) linewidth 
changes the thickness of the line 
plt.plot(x,y, linewidth=3)
larger value = thicker line
d) marker 
shows symbols at every data point 
plt.plot (x,y, marker ="0")
0 - circle 
s - square 
^ - triangle 
* - star 
"X" - cross
"+" - plus

e) markersize 
changes the size of markers '
plt.plot (x,y , marker ="0" , markersize =10 )
larger number = larger marker 

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [60,70,80,75,90]

plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    linewidth=3,
    marker="o",
    markersize=8
)

plt.show()

# legends 
1. why it is used 
legends help identify multiple lines on the same graph 
without legend it is difficult to know which line represent which data

label 
gives a name to a plotted line 
plt.plot(x,y,label="arya")

2. plt.legend()
display the legend 
plt.plot(x,y1,label ="student a")
plt.plot(x,y2,label ="student b")
plt.legend()

3. figure size 
plt.figure(figsize=(8,5))
width = 8 
height =5 

4.why figure size matters 
- make graphs easier to read 
- prevents labels from overlapping 
- looks better in reports and presentations
plt.figure (figsize=(10,6))

5. plot stylig 
- use meaning full titles 
- label bith axes 
- use suitable colours 
- keep line style consistent 
- add a grid for readability 
- use legends when plotting multiple datasets 

