
from typing import Counter

num_list=[]
week_days_list=[
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "saturday",
]

print(num_list)
Counter=0

for day in week_days_list:
    Counter+=1
    print(f"The {Counter} day is ----->{day}")