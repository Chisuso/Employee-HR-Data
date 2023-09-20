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

# Automated Interpretation for T-test:
print(f"We performed an independent two-sample t-test to compare satisfaction rates between female and male employees.")
print(f"The t-statistic is {t_stat} and the p-value is {p_value}.")
if p_value < 0.05:
    print("\nInterpretation: There is a significant difference in satisfaction rates between genders.")
else:
    print("\nInterpretation: There is no significant difference in satisfaction rates between genders.")

# Case 2: Employee Productivity Analysis: Analyze the factors affecting employee productivity and identify top-performing employees.
# Step 3: Descriptive Statistics and Visualization
# Calculate summary statistics
summary_stats = employee_data[['Projects Completed', 'Productivity (%)', 'Satisfaction Rate (%)', 'Feedback Score']].describe()

# Visualize key variables
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.hist(employee_data['Projects Completed'], bins=15, edgecolor='k')
plt.xlabel('Projects Completed')
plt.ylabel('Frequency')
plt.title('Distribution of Projects Completed')

# Subplot Interpretation:
proj_peak = employee_data['Projects Completed'].mode().values[0]
print(f"Subplot Interpretation:")
print(f"The histogram shows the distribution of projects completed by employees.")
print(f"Most employees have completed a moderate number of projects, with a peak around {proj_peak} projects.")

plt.subplot(2, 2, 2)
plt.hist(employee_data['Productivity (%)'], bins=15, edgecolor='k')
plt.xlabel('Productivity (%)')
plt.ylabel('Number of Employees')
plt.title('Distribution of Productivity')

# Subplot Interpretation:
prod_peak = employee_data['Productivity (%)'].mode().values[0]
print("\nSubplot Interpretation:")
print("The histogram displays the distribution of employee productivity scores.")
print(f"The majority of employees have productivity scores around {prod_peak}%.")

plt.subplot(2, 2, 3)
plt.hist(employee_data['Satisfaction Rate (%)'], bins=15, edgecolor='k')
plt.xlabel('Satisfaction Rate (%)')
plt.ylabel('Number of Employees')
plt.title('Distribution of Satisfaction Rate')

# Subplot Interpretation:
sat_peak = employee_data['Satisfaction Rate (%)'].mode().values[0]
zero_satisfaction = (employee_data['Satisfaction Rate (%)'] == 0).sum()
print("\nSubplot Interpretation:")
print("The histogram illustrates the distribution of employee satisfaction rates.")
print(f"Most employees have satisfaction rates around >40%, indicating moderate satisfaction levels.")
print(f"Only {zero_satisfaction} employee has a satisfaction rate of 0%.")

plt.subplot(2, 2, 4)
plt.hist(employee_data['Feedback Score'], bins=5, edgecolor='k')
plt.xlabel('Feedback Score')
plt.ylabel('Number of Employees')
plt.title('Distribution of Feedback Score')

# Subplot Interpretation:
feedback_peak = employee_data['Feedback Score'].mode().values[0]
print("\nSubplot Interpretation:")
print("The histogram represents the distribution of feedback scores.")
print(f"Feedback scores are concentrated around {feedback_peak}, indicating a tendency towards positive feedback.")

plt.tight_layout()
plt.show()

# Some More Productivity Analysis
# Calculate average projects completed per employee
avg_projects_per_employee = employee_data['Projects Completed'].mean()

# Group by department and analyze productivity
department_productivity = employee_data.groupby('Department')['Projects Completed'].mean()

# Inferential Statistics
# Perform a t-test to compare productivity between departments
hr_projects = employee_data[employee_data['Department'] == 'HR']['Projects Completed']
it_projects = employee_data[employee_data['Department'] == 'IT']['Projects Completed']
t_stat, p_value = stats.ttest_ind(hr_projects, it_projects)

# Step 6: Insights and Recommendations
# Print summary statistics and insights
print("\nSummary Statistics:\n", summary_stats)
print(f"\nAverage Projects Completed per Employee: {avg_projects_per_employee:.2f}")

print("\nDepartmental Productivity:")
print(department_productivity)

print("\nT-test Results:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

#Case 3: Employee Tenure Analysis: Analyze the impact of employee tenure on productivity and satisfaction.
# Calculate Tenure in Years
def calculate_tenure(joining_date):
    # Extract the last two digits of the year from the Joining Date assuming it is currently Dec, 2022
    year_str = joining_date.split('-')[1].strip()

    if year_str == '98':
        return 24  # 24 years of tenure
    elif year_str == '99':
        return 23  # 23 years of tenure
    else:
        # Convert year_str to an integer and calculate tenure
        joining_year = int(year_str)
        current_year = 22  # Assuming current year is December 2022
        return current_year - joining_year


employee_data['Tenure (Years)'] = employee_data['Joining Date'].apply(calculate_tenure)

# Descriptive Statistics and Visualization
# Calculate summary statistics for tenure
summary_stats = employee_data['Tenure (Years)'].describe()

# Visualize tenure distribution
plt.figure(figsize=(10, 6))
plt.hist(employee_data['Tenure (Years)'], bins=15, edgecolor='k')
plt.xlabel('Tenure (Years)')
plt.ylabel('Number of Employees')
plt.title('Distribution of Employee Tenure')

# Histogram Interpretation:
tenure_median = employee_data['Tenure (Years)'].median()
tenure_min = employee_data['Tenure (Years)'].min()
tenure_max = employee_data['Tenure (Years)'].max()
print("Histogram Interpretation:")
print("The histogram shows the distribution of employee tenure in years.")
print(f"The median tenure is {tenure_median} years.")
print(f"The minimum tenure is {tenure_min} years, and the maximum is {tenure_max} years.")

plt.tight_layout()
plt.show()

# Tenure Analysis
# Calculate average tenure
avg_tenure = employee_data['Tenure (Years)'].mean()

# Group by department and analyze tenure
department_tenure = employee_data.groupby('Department')['Tenure (Years)'].mean()

# Inferential Statistics
# Perform a t-test to compare tenure between departments
hr_tenure = employee_data[employee_data['Department'] == 'HR']['Tenure (Years)']
it_tenure = employee_data[employee_data['Department'] == 'IT']['Tenure (Years)']
t_stat, p_value = stats.ttest_ind(hr_tenure, it_tenure)

# Insights and Recommendations
# Print summary statistics and insights
print("\nSummary Statistics:\n", summary_stats)
print(f"\nAverage Employee Tenure: {avg_tenure:.2f} years")

print("\nDepartmental Tenure:")
print(department_tenure)

print("\nT-test Results:")
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")