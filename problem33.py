from collections import namedtuple

# define the namedtuple with field names
Student = namedtuple('Student', ['ID', 'MARKS', 'NAME', 'CLASS'])

# read input
n = int(input())
columns = input().split()

# map column names to indices
column_indices = {column: index for index, column in enumerate(columns)}

# read student data and calculate sum of marks
marks_sum = 0
for _ in range(n):
    data = input().split()
    student = Student(ID=data[column_indices['ID']],
                      MARKS=int(data[column_indices['MARKS']]),
                      NAME=data[column_indices['NAME']],
                      CLASS=data[column_indices['CLASS']])
    marks_sum += student.MARKS

# calculate and print average marks
average_marks = marks_sum / n
print('{:.2f}'.format(average_marks))
