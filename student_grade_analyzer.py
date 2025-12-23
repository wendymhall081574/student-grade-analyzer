# Student Grade Analyzer
# Sophia Python Touchstone
# Wendy Lassiter

def calculate_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Student Grade Analyzer")

    grades = []

    while True:
        entry = input("Enter a grade (or type 'done' to finish): ")

        if entry.lower() == "done":
            break

        try:
            grade = float(entry)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    if len(grades) == 0:
        print("No grades entered.")
        return

    average = sum(grades) / len(grades)
    letter = calculate_letter_grade(average)

    print(f"\nGrades Entered: {grades}")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter}")

if __name__ == "__main__":
    main()
