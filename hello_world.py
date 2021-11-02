var = 'mundo'
num = 1234
num2 = 5678

flo = 123.4
flo2 = 456.3
carac = 'c'
carac2 = 'd'

bol = True
bol2 = False
bol3 = None

print [var]

print [carac + carac2]

print [flo + flo2]



for x in range(1, 100, 2):
  print(x)

num = 1
for n in range (100): 
    print(num)
    num += 2

  n=100
  cant_divisores = 0
    i = 1
    while (i <= n):
        if n % i == 0:
            cant_divisores+=1
        i+=1
     if cant_divisores==2:
        print(i)