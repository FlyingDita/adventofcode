import numpy as np

a = []
b = []
with open('1/data.txt','r') as file:
    for line in file:
        a.append(int(line.split('   ')[0]))
        b.append(int(line.split('   ')[1].split('\n')[0]))

a.sort()
b.sort()
dis = 0
for i in range(len(a)):
    dis += abs(b[i]-a[i])

# print(dis)

score = 0
dict_b = {}
for i in b:
    if i not in dict_b.keys():
        dict_b[i]=1
    else:
        dict_b[i]+=1
for i in a:
    if i in dict_b.keys():
        score += i*dict_b[i]
print(score)
