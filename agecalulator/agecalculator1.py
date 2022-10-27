import sys
from datetime import date

try:
    birthday = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    now = date.today()
    age = now - birthday

    print(f"You are {age.days / 365} years old")
    print(f"You've lived {age.days} days")

except ValueError as  err:
    print(f"ERROR: {err}")
