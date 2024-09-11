import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print(df.info())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    sex = df["sex"].value_counts()
    men = df.loc[df["sex"] == "Male"]
    print("Males: ", men)
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df["education"] == "Bachelors"
    bachelorsSum = df.loc[df["education"] == "Bachelors"].value_counts().sum()
    totalEdu = df["education"].value_counts().sum()
    percentage_bachelors = round(bachelorsSum * 100/totalEdu, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    masters = df["education"] == "Masters"
    doctors = df["education"] == "Doctorate"

    higher_education = bachelors | masters | doctors 
    print("Advanced Education: ", higher_education)
    lower_education = (df["education"] != "Bachelors") & (df["education"] != "Masters") & (df["education"] != "Doctorate")

    # percentage with salary >50K 
    highEduRich = df.loc[higher_education & (df['salary'] == ">50K")].value_counts().sum()
    highEduTot = df.loc[higher_education].value_counts().sum()
    higher_education_rich = round(highEduRich * 100/highEduTot, 1)

    lowEduRich = df.loc[lower_education & (df['salary'] == ">50K")].value_counts().sum()
    lowEduTot = df.loc[lower_education].value_counts().sum()
    lower_education_rich = round(lowEduRich * 100/lowEduTot, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[df['hours-per-week']].value_counts().min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    highSalMinHPW = df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].value_counts().sum()
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].value_counts().sum()
   
    rich_percentage = round(highSalMinHPW * 100/num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    richPopByCountry = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    countryPop = df['native-country'].value_counts()
    richPercByCountry = round(richPopByCountry * 100 / countryPop, 2)

    highest_earning_country = richPercByCountry.idxmax()
    highest_earning_country_percentage = richPercByCountry.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india = df['native-country'] == 'India'
    indiaRich = df.loc[india & (df['salary'] == '>50K'), 'occupation']. value_counts()
    top_IN_occupation = indiaRich.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)