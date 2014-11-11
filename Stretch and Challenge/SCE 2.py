#Hugo
#Stretch and Challenge Exercise 2



date = str(input("Please enter a date in the format DD/MM/YY: "))
day = date[:2]
month = date[3:5]
year = date[6:8]

if month == "01":
    month = ("January")
elif month == "02":
    month = ("February")
elif month == "03":
    month = ("March")
elif month == "04":
    month = ("April")
elif month == "05":
    month = ("May")
elif month == "06":
    month = ("June")
elif month == "07":
    month = ("July")
elif month == "08":
    month = ("August")
elif month == "09":
    month = ("September")
elif month == "10":
    month = ("October")
elif month == "11":
    month = ("November")
elif month == "12":
    month = ("December")
else:
   print = ("Invalid month")

if day == "01":
    day = "1st"
elif day == "02":
    day = "2nd"
elif day == "03":
    day = "3rd"
elif day == "21":
    day = "21st"
elif day == "22":
    day = "22nd"
elif day == "23":
    day = "23rd"

print("{0} {1} 20{2}".format(day, month, year))
