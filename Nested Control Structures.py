'''
  Programmer: Andre Smith
  Date: 10.21.19
  Program: Double Loop

  '''

for i in range(3):
    print('outer for loop: ' + str(i))
    for l in range(2):
        print('inner for loop: ' + str(l))

print('\n*************\n')

'''
  Programmer: Andre Smith
  Date: 10.23.19
  Program: For Loop + While Loop
  
  This program will create a for loop with a while loop embedded into it
  '''
for i in range(4):
  print('Outer for Loop: ' + str(i))
  x = 1
  while x >= 0:
    print('    While Loop: ' + str(x))

