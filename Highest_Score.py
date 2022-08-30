student_scores = input("This program will find the highest score.  Input a list of student scores, separated by a comma: \n").split(sep=",")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
score = student_scores[0]
for high in range(0, len(student_scores)):
    if score < int(student_scores[high]):
        score = int(student_scores[high])
print(f"The highest score is: {score}.")
