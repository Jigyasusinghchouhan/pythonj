num=[1, 2, 3, 4, 5]
sum=6
out=[]
for i in range(len(num)):
    if sum-num[i] in num:
        out.append([num[i],sum-num[i]])
print(sum)
print(out[:int(len(out)/2)])