#Hugo
#Selection - Development Excercise 3
#03/10/14

print("This program calculates your wage (taking overtime into account).")
print("You will need to enter how many hours you have worked and how much your hourly rate of wage is.")
hours_worked = float(input("Please enter how many hours you have worked: "))
hourly_pay = float(input("Please enter how much you are usually paid per hour: "))
if hours_worked > 0 and hours_worked < 60:
    if hours_worked > 40:
        overtime = hours_worked - 40
        normal_pay = 40*hourly_pay
        overtime_pay = 1.5*hourly_pay*overtime
        total_pay = normal_pay + overtime_pay
        print("Your total pay is £{0}.".format(total_pay))
    else:
        total_pay = hours_worked*hourly_pay
        print("Your total pay is £{0}.".format(total_pay))
else:
    print("Invalid.")


