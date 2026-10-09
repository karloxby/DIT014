'''
    -   ask for students name and display in uppercase
    -   ask for number of study hours for seven days
    -   convert each input to an integer
    -   use a for loop to process the seven days
    -   calculate the total and average study hours
    -   count how many days were above the 2-hour target
    -   classify the student's weekly performance* based on average
    -   display the results using f-strings
    -   use the for loop to process each day's value and update the
        required totals and counters

'''

name = input("\nStudent name: \n")

total = 0
days_above_target = 0

performance = ""

hours_per_day = []

print("")
for day in range(1, 8):
    hours = int(input(f"Day {day}: "))
    hours_per_day.append(hours)


for hour in hours_per_day:
    total += hour
    average = total / len(hours_per_day)

    if hour > 2:
        days_above_target += 1

if average > 2:
    performance = "High"
elif average < 1:
    performance = "Low"
else:
    performance = "Moderate"

print(f"""
STUDYSPARK WEEK REVIEW

{'Student:':<24} {name.upper()}
{'Total:':<24} {total} hours
{'Average:':<24} {average:.2f} hours
{'Days above target:':<24} {days_above_target}
{'Performance:':<24} {performance}
""")
