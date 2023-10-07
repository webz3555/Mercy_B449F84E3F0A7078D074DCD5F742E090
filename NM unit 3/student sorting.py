class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:

# Create some student objects
students = [
    Student("Alice", "A101", 3.8),
    Student("Bob", "B102", 3.9),
    Student("Charlie", "C103", 3.7),
    Student("David", "D104", 3.5),
    Student("Eve", "E105", 3.9),
]

# Sort the students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
