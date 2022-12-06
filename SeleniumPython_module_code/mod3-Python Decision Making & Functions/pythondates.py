from _datetime import datetime

currentdate = datetime.now()
print(currentdate)
print(type(currentdate))

formattedDate = currentdate.strftime("%Y,%d %b")
print(formattedDate)
date = "28/09/2020"
string_formattedDate = datetime.strptime(date, "%d/%m/%Y")
print(string_formattedDate)

year = string_formattedDate.year
print(year)

date = string_formattedDate.day
print(date)

month = string_formattedDate.strftime("%B")
print(month)

desired_date = str(year)+ ","+str(date)+" " +month
print(desired_date)