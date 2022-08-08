year = int(input('We are going to check to see if a year is a leap year.  Please enter the year you would like to check: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ('This is a leap year.')
        else:
            print ('This is not a leap year.')
    else:
        print ('This is a leap year.')
else:
   print ('This is not a leap year.')

