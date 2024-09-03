for i in range (10):
    print('Hello')

for i in range (15):
    i=i+1
    print('Hello! i is set to ' + str(i))

for i in range(1,1000000):
    print(i)

n = 1000000
sum = n *(n+1)/2
print(sum)

integer1 = input('please enter an integer between 1 to 10: ')
integer2 = input('please enter another integer between 1 to 10: ')
integer1 = int(integer1)
integer2 = int(integer2)
for number in range(integer1,integer2, 2):
    print(number**2)

integerty = input('please enter an integer: ')
integerty = int(integerty)
if integerty ==2:
    print('prime number')
elif integerty %2 == 0:
    print('even number')
else:
    print('print number')
