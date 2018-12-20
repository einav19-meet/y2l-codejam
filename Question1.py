max=4000000
a=0
b=1
counter=0
x=0

while  counter<max:
    x = a + b
    a = b
    b = x
    if x%2==0:
        counter += x
print(counter)