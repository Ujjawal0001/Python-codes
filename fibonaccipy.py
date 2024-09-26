a=int(input("Enter number of terms : "))
firstterm=0
secondterm=1
sum=0
i=0
while i < a :
    print(firstterm)
    sum=firstterm+secondterm
    firstterm=secondterm
    secondterm=sum
    
    i=i+1
      