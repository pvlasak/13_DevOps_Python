from datetime import datetime

input_user = input("Please enter your task and deadline as comma separate date. Task and deadline are divided by semi-colon!\n")
input_list = input_user.split(":")
print(input_list)

task = input_list[0]
deadline = input_list[1].strip()

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
print(deadline_date)
today_date = datetime.today()
print(today_date)
time_remaining = (deadline_date-today_date)
print(f'Number of hours remaining to meet the deadline: {int(time_remaining.total_seconds() / 60 / 60 )} hours.')
