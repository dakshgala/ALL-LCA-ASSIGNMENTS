#Problem Statement: Student Data Management Using Python Collections
#Write a Python program to create and store student information using a Dictionary, Tuple, and List. Perform the following operations on the Dictionary:
#Add a new student record.
#Delete an existing student record.
#Update the details of a student.
#Display the final student records after performing all the operations.
#Use suitable student attributes such as Roll Number, Name, Branch, and Marks.


Assignment 1: Student Data Management Using Python Collections
- Dictionary : main storage  {roll_no: (name, branch, marks)}
- Tuple      : one student's record (immutable, so update = replace the tuple)
- List       : initial records, and the list of roll numbers for display


# List of tuples used to load the initial data
initial_records = [
    (101, "Aarav Shah", "CSE AI-DS", 88),
    (102, "Riya Mehta", "CSE AI-DS", 92),
    (103, "Kabir Singh", "IT", 75),
]

# Dictionary: key = Roll Number, value = tuple (Name, Branch, Marks)
students = {}
for roll, name, branch, marks in initial_records:
    students[roll] = (name, branch, marks)


def add_student(roll, name, branch, marks):
    if roll in students:
        print(f"Roll number {roll} already exists. Use update instead.")
    else:
        students[roll] = (name, branch, marks)
        print(f"Student {roll} added.")


def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f"Student {roll} deleted.")
    else:
        print(f"Roll number {roll} not found.")


def update_student(roll, name=None, branch=None, marks=None):
    if roll not in students:
        print(f"Roll number {roll} not found.")
        return
    old_name, old_branch, old_marks = students[roll]
    # Tuples can't be modified, so build a new tuple and replace the old one
    students[roll] = (
        name if name is not None else old_name,
        branch if branch is not None else old_branch,
        marks if marks is not None else old_marks,
    )
    print(f"Student {roll} updated.")


def display_students(title="Student Records"):
    print(f"\n--- {title} ---")
    if not students:
        print("No records available.")
        return
    print(f"{'Roll No':<10}{'Name':<20}{'Branch':<15}{'Marks':<6}")
    print("-" * 51)
    rolls = sorted(students.keys())  # list of roll numbers
    for roll in rolls:
        name, branch, marks = students[roll]
        print(f"{roll:<10}{name:<20}{branch:<15}{marks:<6}")


def main():
    while True:
        print("\n===== Student Data Management =====")
        print("1. Add a student")
        print("2. Delete a student")
        print("3. Update a student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                roll = int(input("Roll Number: "))
                name = input("Name: ").strip()
                branch = input("Branch: ").strip()
                marks = float(input("Marks: "))
                add_student(roll, name, branch, marks)

            elif choice == "2":
                roll = int(input("Roll Number to delete: "))
                delete_student(roll)

            elif choice == "3":
                roll = int(input("Roll Number to update: "))
                print("Press Enter to keep the current value.")
                name = input("New Name: ").strip() or None
                branch = input("New Branch: ").strip() or None
                m = input("New Marks: ").strip()
                marks = float(m) if m else None
                update_student(roll, name, branch, marks)

            elif choice == "4":
                display_students()

            elif choice == "5":
                display_students("Final Student Records")
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Roll number and marks must be numbers.")


if __name__ == "__main__":
    main()
