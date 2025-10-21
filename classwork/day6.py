attendance = [18,20,19,15,21]
full_class= 0
total_attendance = 0
for x in attendance:
 print(x)
 if x >= 20:
    print('class is full')
    full_class += 1
 else:
    print('class is not full')
 total_attendance += x   
print('no of days full:',full_class)
print('total attendance:',total_attendance)