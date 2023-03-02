k = input('Enter a number: ')

#enters users input in the equation
if int(k) > 5:
  print('Big Number')

#intermediate statment 'elif'
elif int(k) == 7:
  print('Lucky 7!')
  
else:  
  print('Small Number')

k = input('Enter a number: ')

#Order of operations, exchange 'if' & 'elif' content for 7 section
if int(k) == 7:
  print('Lucky 7!!')

#intermediate statment 'elif'
elif int(k) > 5:
  print('Big Number')
  
else:  
  print('Small Number')
