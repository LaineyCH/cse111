import math
import datetime
w=int(input('Enter the width of the tire in mm: '))
a=int(input('Enter the aspect ratio of the tire: '))
d=int(input('Enter the diameter of the wheel in inches: '))

 
volume= math.pi*w**2*a*(w*a + 2540 *d)/10000000000
volume=round(volume, 2)

print(f'The approximate volume is {volume} liters'.format(volume))
 
current_date=datetime.date.today()

if w==185 and a==50 and d==14:
    price='50 $'
elif w==205 and a==60 and d==15:
    price='60 $'
else:
    price='0'
print(price)
ask=input('Do you want to buy tires with the dimensions that you entered YES or NO? ')
if ask=='YES':
   client_cell=int(input('What is your phone number? '))
else:
    print('Thanks. Good evening!')
   
with open ('volumes.txt','a') as client_info:
    client_info.write(f'{current_date},{w},{a},{d},{volume},{client_cell}\n')