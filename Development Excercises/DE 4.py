#Hugo
#Development Excercise 4

print("This program will take in an exam mark and return the relevant grade.")
mark = float(input("Please enter your mark: "))
if mark <= 100 and mark >= 81:
    print("Grade A")
elif mark <= 80 and mark >= 71:
    print("Grade B")
elif mark <= 70 and mark >= 61:
    print("Grade C")
elif mark <=60 and mark >=51:
    print("Grade D")
elif mark <=50 and mark >=41:
    print("Grade E")
elif mark <= 40:
    print("Grade U")
else:
    print("That is not a valid mark.")
