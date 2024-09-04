class Student:
    def __init__(self, name):
        self.name = name  # Initialize the student's name
        self._grades = {}  # Initialize an empty dictionary to store grades

    def add_grade(self, course, grade):
        # Add or update the grade for the specified course
        self._grades[course] = grade

    def aggregate_average_grade(self):
        # Calculate the sum of all grades
        total_grades = sum(self._grades.values())
        # Calculate the number of courses
        num_courses = len(self._grades)
        # Calculate the average grade
        average_grade = total_grades / num_courses
        return average_grade  # Return the average grade

# Example usage:
student = Student("Alice")  # Create a student named Alice

student.add_grade("Math 101", 85)  # Add a grade of 85 for Math 101
student.add_grade("History 202", 90)  # Add a grade of 90 for History 202
student.add_grade("Science 303", 95)  # Add a grade of 95 for Science 303

print(student.aggregate_average_grade())  # Output the average grade
# => 90.0
