import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 Read in medical examination data
df = pd.read_csv('medical_examination.csv')
#print(df.info())

# 2 Create overweight column by calculating BMI (weight kg / height m) ** 2 
# where overweight is bmi > 25 with 'overweight' valued at 1, else 0 
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(
(lambda x : 1 if x > 25 else 0))

# 3 Normalize data so for chol and gluc, 1 == 0 and anything above 1 == 1
# now 0 = 'good' and 1 = 'bad'
df['cholesterol'] = df['cholesterol'].apply((lambda x : 0 if x == 1 else 1)) 
df['gluc'] = df['gluc'].apply((lambda x : 0 if x == 1 else 1))

# 4 Draw plot showing 0 vs 1 values for each variable in a bar plot 
# which is split by cardio = 0 vs cardio = 1
def draw_cat_plot():
    # 5 id_vars is columns used as identifier variable, and value_vars is 
    # columns compared side by side (to 'unpivot')
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars = ['cholesterol', 
    'gluc', 'smoke', 'alco', 'active', 'overweight'])
    print(df_cat.head())

    # 6 Group and reformat data to split it by cardio, showing the counts 
    # for each feature. One of the columns will be renamed for functionality 
    # (total [items] column which = 1, for y axis purposes)
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).count()
    # pd.melt makes 'variable' and 'value' columns in df 
    # 'for aggregated output, return object with group labels as index' 
    # (makes cardio not the index? although 'True' is default)

    # 7 Draw catplot with sns.catplot()
    
    # 8
    fig = sns.catplot(
        data=df_cat, x='variable', y='total', col='cardio', hue='value', kind='bar'
    )
    # Function inputs found on seaborns website by finding the plot that looked kinda similar 

    # 9 Do not modify
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()

# 10 Create function to draw the correlation heat map of different variables
def draw_heat_map():
    # 11 Clean the data to of potential outliers by removing: 
    # Height < the 2.5th percentile or > the 97.5th percentile 
    # Weight > the 2.5th percentile or > the 97.5th percentile 
    # Diastolic bp (minimum pressure in arteries when heart contracts) should not be more than 
    # systolic bp (maximum pressure in arteries when heart relaxes) 
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975)) &
        (df['ap_lo'] <= df['ap_hi'])
    ]

    # 12 Calculate correlation matrix and store in corr variable
    corr = df_heat.corr(method='pearson')

    # 13 Mask upper triangle and store in mask variable
    mask = np.triu(corr)

    # 14 Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    # 15 Plot correlation matrix using sns.heatmap() method 
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt='.1f',
                center=0.08, cbar_kws={'shrink':0.5})
    # look at documentation on site, most of these are for styling 

    # 16 Do not modify
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
