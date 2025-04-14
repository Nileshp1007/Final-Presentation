import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import load_and_clean_data

#Load and clean data
df = load_and_clean_data('dataset/health_expenditure.csv', 'dataset/life_expectancy.csv')

#Define variables
X = df[['HealthExpenditure']]
Y = df['LifeExpectancy']

#Build linear regression model
model = LinearRegression()
model.fit(X,Y)

#Predict
Y_pred = model.predict(X)

#Evaluation
print('R^2 Score:', r2_score(Y,Y_pred))
print('MAE:', mean_absolute_error(Y,Y_pred))

#plot graph
sns.regplot(x='HealthExpenditure', y='LifeExpectancy', data=df, line_kws={'color':'red'})
plt.title('Linear Regression: Health Expenditure vs. Life Expectancy')
plt.savefig('report/visuals/regression_plot.png')