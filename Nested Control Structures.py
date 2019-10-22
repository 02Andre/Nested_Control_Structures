'''
  Programmer: Andre Smith
  Date: 10.21.19
  Program: Double For Loop
 '''

for i in range(3):
    print('outer for loop: ' + str(i))
    for l in range(2):
        print('     inner for loop: ' + str(l))

print('\n*************\n')

'''
  Programmer: Andre Smith
  Date: 10.22.19
  Program: Average Test Scores
 
  This program asks for the test scores for multiple people
  and reports the avg test score for each
  '''

num_people = int(input('how many people are taking the test: '))
test_per_person = int(input('how many test are going to be averaged?: '))

for i in range(num_people):
    name = input('Enter name: ')
    sum = 0
    for j in range(test_per_person):
        score = int(input('    Enter a Score: '))
        sum = sum + score
    average = float(sum) / test_per_person
    print('    Average for ' + name + ': ' + str(round(average, 2)))
