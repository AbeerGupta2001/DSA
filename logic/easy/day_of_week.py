import datetime

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Webnesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def day_of_week(d=30,m=8,y=2010):
    date = datetime.date(y,m,d)
    return date.weekday()


print(days[day_of_week(15,6,1995)])