# b1. Identify the top 3 job roles with the highest number of employees hired based on education level.
def get_top_job_roles_by_education(HR_data):
    top_roles = HR_data.groupby(['Job_Role', 'Education_level'])['Employee_Number'].count().sort_values(ascending=False).head(3)
    return top_roles

# b2. Analyze the average monthly rate of employees based on a specific education level.
def calculate_average_monthly_rate(HR_data):
    average_rate = HR_data[HR_data['Education_level'] == 'Doctoral Degree']['Monthly_Rate'].mean()
    return average_rate

# b3. Analyze the average duration of employment for employees in a specific department within the company.
def calculate_average_employment_duration(HR_data):
    average_duration = HR_data[HR_data['Department'] == 'HR']['Total_Working_Years'].mean()
    return average_duration

# b4. Derive meaningful insights based on a unique selection (distinct from the previous requirements).
# Top 10 employee numbers whose satisfaction level is greater than 3 and who have not been promoted in the last 5 years.
# Show Employee Number, Department, Job_Role, Job Satisfaction, and Years_Since_Last_Promotion.
def get_top_10_satisfied_employees(HR_data):
    top_employees = HR_data[
        (HR_data['Job_Satisfaction'] > 3) & (HR_data['Years_Since_Last_Promotion'] >= 5)
    ].head(10)[['Employee_Number', 'Department', 'Job_Role', 'Job_Satisfaction', 'Years_Since_Last_Promotion']]
    return top_employees
