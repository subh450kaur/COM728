import matplotlib.pyplot as plt

# c1  Function to visualize the proportion of employees by education level
def proportion_of_employees_by_education(HR_data):
    if 'Education_level' not in HR_data.columns:
        raise KeyError("The column 'Education_level' is missing in the dataset.")
        
    # Count the occurrences of each education level
    education_level_counts = HR_data['Education_level'].value_counts()

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        education_level_counts, 
        labels=education_level_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired(range(len(education_level_counts)))
    )
    plt.title('Proportion of Employees by Education Level', fontsize=14)
    plt.show()

# c2 Function to visualize the frequency of employee training by education field
def employee_training_frequency(HR_data):
    if 'Education_Field' not in HR_data.columns or 'Training_Times_Last_Year' not in HR_data.columns:
        raise KeyError("Required columns ('Education_Field', 'Training_Times_Last_Year') are missing in the dataset.")
        
    # Sum training times grouped by education field
    training_counts = HR_data.groupby('Education_Field')['Training_Times_Last_Year'].sum()

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    bar_colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
    plt.bar(training_counts.index, training_counts.values, color=bar_colors[:len(training_counts)])
    plt.xlabel('Education Field', fontsize=12)
    plt.ylabel('Total Training Times', fontsize=12)
    plt.title('Frequency of Employee Training by Education Field', fontsize=14)
    plt.xticks(rotation=45, ha='right')

    # Display data labels
    for i, value in enumerate(training_counts.values):
        plt.text(i, value, str(value), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

# c3 Function to visualize job satisfaction scores across job levels for each department
def job_satisfaction_across_levels(HR_data):
    if 'Department' not in HR_data.columns or 'Job_Level' not in HR_data.columns or 'Job_Satisfaction' not in HR_data.columns:
        raise KeyError("Required columns ('Department', 'Job_Level', 'Job_Satisfaction') are missing in the dataset.")
        
    # Calculate average job satisfaction grouped by department and job level
    satisfaction_by_level = HR_data.groupby(['Department', 'Job_Level'])['Job_Satisfaction'].mean().reset_index()

    # Define colors for departments
    department_colors = {'Sales': 'blue', 'R&D': 'green', 'HR': 'red'}

    # Plot job satisfaction scores
    plt.figure(figsize=(12, 6))
    for department in satisfaction_by_level['Department'].unique():
        dept_data = satisfaction_by_level[satisfaction_by_level['Department'] == department]
        plt.plot(dept_data['Job_Level'], dept_data['Job_Satisfaction'], marker='o', label=department, color=department_colors.get(department, 'gray'))

    plt.title('Job Satisfaction Across Job Levels by Department', fontsize=14)
    plt.xlabel('Job Level', fontsize=12)
    plt.ylabel('Average Job Satisfaction', fontsize=12)
    plt.legend(title="Department")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to visualize average monthly income by job role
def average_monthly_income_by_role(HR_data):
    if 'Job_Role' not in HR_data.columns or 'Monthly_Income' not in HR_data.columns:
        raise KeyError("Required columns ('Job_Role', 'Monthly_Income') are missing in the dataset.")
        
    # Calculate and sort average monthly income
    avg_income = HR_data.groupby('Job_Role')['Monthly_Income'].mean().reset_index()
    sorted_income = avg_income.sort_values('Monthly_Income', ascending=False)

    # Create a bar plot
    plt.figure(figsize=(12, 6))
    bar_plot = plt.bar(
        sorted_income['Job_Role'], 
        sorted_income['Monthly_Income'], 
        color=plt.cm.Paired(range(len(sorted_income)))
    )
    plt.xlabel('Job Role', fontsize=12)
    plt.ylabel('Average Monthly Income', fontsize=12)
    plt.title('Average Monthly Income by Job Role', fontsize=14)
    plt.xticks(rotation=45, ha='right')

    # Annotate bars with values
    for bar in bar_plot:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2, 
            height, 
            f'{height:.2f}', 
            ha='center', 
            va='bottom', 
            fontsize=10
        )

    plt.tight_layout()
    plt.show()
