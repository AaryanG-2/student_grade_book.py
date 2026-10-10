grades = {("Liam" : 50,)
          ["Raj" :  5,]
          ["Bob" : 93,]
          ["Arjun" : 100,]
          ["Andrew" : 82]
          }
total_grades = 0
total_students = 0
for i in grades:
    total_grades + grades(i)
    total_students += 1
class_average = (total_grades / total_students)
print(f"The class average is = {class_average}")
highest_scorer = max(grades)
print(f"Highest grade = {highest_scorer}")
lowest_scorer = min(grades)
print(f"Lowest grade = {lowest_scorer}")
print(grades.get("Arjun"))
user_request = input("Enter the student whose grades you want to see: ")
grades.get(user_request)