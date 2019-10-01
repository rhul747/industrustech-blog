s=str(input("enter string ofsomething"))
def rev(s):
    a=len(s)
    l1="  "
    for i in range(a-1,-1,-1):
        l1=l1+s[i]
        return l1
s1=rev(s)
if s1==s:
    print(s,"is a palindrome")
else:
    print(s,"not a palindrome")
