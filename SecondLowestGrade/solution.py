# ============================================
# Problem  : Second Lowest Grade
# Platform : HackerRank
# Topic    : Nested Lists
# Language : Python
# ============================================

if __name__ == '__main__':

    # Step 1: Create an empty list to store all students
    students = []

    # Step 2: Read the number of students
    n = int(input("Enter the number of students: "))

    # Step 3: Loop n times to read each student's name and score
    for _ in range(n):

        name = input("Enter student name: ")          # Read student name
        score = float(input("Enter student score: ")) # Read student score as a decimal number

        # Store each student as [name, score] inside the students list
        # This creates a nested list like [['Harry', 37.21], ['Berry', 37.21], ...]
        students.append([name, score])

    # Step 4: Extract all unique grades and sort them in ascending order
    # set()    → removes duplicate grades
    # sorted() → arranges grades from lowest to highest
    # s[1]     → gets the grade (index 1) from each student [name, grade]
    grades = sorted(set(s[1] for s in students))
    # Example: [37.2, 37.21, 39, 41]

    # Step 5: Pick the second lowest grade
    # grades[0] → lowest grade
    # grades[1] → second lowest grade
    second_lowest = grades[1]

    # Step 6: Filter students who have the second lowest grade
    # s[1] == second_lowest → keep only matching students
    # s[0]                  → get their name
    # sorted()              → sort names alphabetically
    result = sorted(s[0] for s in students if s[1] == second_lowest)
    # Example: ['Berry', 'Harry']

    # Step 7: Print the result
    print("\nStudents with the second lowest grade:")
    print("---------------------------------------")
    for name in result:
        print(name)
