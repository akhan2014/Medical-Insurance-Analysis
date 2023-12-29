# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Load the dataset
df = pd.read_csv('/Users/alexkhan/Desktop/insurance.csv')

# Display basic information and first few rows of the dataset
print(df.info())
print(df.head(10))

# Data Cleaning Section
# ----------------------
# Check for duplicates and missing values
print('Number of Duplicated Rows: ', df.duplicated().sum())
print('Missing Value Count:', df.isnull().sum())

# Initial Data Analysis Section
# -----------------------------
# Display statistical summary of the dataset
print(df.describe())

# Question 1 Analysis
# --------------------
# Question 1: Do smokers incur higher medical costs than non-smokers?
# Group data by 'smoker' status and get summary statistics for the charges
smoker_summary_charge = df.groupby('smoker')['charges'].describe()
print(smoker_summary_charge)

# Visualize medical charges by smoker status
sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Medical Charges By Smoker Status')
plt.show()

# Perform t-test to compare charges between smokers and non-smokers
charges_smokers = df[df['smoker'] == 'yes']['charges']
charges_nonsmokers = df[df['smoker'] == 'no']['charges']
t_stat, p_val = stats.ttest_ind(charges_smokers, charges_nonsmokers)
print('T-statistic is: ', t_stat)
print('P-value is: ', p_val)

# Question 2 Analysis
# --------------------
# Question 2: Does your number of children impact your insurance rate?
# Group data by 'children' and get summary statistics for the charges
children_summary_charge = df.groupby('children')['charges'].describe()
print(children_summary_charge)

# Visualize with a bar chart
sns.barplot(x='children', y='charges', data=df)
plt.title('Medical Charges By Number Of Children')
plt.show()

# Perform ANOVA to compare the means of each category
f_stat, p_val = stats.f_oneway(df[df['children']==0]['charges'],
                               df[df['children']==1]['charges'],
                               df[df['children']==2]['charges'],
                               df[df['children']==3]['charges'],
                               df[df['children']==4]['charges'],
                               df[df['children']==5]['charges'])
print('F-statistic is: ', f_stat)
print('P-value is: ', p_val)

# Question 3 Analysis
# --------------------
# Question 3: Are Medical Charges different across various regions?
# Group data by 'region' and get summary statistics for the charges
region_summary_charge = df.groupby('region')['charges'].describe()
print(region_summary_charge)

# Visualize with a bar chart
sns.barplot(x='region', y='charges', data=df)
plt.title('Medical Charges By Region')
plt.show()

# Perform ANOVA to compare the means of each category
f_stat, p_val = stats.f_oneway(df[df['region']=='southwest']['charges'],
                               df[df['region']=='southeast']['charges'],
                               df[df['region']=='northwest']['charges'],
                               df[df['region']=='northeast']['charges'])
print('F-statistic is: ', f_stat)
print('P-value is: ', p_val)