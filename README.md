# P6_Data_Visualization

This project deals with **effective data visualization using D3**. This project deals with creating an explanatory data visualization from a data set that communicates a clear finding or that highlights relationships or patterns in a data set.

The challenge for me in this project was choosing the dataset I would like to work with. I tried choosing datasets of my own and after treading midway into the path, I couldn't come
up with a good visualization that represents the data. So eventually for this project, I had chosen the **PISA Dataset**.

## Summary

PISA is a survey of students' skills and knowledge as they approach the end of compulsory education. It is not a conventional school test. Rather than examining how well students have learned the school curriculum, it looks at how well prepared they are for life beyond school. Around 510,000 students in 65 economies took part in the PISA 2012 assessment of reading, mathematics and science representing about 28 million 15-year-olds globally. Of those economies, 44 took part in an assessment of creative problem solving and 18 in an assessment of financial literacy.

The study gathered background and contextual information from student and school questionnaires. PISA 2012 uses plausible values as indicators of individual student performance and as the basis for national and group estimates. Individual item performance on the student assessments is reported along with overall performance in plausible values.

In this project I have chosen to represent a visualization that shows student's mathematics score across 69 countries and how the education level of the parent's influence their grades. 

## Design 

Out of the various variables available I had chosen CNT(country),MISCED(mother's education level),FISCED(Father's education level) and plausible mathematics variables i.e. PV1MATH,PV2MATH,PV3MATH,PV4MATH,PV5MATH to determine average mathematics score. Before starting with my visualization I had  chosen to clean and organize my dataset further using Python scripts, the code for the same can be found in student_data_process. As a result of which I created 3 csv files for mother,father and both parent's education level.

Representing 7 categorical variables for each parent's education level was a tough task.The first version of my chart used parallel coordinates as a chart type and just used mother's education level but also as per my observation and the feedback I received, representing 69 countries with 7 variables lead to too much clutter on the chart. Though the user could choose a specific country and on mouse over select the specific country and compare the high/low of the grade across parent's education level but seeing the chart as a whole could scare the reader with too much information onboard. 

I also wanted to reader to have an idea of how father's education level as well as both parent's education level impacted the mathematics grade as well. So I chose to add radio buttons which allowed user to pick a choice of who's education level they want to visualize(mother, father, both). Though this visualization allowed the user to interact with the chart but the main concern was still the clutter present in the chart and how difficult it was to digest this information.

So as a result of this I created my third visualization which used stacked bar chart which grouped education level None,ISCED 1,ISCED 2,ISCED 3A,4,ISCED 3B,C,ISCED 5A,6,ISCED 5B and used the x axis to represent the countries and the y axis to show the mathematics score. I kept the interaction part by keeping the radio buttons to choose the parent and compare the scores. To provide animation I had chosen to go with a simple tooltip of mouse over which shows for each country the score corresponding to each ISCED level of the parent. 

Also to depict the relationship between each grade, I chose to alter the color scheme to shades of red/orange with intense shades of reds for higher ISCED levels like ISCED 5B, ISCED 5A,6 and dull shades of orange to represent lower ISCED level like None,ISCED 1. Also I wrote a narrative about how parent's education level influences kids studies in the long run to depict the findings of my chart.

The final visualization can be found at [PISA visualization](https://bl.ocks.org/Ruchita7/raw/1772b9377ae5521a8acb3e07d8839127/)

## Feedback

**Feedback 1**
Nice visualization and the choice of variables for the visualization. The animations which allow me to choose a particular country and compare the grade across mother's different ISCED level is pretty interesting. I would like to compare how father's education level and both parent's education level have an effect on the mathematics grade. Also 1 thing that immediately strikes me when I open this visualization is the clutter and the amount of data that is represented in the single chart which is tough on the eyes.

**Feedback 2**
Nice work done on adding interaction to the chart by allowing the user to choose which parent's education level they want to check and how their kids grade then vary depending upon the chosen parent's education level. The use of animation/interaction by allowing me to choose an axis value is pretty exciting. The chart on initally loading looks like a cobweb but as one choose a country the other countries axis lines fade out is good. Can we make the axis lines light initally so that the chart doesn't look like an information overload. Is it possible to add tooltip to the charts so that I can the comparative scores across each ISCED level of the parent.

**Feedback 3**
This is an impressive graph on display here.
I like that you have provided explanation for variables you are looking into. Also the fact that I can choose which parent to compare with gives a good understanding of which parent has a higher effect on the child's education.
Frankly there is nothing big that I would like to see different in your visualization. It gives the information it is claiming to give in a clear manner. 
Good job and best wishes!

## Resources<br/>

https://bl.ocks.org/mbostock
https://wdexplorer.com/20-examples-beautiful-css-typography-design/
http://bl.ocks.org/mbostock/3943967
https://tympanus.net/codrops/2012/11/02/heading-set-styling-with-css/
http://www.jeromecukier.net/blog/2013/03/05/d3-tutorial-at-strata-redux/
https://discussions.udacity.com/
https://nces.ed.gov/surveys/pisa/pdf/PISA2009CB_quickguide.pdf
https://nces.ed.gov/surveys/pisa/index.asp
http://www.oecd.org/pisa/pisaproducts/datavisualizationcontest.htm
https://www.oecd.org/pisa/pisaproducts/PISA%202012%20Technical%20Report_ANNEX%20B%20%E2%80%93%20CONTRAST%20CODING%20USED%20IN%20CONDITIONING.pdf
https://www.oecd.org/pisa/pisaproducts/PISA12_stu_codebook.pdf
http://mi2.mini.pw.edu.pl:8080/SmarterPoland/PISAcontest/
