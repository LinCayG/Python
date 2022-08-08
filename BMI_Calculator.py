print('We are going to calculate your BMI.')
Height = input('Please enter your height in inches: \n')
Weight = input('Please enter your weight in pounds: \n')
BMI = round((int(Weight)*703/(int(Height)*int(Height))),1)
print(f'Your BMI is calculated as: {BMI}')
if BMI < 18.5:
    print('You are considered underweight.')
elif BMI <25:
    print('You are considered to be in a normal weight range.')
elif BMI <30:
    print('You are considered overweight.')
elif BMI < 35:
    print('You are considered obese.')
else:
    print('You are considered clinically obese.')
