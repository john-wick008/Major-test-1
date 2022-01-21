num=int(input())
lis=[int(ele) for ele in input().split()]
lis.sort()
value=1
for i in range(1,len(lis)+1,1):
    if(lis[i-1]==value):
        value+=1
    else:
        break
print(value)