height = float(input('Digite sua altura: \n'))
weight = int(input('Digite seu peso: \n'))

bmi = weight / (height**2)

if bmi < 18.5:
  print(f'Your BMI is {bmi:.2f}, you are underweight.')
elif bmi < 25:
  print(f'Your BMI is {bmi:.2f}, you have a normal weight.')
elif bmi < 30:
  print(f'Your BMI is {bmi:.2f}, you are slightly overweight.')
elif bmi < 35:
  print(f'Your BMI is {bmi:.2f}, you are obese.')
else:
  print(f'Your BMI is {bmi:.2f}, you are clinically obese.')
