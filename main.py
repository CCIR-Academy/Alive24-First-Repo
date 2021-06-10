# This block of code tries to output some information about the current date and time properly, 
# but it contains some errors that need to be fixed and submitted as part of a pull request.
import datetime

monthCodeList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
weekdayCodeList = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
now = datetime.datetime.now()


print("This is the year %s." % now.year)
print("We are in %s now." % monthCodeList[now.month-1])
print("It's %s today." % weekdayCodeList[now.weekday()])