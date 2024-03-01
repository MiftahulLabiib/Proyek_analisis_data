import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
bike_day = pd.read_csv('Bike-sharing-dataset/day.csv')
bike_hour = pd.read_csv('Bike-sharing-dataset/hour.csv')

# Display data descriptions
st.subheader("Day Dataset Description:")
st.write(bike_day.describe())

st.subheader("Hourly Dataset Description:")
st.write(bike_hour.describe())

# Correlation heatmap
st.subheader("Correlation Heatmap:")
correlation = bike_day[['cnt', 'temp', 'atemp', 'hum', 'windspeed']].corr()
sns.heatmap(correlation, annot=True, cmap='Reds')
st.pyplot()

# Scatter plots
st.subheader("Correlation between Daily Rental and Temperature:")
columns = ['temp', 'atemp']
for column in columns:
    plt.figure()
    plt.scatter(x=bike_day['cnt'], y=bike_day[column], c="#BF3131")
    plt.xlabel('Number of daily rental')
    plt.ylabel(f'{column}')
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.title(f'Correlation between daily rental and {column}')
    plt.legend()
    st.pyplot()

# Hourly trend plot
st.subheader("Hourly Bike Rental Trend:")
hourly_tren = bike_hour.groupby(by='hr').agg({'cnt': 'mean'}).reset_index()
plt.plot(hourly_tren['hr'], hourly_tren['cnt'], marker=".", c="#BF3131")
plt.xticks(hourly_tren['hr'])
plt.xlabel('hour')
plt.ylabel('Number of Rental Bikes')
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.title("Hourly Bike Rental Trend")
plt.legend()
st.pyplot()

# Hourly temperature plot
st.subheader("Hourly Temperature:")
hourly_temperature = bike_hour.groupby(by='hr').agg({'temp': 'mean', 'atemp': 'mean'}).reset_index()
plt.plot(hourly_temperature['hr'], hourly_temperature['temp'], marker='.', label='Temperature', c="#7D0A0A")
plt.plot(hourly_temperature['hr'], hourly_temperature['atemp'], marker='.', label='Feels-like Temperature', c="#BF3131")
plt.xticks(hourly_temperature['hr'])
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Hourly Temperature')
plt.legend()
st.pyplot()

# Comparison between holiday and weekdays
st.subheader("Comparison Between Holiday and Weekdays:")
rental_day = bike_hour.groupby(by='workingday').agg({'cnt': 'sum'}).reset_index().sort_values(by='cnt', ascending=False)
plt.bar(rental_day['workingday'], rental_day['cnt'], color='#7D0A0A')
plt.xticks(rental_day['workingday'], ['Workingday', 'Holiday & Weekend'])
plt.ylabel('Total Rental Bikes')
plt.yscale('linear')
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.title('Comparison Between Holiday and Weekdays')
st.pyplot()

# Median count of rental bikes on working days vs non-working days
st.subheader("Median Count of Rental Bikes on Working Days vs Non-Working Days:")
working_days = bike_hour[bike_hour['workingday'] == 1]['dteday']
working_day_data = bike_hour[bike_hour['dteday'].isin(working_days)]
non_working_day_data = bike_hour[~bike_hour['dteday'].isin(working_days)]
avg_rentals_working_day = working_day_data['cnt'].median()
avg_rentals_non_working_day = non_working_day_data['cnt'].median()
plt.bar(['Working Day', 'Holiday and Weekend'], [avg_rentals_working_day, avg_rentals_non_working_day], color=['#7D0A0A', '#BF3131'])
plt.xlabel('Day Type')
plt.ylabel('Median Count of Rental Bikes')
plt.title('Median Count of Rental Bikes on Working Days vs Non-Working Days')
st.pyplot()
