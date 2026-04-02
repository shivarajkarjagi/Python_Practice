if __name__ == '__main__':
    # Read the number of students
    n = int(input())
    
    student_marks = {}
    for _ in range(n):
        # Unpack name and the list of scores
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    # The name of the student to look up
    query_name = input()
    
    if query_name in student_marks:
        marks_list = student_marks[query_name]
        # Calculate average
        avg = sum(marks_list) / len(marks_list)
        # Format to 2 decimal places
        print(f"{avg:.2f}")
