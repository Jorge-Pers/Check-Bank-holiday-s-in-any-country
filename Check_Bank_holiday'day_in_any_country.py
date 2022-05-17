# importing holidays module
import holidays
from datetime import date

#Select the country
country = input("Enter the country please : ")
#holidays date
date = input("Enter the date please yyyy-mm-dd: ")

#calculate

def calculate_holidays(date,country):
    country_holiday = holidays.country_holidays(country)
    name_holiday = country_holiday.get(date)
    print(date,name_holiday)
calculate_holidays(date,country)
