n=int(input("Enter a number:"))
t=num
r=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(t==rev):
    print("palindrome!")
else:
    print("Not a palindrome!")
