#*******A program of printing Palindrome numbers***********
N=int(input("Starting point="))
M=int(input("Ending point="))

if (N>=10):
    n=N
else:
    n=10
for a in range(n,M+1):
    f=0
    temp=a
    A=str(a)
    for i in A:
        j=temp%10
        f=j+f*10
        temp=temp//10
    
    if (a==f):
         print(f)
