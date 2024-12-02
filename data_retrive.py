# a1. Retrieve the Gender, Age, Marital Status, and Department based on the Employee number
def retrieve_employee_info(data, employee_number):
    for row in data:
        if row['Employee_Number'] == str(employee_number):  
            gender = row['Gender']
            age = row['Age']
            marital_status = row['Marital_Status']
            department = row['Department']
            return gender, age, marital_status, department
    return None


# a2. Retrieve the Department, Education Level, Total Working Years, and Standard Hours
# associated with a specific Job Role.
def retrieve_job_role_info(data, job_role):
    result = []
    for row in data:
        if row['Job_Role'] == job_role: 
            department = row['Department']
            education_level = row['Education_level']
            total_working_years = row['Total_Working_Years']
            standard_hours = row['Standard_Hours']
            result.append([department, education_level, total_working_years, standard_hours])
    return result


# a3. Retrieve the Employee Number, Job Role, Marital Status, and Hourly Rate of employees 
# whose Standard Hours are less than 60 hours based on the department.
def retrieve_employees_with_low_standard_hours(data, department_name):
    result = []
    for row in data:
        if row['Department'] == department_name and int(row['Standard_Hours']) < 60:
            employee_number = row['Employee_Number']
            job_role = row['Job_Role']
            marital_status = row['Marital_Status']
            hourly_rate = row['Hourly_Rate']
            result.append([employee_number, job_role, marital_status, hourly_rate])
    return result

# a4. Retrieve the Employee Number, Monthly Income, and Years at Company for employees
# who have a high satisfaction level.
def retrieve_employees_with_high_satisfaction(data, job_role):
    result = []
    for row in data:
        if row['Job_Role'] == job_role and int(row['Job_Satisfaction']) > 3:
            employee_number = row['Employee_Number']
            monthly_income = row['Monthly_Income']
            years_at_company = row['Years_At_Company']
            result.append([employee_number, monthly_income, years_at_company])
    return result
