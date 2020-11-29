a=int(input("numérateur "))
b=int(input("dénominateur "))
i=2
while i<=a and i<=b :
  if a%i==0 and b%i==0 :
    a=a//i
    b=b//i
  else :
    i=i+1
print(str(a)+"/"+str(b))