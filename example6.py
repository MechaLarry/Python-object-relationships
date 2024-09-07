# With Intermediary Class
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay  # Base pay
        self.bonus = bonus  # Bonus pay

    def annual_salary(self):
        # Calculate the annual salary, including bonus
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age):
        self.name = name  # Employee's name
        self.age = age  # Employee's age
        self.compensations = []  # List to hold compensation records

    def add_compensation(self, compensation):
        # Associate the employee with a compensation (which includes salary)
        self.compensations.append(compensation)

    def total_salary(self):
        # Calculate the total salary for each compensation (if multiple salaries exist)
        return sum(comp.salary.annual_salary() for comp in self.compensations)


class Compensation:
    def __init__(self, employee, salary):
        self.employee = employee  # Link to the employee
        self.salary = salary  # Link to the salary


# Example Usage
salary = Salary(15000, 10000)  # Salary object
emp = Employee('Jeff', 25)  # Employee object
comp = Compensation(emp, salary)  # Intermediary linking Employee and Salary

emp.add_compensation(comp)  # Add the compensation to the employee
print(emp.total_salary())  # Prints: 190000
