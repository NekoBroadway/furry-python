#Exc 3 - Print to display current date and time YYYY-MM-DD HH:MM:SS

from datetime import datetime

today = datetime.now()

print("Actual datetime is - {}-{}-{} {}:{}:{}".format(today.year, today.month, today.day, today.hour, today.minute, today.second))