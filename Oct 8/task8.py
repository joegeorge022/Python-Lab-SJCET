from datetime import datetime
from pprint import PrettyPrinter

current_time = datetime.now()
print(current_time)

format_1 = current_time.strftime("%Y-%m-%d %H:%M:%S")              # Display the format [YYYY-MM-DD HH:MM:SS]
print(format_1)

format_2 = current_time.strftime("%m/%d/%Y")                       # Display the format [MM/DD/YYYY]
print(format_2)

format_3 = current_time.strftime("%A, %B %d, %Y")                  # Display the format [Day, Month DD, YYYY]
print(format_3)

format_4 = current_time.strftime("%A, %B %d, %Y %I:%M:%S %p")      # Display the format [Day, Month DD, YYYY HH:MM:SS AM/PM]
print(format_4)

format_5 = current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")       # Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
print(format_5)

format_6 = current_time.strftime("%a-%b-%d %H:%M:%S IST %Y")       # Display [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]
print(format_6)

format_7 = current_time.strftime("%B")                             # Display Month
print(format_7)

format_8 = current_time.strftime("%d-%m-%Y")                       # Display Date only
print(format_8)

format_9 = current_time.strftime("%H-%M-%S")                       # Display Time only
print(format_9)

format_10 = current_time.strftime("%B")                            # Display Month only
print(format_10)

format_11 = current_time.strftime("%Y")                            # Display Year only
print(format_11)
