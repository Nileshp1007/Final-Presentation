import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import os
from data_cleaning import load_and_clean_data

#Load and clean data
df = load_and_clean_data('dataset/HealthExpenditure.csv', 'dataset/LifeExpectancy.csv')

os.makedirs('report/visuals', exist_ok=True)
#Scatter plot
sns.scatterplot(data=df, x='HealthExpenditure', y='LifeExpectancy')
plt.title('Health Expenditure vs. Life Expectancy')
plt.xlabel('Health Expenditure per Capita (USD)')
plt.ylabel('Life Expectancy (Years)')
plt.savefig('report/visuals/scatter_plot.png')
plt.clf()

#Correlation heatmap
correlation = df[['HealthExpenditure', 'LifeExpectancy']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('report/visuals/correlation_heatmap.png')