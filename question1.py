#Get a Leap Year
year =int(input ('Enter the year:'))

#year is a century i.e divisible by 100
if year % 100 == 0:
#for a centuary to be a leap year it must be divible by 400
    if year % 400 == 0:
        print(True)
    else:
        print(False)
# year is divible by 4
elif year % 4 == 0:
    print(True)

#if all the conditions are not met then the year is definately not a leap year
else:
    print(False)
