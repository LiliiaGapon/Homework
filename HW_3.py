class_of_student=int(input('Enter the number of student: ')) #вводимо загальну кількість студентів в класі

assessment=[] # всі оцінки студентів
status=[] # є лише два статуси
passeds=[] #всі хто здав екзамен
faileds=[] #всі хто не здав екзамен

for i in range (class_of_student):
    student_assessment=int(input('Enter student assessment: '))
    assessment.append(student_assessment) #до наявних додаємо поточну оцінку студента
    status_exam=str(input('Enter status exam (pased/failed): ')).lower()
    status.append(status_exam) #до наяних додаємо поточний статус студента
class_students=dict(zip(assessment,status)) #словник, який в собі містить оцінку-статус
for key, value in class_students.items(): #обираємо куди віднесемо ключ-значення
    if value == 'pased':  #якщо значення 'pased'
        passeds.append(key) # ключ додаємо до списку passeds
    elif value == 'failed':  #якщо значення 'failed'
        faileds.append(key) # ключ додаємо до списку faileds

if max(faileds) > min(passeds): # треба порівняти чи був послідовним
    print('Professor Gruble was not consistent')
else:
    print(f'Professor Gruble was consistent and the threshold for passing the exam is in the range of' f' {max(faileds) + 1} – {min(passeds)} range.')

#var2
import random
assessments=[] # всі оцінки студентів
for i in range(3):
    assessment = random.randint(1, 100) #обираємо рандомну оцінку від 1 до 100
    status = random.randint(0, 1) #обираємо рандомну статус 0 або 1
    result = 'p' #визначаємо, що результат екзамену зданий і він буде відповідати 'p' і значенню 1
    if status == 0: #якщо статус буде 0
        result = 'f' #то результат екзамену буде не зданий 'f'
    assessments.append([assessment, result]) #в список оцінок добавляємо оцінку і результат або 'p'або 'f'
print(assessments) #подивимось на цей список оцінок


passed = [] # створюємо список тих, хто здав
failed = [] # створюємо список тих, хто не здав
for assessment in assessments: # визначаємо умови для кожної оцінки і куди вона потрапить
    if assessment[1] == 'p': #якщо для оцінки результат(1 це його індекс в послідовності оцінка-результат) = 'p'
        passed.append(assessment[0]) #то добавляємо в список тих, хто здав і ставимо оцінку (індекс 0 - тобто перше значення)
    else:
        failed.append(assessment[0]) # при інших умовах добавляємо в список тих, хто не здав і ставимо оцінку (індекс 0 - тобто перше значення)

if len(passed) == 0 or len(failed) == 0: #якщо хоч один список зданих або незданих пустий - пишемо що був послідовним
    print('Професор був послідовним')
else: #в інших випадках
    min_passed = min(passed) #нам потрібно визначити мінімальну оцінку зданих
    max_failed = max(failed) #і нам потрібно визначити максимальну оцінку незданих
if min_passed > max_failed: # і якщо мінімально-здана оцінка є більшою за максимально-нездану то все ок
    print(f'Професор був послідовним. Порог здачі екзамена знаходиться в діапазоні від  {max_failed} до {min_passed}.')
else: # в іншому випадку є непослідовність
    print('Профессор был непоследовательным.')

#var 3
import random
students = ['student1', 'student2', 'student3', 'student4', 'student5', 'student6']
slovnyk = {}
for student in students:
    slovnyk[student] = (random.randint(60, 100), random.choice(['Failed', 'Passed']))
print(slovnyk)
# Let`s check if all results are Failed or all results are Passed
all_passed = True
for student, (grade, result) in slovnyk.items():
    if result != "Passed":
        all_passed = False
        break
all_failed = True
for student, (grade, result) in slovnyk.items():
    if result != "Failed":
        all_failed = False
        break
if all_passed or all_failed:
    print("Professor Grubl was consistent in marking the same result")
else:
    min_passed = 100
    max_failed = 60
    for student, (grade, result) in slovnyk.items():
        if grade > max_failed and result == 'Failed':
            max_failed = grade
        elif grade < min_passed and result == 'Passed':
            min_passed = grade
    if min_passed <= max_failed:
        print("Professor Grubl wasn't consistent in marking 'Passed' for students")
        print(f'{min_passed} (min_passed) < {max_failed} (max_failed)')
    else:
        print("Professor Grubl was consistent in marking 'Passed' for students")
        print(f'{min_passed} (min_passed) > {max_failed} (max_failed)')
        print(f"The threshold for passing the exam: {max_failed+1,min_passed}")