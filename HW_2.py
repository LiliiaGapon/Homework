"""
1. Як вхідні дані запитайте ціле число. Якщо воно ділиться на 3, виведіть "foo"; якщо воно ділиться на 5,
виведіть "bar"; якщо воно ділиться на обидва, виведіть "ham" (а не "foo" або "bar").
"""
integer_number=int(input('Enter integer number: '))

if integer_number % 3 == 0 and integer_number % 5 == 0:
      print('ham')
elif integer_number % 3 == 0:
      print('foo')
elif integer_number % 5 == 0:
      print('bar')
else:
      print('else number')

"""
2.Як вхідні дані запитайте два числа та виведіть яке з них менше і яке більше
"""
number_1=int(input('Enter first number: '))
number_2=int(input('Enter second number: '))

print('Number _1 is bigger' if number_1>number_2 else 'Number _2 is bigger')


"""
3. Як вхідні дані запитайте три числа і виведіть найменше, середнє та найбільше. Припустимо, всі вони різні
"""
import  statistics
number_1=int(input('Enter first number: '))
number_2=int(input('Enter second number: '))
number_3=int(input('Enter third number: '))

list_1=[number_1,number_2,number_3]
print('Max:',max(list_1),'Min:', min(list_1),'Median' ,statistics.median(list_1))

"""
4.Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100; якщо число ділиться на 3, замість числа виведіть "fizz".
Якщо воно ділиться на 5, замість числа виведіть "Buzz". Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.
"""
number=0
while number<100:
    number+=1
    if number %3==0 and number %5==0:
        print('fizz buzz')
        continue
    elif number %3==0:
        print('fizz')
        continue
    elif number %5==0:
        print('buzz')
        continue

    print(number)

"""
5.Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100; якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM"
замість числа
"""
number=0
while number<100:
    number+=1
    if number %7==0:
        print('BOOM')
        continue
    elif str(7) in str(number):
        print('BOOM')
        continue
    print(number)

