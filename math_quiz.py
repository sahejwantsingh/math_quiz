import pyinputplus as pyip
import random, time

number_of_question = 15
correct_answer=0

print("Let's begin Math Quiz")
#Addition Quiz
print('Start with Addition')
time.sleep(2)
for question_number in range(1,6):
    #choose random numbers
    num1= random.randint(0,60)
    num2= random.randint(0,60)

    prompt = f'#{question_number}: {num1} + {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'{num1+num2}'], blockRegexes=[('.*', 'Incorrect!')], timeout=10, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct')
        correct_answer += 1
    time.sleep(1)

#Subraction Quiz
print('Continue with Subraction')
time.sleep(2.5)
for question_number in range(1,6):
    #chose random numbers
    num1= random.randint(0,70)
    num2= random.randint(0,75)

    prompt = f'#{question_number}: {num1} - {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'{num1-num2}'], blockRegexes=[('.*', 'Incorrect!')], timeout=12, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct')
        correct_answer += 1
    time.sleep(1)

#Multiplication quiz
print('Its time for Multiplication')
time.sleep(2.5)
for question_number in range(1,6):
    #chose random numbers
    num1= random.randint(0,12)
    num2= random.randint(0,9)

    prompt = f'#{question_number}: {num1} X {num2} = '
    try:
        pyip.inputStr(prompt, allowRegexes=[f'{num1*num2}'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct')
        correct_answer += 1
    time.sleep(1)
print(f'{correct_answer}/{number_of_question}')
