class Student:
    def __init__(self, name):
        self.name = name  # Initialize the student's name
        self._enrollments = []  # Initialize an empty list to store enrollments

    def enroll_in_course(self, course):
        self._enrollments.append(course)  # Add a course to the student's enrollments

    def course_count(self):
        # Return the number of courses (enrollments) the student is part of
        return len(self._enrollments)

# Example usage:
student = Student("Alice")  # Create a student named Alice
course1 = "Math 101"  # Example course 1
course2 = "History 202"  # Example course 2

student.enroll_in_course(course1)  # Alice enrolls in Math 101
student.enroll_in_course(course2)  # Alice enrolls in History 202

print(student.course_count())  # Output the number of courses Alice is enrolled in
# => 2



