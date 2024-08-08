##a="HELLO AND (WELCOME (TO THE) TCEA (CONTEST) TODAY) IS (SATURDAY()"
##pl=[]
##pr=[]
##for i in a:
##    if i=='(':
##        pl.append(i)
##    elif i==')':
##        pr.append(i)
##    else:
##        pass
##for i in str(pl):
##    for j in str(pr):
##        if i==j:
##            print(0)
##        else:
##            print(1)
##    
####    if pl==pr:
####        print(0)
####    else:
####        print(1)
####print(pl)
####print(pr)

def check_parentheses_balance(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 1
            stack.pop()
    
    if stack:
        return 1
    
    return 0

# Sample inputs
input1 = "HELLO AND (WELCOME (TO THE) TCEA (CONTEST) TODAY) IS (SATURDAY())"
input2 = "(9*(7-2)*(1*5)"

# Outputs
print(check_parentheses_balance(input1))  # Output: 0
print(check_parentheses_balance(input2))  # Output: 1
