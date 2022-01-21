num=int(input())
odd_sum=0
even_sum=0
while (num/10!=0):
    if(num%2==0):
        even_sum+=num%10
    else:
        odd_sum=odd_sum+num%10
    num=num//10
print(even_sum,odd_sum)