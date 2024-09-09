#without intermediary class
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay  # Storing pay
        self.bonus = bonus  # Storing bonus

    def annual_salary(self):
        # Calculate annual salary by multiplying pay by 12 and adding the bonus
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name  # Store the name of the employee
        self.age = age  # Store the age of the employee
        # Create a Salary object inside the Employee class (composition)
        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        # Return the calculated annual salary from the Salary object
        return self.obj_salary.annual_salary()


# Now pass the pay and bonus directly to the Employee constructor
emp = Employee('Jeff', 25, 15000, 10000)
print(emp.total_salary())  # This will print Jeff's total salary



