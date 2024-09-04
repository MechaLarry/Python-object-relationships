from datetime import datetime

class Enrollment:
    all = []  # Class-level list to store all enrollments

    def __init__(self, student, course):
        self.student = student  # Associate the student with this enrollment
        self.course = course  # Associate the course with this enrollment
        self.enrollment_date = datetime.now()  # Record the current date and time of enrollment
        Enrollment.all.append(self)  # Add this enrollment to the class-level list

    def get_enrollment_date(self):
        # Return the date part of the enrollment date
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}  # Initialize an empty dictionary to count enrollments per day
        for enrollment in cls.all:
            # Get the date of the enrollment (ignoring time)
            date = enrollment.get_enrollment_date().date()
            # Increment the count for this date in the dictionary
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

# Example usage:
student1 = "Alice"  # Example student 1
course1 = "Math 101"  # Example course 1

enrollment1 = Enrollment(student1, course1)  # Alice enrolls in Math 101

# Simulate another enrollment on the same day
enrollment2 = Enrollment("Bob", "History 202")  # Bob enrolls in History 202

# Print the count of enrollments per day
print(Enrollment.aggregate_enrollments_per_day())
# => {datetime.date(2024, 9, 4): 2}
