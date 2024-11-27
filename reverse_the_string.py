a=input("Enter your ordered word: ")
rev_val=""
for i in a:
    rev_val=i+rev_val
print(rev_val)

print(a[::-1])

print(''.join(reversed(a)))


