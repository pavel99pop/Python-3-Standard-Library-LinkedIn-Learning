# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()
print((now + timedelta(days = 2)).date())
print((now - timedelta(weeks = 5)).date())

print(calendar.month(2024, 2))
print(calendar.weekday(2024, 2, 2))
print(calendar.isleap(2024))