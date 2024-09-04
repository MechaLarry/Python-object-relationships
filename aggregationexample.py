from datetime import datetime

# Define the Student class
class Student:
    all = []  # A list to keep track of all Student objects

    def __init__(self, name):
        self.name = name  # Each Student has a name
        self._enrollments = []  # Initialize an empty list for enrollments
        self._grades = {}  # Initialize an empty dictionary for grades
        Student.all.append(self)  # Add the student to the list of all students

    def enroll_in_course(self, course):
        Enrollment(self, course)  # Create an Enrollment object for the student and course

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]
        # Return a list of this student's enrollments

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]
        # Return a list of courses this student is enrolled in

    def course_count(self):
        return len(self._enrollments)
        # Return the number of courses the student is enrolled in

    def aggregate_average_grade(self):
        if not self._grades:
            return 0  # Avoid division by zero if there are no grades
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        average_grade = total_grades / num_courses
        return average_grade

# Define the Course class
class Course:
    all = []  # A list to keep track of all Course objects

    def __init__(self, title):
        self.title = title  # Each Course has a title
        Course.all.append(self)  # Add the course to the list of all courses

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]
        # Return a list of enrollments for this course

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]
        # Return a list of students enrolled in this course

    def enroll_student(self, student):
        Enrollment(student, self)  # Create an Enrollment object for the student and course

# Define the Enrollment class
class Enrollment:
    all = []  # A list to keep track of all Enrollment objects

    def __init__(self, student, course):
        self.student = student  # Each Enrollment links to a Student
        self.course = course  # Each Enrollment links to a Course
        self.enrollment_date = datetime.now()  # Store the date of enrollment
        Enrollment.all.append(self)  # Add the enrollment to the list of all enrollments

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.enrollment_date.date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

# Example usage of the classes and aggregate methods
if __name__ == "__main__":
    # Create Student and Course objects
    student1 = Student('Steve')
    student2 = Student('Anna')
    course1 = Course('Math 101')
    course2 = Course('History 202')

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student1.enroll_in_course(course2)
    student2.enroll_in_course(course1)

    # Assign grades to students
    # Note: We need to create enrollments before assigning grades
    for enrollment in student1.enrollments():
        student1._grades[enrollment] = 90 if enrollment.course == course1 else 85
    for enrollment in student2.enrollments():
        student2._grades[enrollment] = 88

    # Display results
    print(f"Courses for {student1.name}: {[course.title for course in student1.courses()]}")
    print(f"Number of courses for {student1.name}: {student1.course_count()}")
    print(f"Average grade for {student1.name}: {student1.aggregate_average_grade()}")

    print(f"Enrollments per day: {Enrollment.aggregate_enrollments_per_day()}")
