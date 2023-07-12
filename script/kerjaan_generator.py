from datetime import date, datetime, timedelta

today = date.today() - timedelta(days=1)

first = datetime.combine(today, datetime.strptime("08:00:00", "%H:%M:%S").time())
second = first + timedelta(hours=2, minutes=1)
rest = second + timedelta(hours=2, minutes=1)
third = datetime.combine(today, datetime.strptime("13:00:00", "%H:%M:%S").time())
fourth = third + timedelta(hours=2, minutes=1)

print(first.strftime('%m/%d/%Y %H:%M:%S') + " - " + (first + timedelta(hours=2)).strftime('%m/%d/%Y %H:%M:%S'))
print(second.strftime('%m/%d/%Y %H:%M:%S') + " - " + (second + timedelta(hours=2)).strftime('%m/%d/%Y %H:%M:%S'))
print(rest.strftime('%m/%d/%Y %H:%M:%S') + " - " + (third - timedelta(minutes=1)).strftime('%m/%d/%Y %H:%M:%S') + " Istirahat")
print(third.strftime('%m/%d/%Y %H:%M:%S') + " - " + (third + timedelta(hours=2)).strftime('%m/%d/%Y %H:%M:%S'))
print(fourth.strftime('%m/%d/%Y %H:%M:%S') + " - " + (fourth + timedelta(hours=2)).strftime('%m/%d/%Y %H:%M:%S'))
