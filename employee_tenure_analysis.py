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