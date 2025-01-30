def number_of_day_in_a_year(string_date):

    #returning the number of day in a year

    year,month,day=map(int,string_date.split("-"))#splitting the input string "-" for accessing year,month,date

    days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #storing the no.of datys in each month in a list

    if (year%4==0 and year%100!=0) or year%400==0: #checking if the year is lear year or not if it add one in february month
        days_in_month[1]=29

    return sum(days_in_month[:month-1])+day #previous month total days + current date

string_date="2024-11-24"
print(number_of_day_in_a_year(string_date))
