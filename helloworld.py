# Roy Davis

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

while True:
  print('Hello there, what language would you like to use, Spanish, French,Portuguese?')#greeting in English
  name = input()
  if name ==('Spanish'):   
   print('Hola, como estas')
  
  if name ==('French'):    
   print ('Salut comment allez-vous')
  
  if name ==('Portuguese'):    
   print ('Oi como vai')

  if name ==('quit'):#Use to end the program
   exit()
  
  