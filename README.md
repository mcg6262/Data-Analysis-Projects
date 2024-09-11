This repository houses the analysis projects I completed for the Data Analysis with Python course by freeCodeCamp. Each of the five projects and their respective files, including CSV datasets, Python scripts, and figures produced, are described below. 

**1. Mean, Variance, and Standard Deviation Calculator**

* Goal: Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
* Python script: mean_var_std.py

**2. Demographic Data Analyzer**

* Goal: Given a dataset of demographic data that was extracted from the 1994 Census database, analyze demographic data using Pandas.  
* Python script: demographic_data_analyzer.py

**3. Medical Data Visualizer**

* Goal: Visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations, and this data used to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.
* Python script: medical_data_visualizer.py
* Categorical bar chart (catplot.png): A bar chart comparing the categorical features between patients with 'cardio' values of 0 (representing the absence of a cardiovascular disease) and 1 (representing the presence of cardiovascular disease). 
![catplot](https://github.com/user-attachments/assets/ca669c10-52ef-40f7-bcaf-6afbdcea9534)

* Correlation heat map (heatmap.png): A triangular matrix using color to visualize the correlation between medical data variables.
![heatmap](https://github.com/user-attachments/assets/dcd5a53f-6eb3-402b-8b4b-5a53d08de6f4)

**4. Page View Time Series Visualzier**

* Goal: Visualize time series data using a line chart, bar chart, and box plots. This project uses Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help to understand the patterns in visits and identify yearly and monthly growth.
* Python script: time_series_visualizer.py
* Line plot (line_plot.png): Daily freeCodeCamp Forum Page Views From May 2016 to December 2019.
![line_plot](https://github.com/user-attachments/assets/a765596f-c7f1-4512-b559-edef0960c84b)

* Bar plot (bar_plot.png): Average page views by month, grouped by years 2016 to 2019.
![bar_plot](https://github.com/user-attachments/assets/b416af85-149f-4213-83e7-bf861cffa2dc)

* Box plot (box_plot.png): Year-wise page views to visualize by trend (L) and month-wise page views to visualize by seasonality (R).  
![box_plot](https://github.com/user-attachments/assets/e2798991-ad14-4a7c-b9df-84aba7f7063c)

**5. Sea Level Predictor**

* Goal: Analyze a dataset of the global average sea level change since 1880, and use the data to predict the sea level change through year 2050.
* Python script: sea_level_predictor.py
* Scatter plot with regression line (sea_level_plot.png): Plots sea level values from 1880 to 2013, including a red line of best fit which predicts sea levels up through the year 2050. A pink line of regression predicts future sea levels to the year 2050, but only considers data from the years 2000-2013. 
![sea_level_plot](https://github.com/user-attachments/assets/77e46f79-b3ed-4366-aaad-4a81a692279a)
