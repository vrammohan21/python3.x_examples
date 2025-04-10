if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name of the student: ")
    if query_name in student_marks.keys():
        print("{:.2f}".format(sum(student_marks[query_name])/3))

print(f"sum of 1,2,3 = {sum([1,2,3])}")