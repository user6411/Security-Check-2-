# use input() this time
 
age = int(input('How old are you?'))
password = input('What is your password?').strip()
true_password = 'python123'

if age >= 18 and password == true_password:
        print('login successful')

elif age >= 18 and password != true_password:
        print('login failed, password incorrect')

elif age < 18 and password == true_password:
        print('login failed, you are not old enough')

elif age < 18 and password != true_password:
        print('login failed, age and password invalid')   


