#1 Запросіть у користувача ім'я та місячну зарплату в доларах та виведіть їхню річну зарплату в тисячах доларів.
#first var
name=input('Enter your name: ')
salary=int(input('Enter your salary per month in dollars: '))

print('Annual salary in thousands of dollars: ',round(salary*12/1000))

#second var
print('Name: {name} \n Annual salary in thousands of dollars: {salary}'.format(name=name,salary=round(salary*12/1000)),end='\n')

#2 2. Запросіть ціле число і виведіть True, якщо це парне число діапазоні від 100 до 999, інакше - «False».
#first var
whole_number=int(input('Enter whole number: '))
if whole_number%2==0 and 100<=whole_number<=999:
    print('True')
else:
    print('False')

#second var
whole_number=int(input('Enter whole number: '))
if whole_number%2==0 and 100<=whole_number<=999:
    print('True')
elif whole_number%2==1  and 100<=whole_number<=999:
    print('False')
else:
    print('No info')

#third var
whole_number=int(input('Enter whole number: '))
result = 'True' if whole_number%2==0 and 100<=whole_number<=999 else 'False'
print(result)

#3 Як вхідні дані візьмемо ціле число; Це число від 101 до 999, а його остання цифра не дорівнює нулю.Виведіть число, що складається з чисел першого у зворотньому порядку.
x = int(input('Enter whole number between 101 and 999 (the last digit is not zero): '))
x = str(x)
x = (x[2] + x[1] + x[0])
print(x)

#4
'''
Запитайте два цілих числа та виведіть:
a. Їхню суму
b. Їхня різниця
c. результат множення
d. Результат поділу першого на друге
e. Залишок від поділу першого на друге
f. True, якщо перше число більше або дорівнює другому, інакше False.
'''
n_first=int(input('Enter first whole number: '))
n_second=int(input('Enter second whole number: '))
print(f'Add: {n_first+n_second}\nSub: {n_first-n_second}\nMultip: {n_first*n_second}\nDivision: {round(n_first/n_second,1)}\nModulus: {n_first%n_second}')
if n_first>=n_second:
    print('True')
else:
    print('False')
#second var
result='True' if n_first>=n_second else 'False'
print(result)