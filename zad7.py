x = int(input("podaj pierwszą liczbę: "))
y = int(input("podaj pierwszą liczbę: "))
# petla for 
if abs(x-y)>20:
    avg = round((x+y)/2)
    for j1 in range(avg-3,avg):
        print(j1)
    for j2 in range(avg+1,avg+4):
        print(j2)
else:
    for i in range(x,y+1):
        print(i)
    
#petla while 
if x > y:
    x,y = y,x
if abs(x-y)>20:
    z = avg-3
    while z < avg:
        print(z)
        z+=1
    while z < avg+3:
        z+=1
        print(z)
else:
    while x < y:
        print(x)
        x+=1
    else:
        print(y)
        