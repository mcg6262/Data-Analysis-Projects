import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    line1 = linregress(x, y)
    print(line1)
    x_pred1 = pd.Series([i for i in range(1880, 2050)])
    plt.plot(x_pred1, line1.intercept + line1.slope*x_pred1, '#900C3F')

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    line2 = linregress(x_2000, y_2000)
    x_pred2 = pd.Series([i for i in range(2000, 2050)])
    plt.plot(x_pred2, line2.intercept + x_pred2*line2.slope, '#FF5733')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()