# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print('When is this?\n' + now.strftime('%H:%M:%S %p - %b %d %Y'))