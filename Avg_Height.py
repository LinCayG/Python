student_heights = input("Input a list of student heights, separated by a comma and this program will calculate the average height: \n").split(sep=",")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
height = 0
i = 0
for h in range(0, len(student_heights)):
    height = height + student_heights[h]
    i = i+1
avg_height = round(height/i, 0)
print(f"The average height of the students (rounded) is {avg_height}.")

