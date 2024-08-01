# Create a Timer with the Time module
import time

userIn = input('Run? >')

seconds = 1
if userIn == 'yes':
    while seconds < 10:
        print(seconds)
        time.sleep(1)
        seconds += 1
    print(10)