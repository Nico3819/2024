def create_list ():
  mylist = []
  total = 0
  for x in range (0,4):
    num = int(input('Enter a number:  '))
    number = int(num)
    mylist.append(num)
    total = total + num
 # print (total)
  return (mylist) 


def sum (z):
  print ('debug %s ' % (z))
  print ('debug %s ' % (x))
  total = 0
  for y in x:
    y = int(y)
    total = total + y
  print (total)
  


x = create_list()
sum (x)
