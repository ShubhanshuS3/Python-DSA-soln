n=int(input("Enter number:"))
s= ''
while n>0:
    d=n%16
    if d<=9:
        s=s+str(d)
    else:
        s=s+chr(d+87)
    n=n//16
print(s[::-1])

