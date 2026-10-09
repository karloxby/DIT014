'''
    -   ask the user for their age and convert it to an integer

    -   ask whether they are a student (treat yes, Yes, YES, etc. as the same 
        answer)

    -   check whether the age is valid

    -   use if / elif / else to determine the fare

    -   select exactly one fare category

    -   for a valid age, assign the correct fare according to the rules, and print
        these parameters in the output: Age, Fare category, Price

    -   for an invalid age, display only Invalid age in the Fare category. Do not
        print any other parameters in the output

    -   display the result using an f-string

    fare rules

    passenger                       category                    fare
    age below 18                    child                       15 SEK    
    student, age 18-28              student                     24 SEK
    age 65 or above                 senior                      20 SEK
    everyone else                   adult                       36 SEK
    age below 0 or above 120        invalid age                 None

'''
# constants
CLIENT_NAME = "Northline Mobility"
CLIENT_TERM = ["Fare category:", "Age:", "Price:"]

# variables
accepted_student_values = ["yes", "no"]
category = ["Child", "Student", "Senior", "Adult", "Invalid age"]
fare = [15, 24, 20, 36]
currency = "SEK"

age_message = "How old are you?"
student_message = "Are you a student?"

age_error = "Error - Age has to be a number. Try again."
student_error = "Error - Must be a yes or no answer. Try again."

# main
age = input(f"\n{age_message}\n")

age_validated = False

while age_validated is not True:
    try:
        age = int(age)
        age_validated = True
    except ValueError:
        print(age_error)
        age = input(f"\n{age_message}\n")

student = input(f"\n{student_message}\n").lower()

student_validated = False

while student_validated is not True:
    if student in accepted_student_values:
        student_validated = True
    else:
        print(student_error)
        student = input(f"\n{student_message}\n")

if student == "yes":
    student = True
else:
    student = False

if age < 0 or age > 120:
    print(f"\n{CLIENT_NAME.upper()}")
    print(f"{CLIENT_TERM[0]:<20} {category[4]}\n")

elif age <= 120 and age >= 65:
    print(f"\n{CLIENT_NAME.upper()}")
    print(f"{CLIENT_TERM[0]:<20} {category[2]}")
    print(f"{CLIENT_TERM[1]:<20} {age}")
    print(f"{CLIENT_TERM[2]:<20} {fare[2]:.2f} {currency}\n")

elif age >=18 and age <= 25 and student:
    print(f"\n{CLIENT_NAME.upper()}")
    print(f"{CLIENT_TERM[0]:<20} {category[1]}")
    print(f"{CLIENT_TERM[1]:<20} {age}")
    print(f"{CLIENT_TERM[2]:<20} {fare[1]:.2f} {currency}\n")

elif age < 18:
    print(f"\n{CLIENT_NAME.upper()}")
    print(f"{CLIENT_TERM[0]:<20} {category[0]}")
    print(f"{CLIENT_TERM[1]:<20} {age}")
    print(f"{CLIENT_TERM[2]:<20} {fare[0]:.2f} {currency}\n")

else:
    print(f"\n{CLIENT_NAME.upper()}")
    print(f"{CLIENT_TERM[0]:<20} {category[3]}")
    print(f"{CLIENT_TERM[1]:<20} {age}")
    print(f"{CLIENT_TERM[2]:<20} {fare[3]:.2f} {currency}\n")

