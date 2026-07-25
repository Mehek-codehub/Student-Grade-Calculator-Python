def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding Performance!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good Job! You can do even better!"
    elif marks >= 60:
        return "D", "Keep Practicing! Success is near!"
    else:
        return "F", "Don't Give Up! Work Hard and Try Again!"


# Get student name
Student_name = input("Enter the student name: ")

# Get valid marks
while True:
    try:
        marks = int(input("Enter Marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")

    except ValueError:
        print("Please enter valid numeric marks.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display Result
print("\n==============================")
print(" STUDENT GRADE REPORT")
print("==============================")
print(f"Student Name : {Student_name.upper()}")
print(f"Marks        : {marks}/100")
print(f"Grade        : {grade}")
print(f"Message      : {message}")
print("==============================")