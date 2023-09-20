import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 2: Load the Data
employee_data = pd.read_csv("/Users/susoeresia-eke/Downloads/hr_dashboard_data.csv")
# Display the first few rows of the dataset to get a sense of the data
employee_data.head()
employee_data.info()

# Step 3: Data Cleaning
# Check for missing values
missing_values = employee_data.isnull().sum()
print("Missing Values:\n", missing_values)

# Remove rows with missing values (if necessary)
employee_data.dropna(inplace=True)

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

