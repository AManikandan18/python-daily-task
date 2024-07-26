start=int(input("Enter the start value: "))
end=int(input("enter the end value: "))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,"is prime")

