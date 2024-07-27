##a=10
##for i in range(10):
##    if i%2==0:
##        print(i,"even")
##    else:
##        print(i,"is odd")
        

##without using module(%):
def is_even(number):
    # Check if the least significant bit is 0 (even) or 1 (odd)
    return (number & 1) == 0

# Input from the user
num = int(input("Enter a number: "))

if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

