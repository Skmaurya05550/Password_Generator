# Password Generator by the python code .

import random 
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
lenght = int (input(" Enter  password lenght : "))
password = " "
for a in range (lenght ):
  password +=random.choice(chars)
  
print(password)



