def sum1(n):
    return (n*(n+1)/2)

num=int(input("Enter range of natural numbers"))

print("Sum of ",num," natural numbers is",sum1(num))

def sum2(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

print("Sum of ",num," natural numbers is",sum2(num))    