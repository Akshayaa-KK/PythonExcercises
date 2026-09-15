#1

teams = ['Data','AI','DevOps']

for team in teams:
        print("Hello",team,'Team from Inceptez Technologies')
        print("Keep Learning and Exploring")

#2

# Below code sums up student and trainers
'''
  Below code sums up
  student and trainers
'''

students = 100
trainers = 2
total = students + trainers
print(total)


#3
institution = "Inceptez's"
course = "Python"
audience = "Data Engineers & AI Engineers"

print(f'''This is {institution} "{course} class for {audience}"''' )

sentence = '''
Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.
'''
print(sentence)

#4

student_name = 'Akshaya Krishnakumar'
course_name = 'Python Fundamentals'
training_institute = "Inceptez Technologies"

print(f"{student_name} is learning the course {course_name} at the institute {training_institute}")

#5
fee = 45000
gst_percentage = 0.18
print(fee + 0.18)
#print(fee + 'Eighteen percent') # proves strongly typed characterstics of a language

#6

#2student = 'Ravi' #invalid
_student_id = 1001
studentName = 'Priya'
#class name = 'Python' invalid variable
inceptez_batch = 'Morning'

#7
PascalCase = 'DataEngineeringBatch'
camalCase = 'dataEngineeringBatch'
snake_case = 'data_engineering_batch'

print(PascalCase,camalCase,snake_case)


#8
age = input("Enter employee's Age: ")
print(type(age))
age = int(age)
remainingYears = 60-age
print(f"You will retire in {remainingYears} years at Inceptez Technologies ")

#9 Fix the type error in the following code for salary calculation:
salary = 50000
bonus = 10000
print('Total Salary in Inceptez:', salary + bonus)

#10
employee_name = input("Enter employee name: ")
base_salary = input("Enter base Salary: ")
hra_percent = input("Enter hra percentage: ")
bonus_amount= input("Enter bonus amount: ")

base_salary = float(base_salary)
hra_percent = int(hra_percent)
bonus_amount = int(bonus_amount)

hra = base_salary * (hra_percent/100)
total_salary = base_salary + bonus_amount + hra

print("Employee Name:", employee_name)
print("Base Salary:", base_salary)
print("HRA", hra)
print("Bonus", bonus_amount)
print("Total Salary Payable:", total_salary)

marks = input("Enter marks: ")

try:

        marks = float(marks)

        if marks >= 90:
                print("Outstanding")
        elif marks >= 75:
                print("Excellent")
        elif marks >= 50:
                print("Pass")
        else:
                print("Fail")

except ValueError:
        print("Invalid marks entered — Please provide numeric input.")


#11

item_name =  input("Enter product name: ")
price = input("Enter price: ")
quantity = input("Enter quantity: ")
price = float(price)
quantity = int(quantity)

total_cost = price * quantity
print(f"You purchased {quantity} units of {item_name}")
print(f"Total payable is:{total_cost} ")

