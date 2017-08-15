import sys
import string
import time
from time import sleep

sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print("Usage: [ python ] alarm_clock.py duration_in_minutes")
    print("Example: [ python ] alarm_clock.py 10")
    print("Use a value of 0 minutes for testing the alarm immediately.")
    print("Press Ctrl-C to terminate the alarm clock early.")
    sys.exit(1)

try:
    minutes = int(sa[1])
except ValueError:
    print("Invalid numeric value (%s) for minutes.") % sa[1]
    print("If you need to use a timer for this, just go already.")
    sys.exit(1)

if minutes < 0:
    print("Are you sure?")
    sys.exit(1)

seconds = minutes * 60

try:
    while minutes > 0:
        minutes -= 1
        if minutes == 1:
            unit_word = " minute"
        else:
            unit_word = " minutes"
        print("You have " + str(minutes) + unit_word + " to go.")
        sleep(60)
    print("You're late! You're late for a very important date!")
except KeyboardInterrupt:
    print("clock stopped.")
    sys.exit(1)
