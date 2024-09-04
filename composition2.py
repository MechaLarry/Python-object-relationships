from datetime import datetime

class Student:
    all = []  # A list to keep track of all Student objects.

    def __init__(self, name):
        self.name = name  # Each Student has a name.
        Student.all.append(self)  # Add the student to the list of all students.

    def enroll_in_course(self, course):
        Enrollment(self, course)  # Create an Enrollment object for the student and course.

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]
        # Return a list of this student's enrollments.

    def courses(self):
        return [enrollment.course for enrollment in self.enrollments()]
        # Return a list of courses this student is enrolled in.

class Course:
    all = []  # A list to keep track of all Course objects.

    def __init__(self, title):
        self.title = title  # Each Course has a title.
        Course.all.append(self)  # Add the course to the list of all courses.

    def enrollments(self):
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]
        # Return a list of enrollments for this course.

    def students(self):
        return [enrollment.student for enrollment in self.enrollments()]
        # Return a list of students enrolled in this course.

    def enroll_student(self, student):
        Enrollment(student, self)  # Create an Enrollment object for the student and course.

class Enrollment:
    all = []  # A list to keep track of all Enrollment objects.

    def __init__(self, student, course):
        self.student = student  # Each Enrollment links to a Student.
        self.course = course  # Each Enrollment links to a Course.
        self.enrollment_date = datetime.now()  # Store the date of enrollment.
        Enrollment.all.append(self)  # Add the enrollment to the list of all enrollments.

# Example of using the classes
# Create Student objects
student1 = Student('Steve')
student2 = Student('Anna')

# Create Course objects
course1 = Course('Math 101')
course2 = Course('History 202')

# Enroll students in courses
student1.enroll_in_course(course1)
student1.enroll_in_course(course2)
student2.enroll_in_course(course1)

# Display students enrolled in each course
print(f"Students in {course1.title}: {[student.name for student in course1.students()]}")
print(f"Students in {course2.title}: {[student.name for student in course2.students()]}")

# Display courses each student is enrolled in
print(f"Courses for {student1.name}: {[course.title for course in student1.courses()]}")
print(f"Courses for {student2.name}: {[course.title for course in student2.courses()]}")
