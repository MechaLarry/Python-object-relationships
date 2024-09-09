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
        # Calculate the total salary including any added compensations
        return sum(comp.salary.annual_salary() + comp.extra_compensation for comp in self.compensations)


class Compensation:
    def __init__(self, employee, salary, extra_compensation=0):
        self.employee = employee  # Link to the employee
        self.salary = salary  # Link to the salary
        self.extra_compensation = extra_compensation  # Additional compensation (e.g., perks, bonuses)


# Example Usage
salary = Salary(15000, 10000)  # Salary object
emp = Employee('Jeff', 25)  # Employee object

# Adding compensation with an additional $5000 as extra compensation
comp = Compensation(emp, salary, extra_compensation=5000)  # Intermediary linking Employee and Salary

emp.add_compensation(comp)  # Add the compensation to the employee
print(emp.total_salary())  # Prints: 195000 (Base salary + extra compensation)
print(f"Employee Name: {emp.name}, Total Salary: {emp.total_salary()}")