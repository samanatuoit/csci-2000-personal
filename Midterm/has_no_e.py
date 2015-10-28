def has_no_e(string):
   #string = raw_input('Enter a string: ')
   temp = True
   for x in string:
      if x == 'e':
         temp = False
   if temp == False:
         #print(temp)
   else:
      temp = True
      #print(temp)
      print(temp)
#has_no_e('hlo')
#has_no_e('hello')

#def has_no_e(file):
#   print(file)

reader = open('gadsby_stripped.txt', 'r')

data = reader.read(64)
while data != '':
   has_no_e(data)




