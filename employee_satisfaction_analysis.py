import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 2: Load the Data
employee_data = pd.read_csv( "/Users/susoeresia-eke/Downloads/hr_dashboard_data.csv")
# Display the first few rows of the dataset to get a sense of the data
employee_data.head()
employee_data.info()

# Step 3: Data Cleaning
# Check for missing values
missing_values = employee_data.isnull().sum()
print("Missing Values:\n", missing_values)

# Remove rows with missing values (if necessary)
employee_data.dropna(inplace=True)

# Case 1: Employee Satisfaction Analysis: Analyze the factors that influence employee satisfaction.
# Check for outliers (e.g., unrealistic age values)
plt.boxplot(employee_data['Age'])
plt.xlabel('Age')
plt.title('Age Boxplot')
plt.show()

# Interpretation for Age BoxPlot
age_data = employee_data['Age']
age_median = age_data.median()
age_iqr = age_data.quantile(0.75) - age_data.quantile(0.25)
age_whisker_upper = age_data.quantile(0.75) + 1.5 * age_iqr
age_whisker_lower = age_data.quantile(0.25) - 1.5 * age_iqr
outliers = age_data[(age_data < age_whisker_lower) | (age_data > age_whisker_upper)]


# Interpretation: The boxplot provides a summary of employee ages. The box represents
# the interquartile range (IQR) where the middle 50% of employees' ages fall. The line
# inside the box is the median age (50th percentile). The "whiskers" extend to the
# minimum and maximum ages within a certain range (typically 1.5 times the IQR).
# Any points beyond the whiskers are considered outliers and might be atypical ages.
# This visualization helps identify the spread and central tendency of employee ages.


# Remove outliers (if necessary)
employee_data = employee_data[(employee_data['Age'] >= 18) & (employee_data['Age'] <= 65)]

# Descriptive Statistics and Visualization
# Descriptive statistics for satisfaction rate
satisfaction_stats = employee_data['Satisfaction Rate (%)'].describe()

# Histogram of satisfaction rates
plt.hist(employee_data['Satisfaction Rate (%)'], bins=20, edgecolor='k')
plt.xlabel('Satisfaction Rate (%)')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Satisfaction Rates')
plt.show()

# Satisfaction Rate Histogram
satisfaction_data = employee_data['Satisfaction Rate (%)']
satisfaction_mean = satisfaction_data.mean()
satisfaction_peak = satisfaction_data.mode().values[0]
satisfaction_std = satisfaction_data.std()

# Box Plot Findings
print(f"The mean satisfaction rate is {satisfaction_mean}%.")
print(f"The most common satisfaction rate is {satisfaction_peak}%.")
print(f"The standard deviation is approximately {satisfaction_std}%, indicating the spread of satisfaction rates.")

# Age Distribution by Department
# Interpretation for Age Distribution by Department
department_age_data = [employee_data[employee_data['Department'] == d]['Age'] for d in employee_data['Department'].unique()]

plt.figure(figsize=(10, 6))
plt.boxplot(department_age_data, labels=employee_data['Department'].unique())
plt.xlabel('Department')
plt.ylabel('Age')
plt.title('Age Distribution by Department')
plt.xticks(rotation=45)
plt.show()

# Histogram Interpretation
for i, department in enumerate(employee_data['Department'].unique()):
    print(f"Statistics for {department} department:")
    print(f"- Mean age: {round(department_age_data[i].mean(), 2)} years")
    print(f"- Median age: {department_age_data[i].median()} years")
    print(f"- Minimum age: {department_age_data[i].min()} years")
    print(f"- Maximum age: {department_age_data[i].max()} years")
    print(f"- IQR: {department_age_data[i].quantile(0.75) - department_age_data[i].quantile(0.25)} years")

# Descriptive statistics for age
age_stats = employee_data['Age'].describe()


# Inferential Statistics
# Hypothesis test: Is there a significant difference in satisfaction rates between genders?

female_satisfaction = employee_data[employee_data['Gender'] == 'Female']['Satisfaction Rate (%)']
male_satisfaction = employee_data[employee_data['Gender'] == 'Male']['Satisfaction Rate (%)']
t_stat, p_value = stats.ttest_ind(female_satisfaction, male_satisfaction)

#Interpretation for T-test:
print(f"We performed an independent two-sample t-test to compare satisfaction rates between female and male employees.")
print(f"The t-statistic is {t_stat} and the p-value is {p_value}.")
if p_value < 0.05:
    print("\nInterpretation: There is a significant difference in satisfaction rates between genders.")
else:
    print("\nInterpretation: There is no significant difference in satisfaction rates between genders.")

