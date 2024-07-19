# DAYS ALIVE by ARMAGEDDON

from datetime import datetime

def days_alive(birthdate):
    today = datetime.now()
    birthdate = datetime.strptime(birthdate, "%m-%d-%Y")
    days_alive = (today - birthdate).days
    return days_alive

your_birthdate = input("Introduce your birthdate (MONTH-DAY-YEAR): ") 
#If you wanna get your days alive you have to pot this "-" bettween MONTH-DAYS-YEARS 
#FOR EXAMPLE: 10-9-2004 

days = days_alive(your_birthdate)


print(f"You have been alive for {days} days")

