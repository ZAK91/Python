x=0
while x <11:
    print(x)
    x +=1
print("------Q1------")    

for x in range(11):
    print (x)
print("------Q2------")

for x in range(11):
    if x==5:
        break
        print (x)
print("------Q3------")

for x in range(11):
    if x==5:
        continue
     print (x)
print("------Q3------")

print("The multiplication table from 1 to 5 ")
for x in range(1, 6):
    for y in range(1,6):
     print(f"\n {x} x {y} = {x*y}")
     print("------Q4------")
for x in range(10,21):
    print(x)
print("------Q5------")
for x in range(10,101,3):
    print(x)
print("------Q5------")
x=range(1,100)
