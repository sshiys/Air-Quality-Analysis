import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title page
st.set_page_config(page_title="Air Quality Analysis in Shunyi")

# Load dataset
data = pd.read_csv('./dataset/PRSA_Data_Shunyi_20130301-20170228.csv')

# Dashboard title
st.title('Air Quality Dashboard: Shunyi Station')

# Description
st.write('This dashboard provides information about air quality in Shunyi, especially on PM2.5 concentrations.')

# Year and Month Selection
selected_year = st.selectbox('Select Year', list(data['year'].unique()), key='year_selection')
selected_month = st.selectbox('Select Month', list(data['month'].unique()), key='month_selection')

# Filtering data based on the selected year and month
data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Displaying data statistics
st.subheader('Data Overview for Selected Period')
st.write(data_filtered.describe())

# Line chart for PM2.5 concentrations over selected month
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'], marker='o')
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.title(f'Daily PM2.5 Levels for {selected_month}/{selected_year}')
st.pyplot(fig)

# Correlation heatmap for the selected month
st.subheader('Correlation Heatmap of Air Quality Indicators')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap of Air Quality')
st.pyplot(fig)

# Monthly Trend Analysis
st.subheader('Monthly Trend Analysis')
monthly_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
monthly_trends.plot(kind='line', marker='o', color='blue', ax=ax) 
plt.title('Average Monthly PM2.5 Concentrations')
plt.xlabel('Month')
plt.ylabel('PM2.5 Concentration (µg/m³)')
st.pyplot(fig)

# Pollutant Distribution
st.subheader('Pollutant Distribution')
selected_pollutant = st.selectbox('Select Pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots()
sns.boxplot(x='month', y=selected_pollutant, data=data[data['year'] == selected_year], ax=ax)
st.pyplot(fig)
