

count = 0

with open('2/data.txt','r') as file:

    for line in file:
        a = line.split(' ')
        b = []
        
        for i in range(len(a)):
            if '\n' in a[i]:
                b.append(int(a[i].split('\n')[0]))
            else:
                b.append(int(a[i]))
        

        num=0
        for j in range(len(b)):
            if j!=len(b)-1:
                if abs(b[j+1]-b[j])>3:
                    continue
                if b[j+1]-b[j]>0:
                    num+=1
                if b[j+1]-b[j]<0:
                    num-=1
                
        if abs(num)==len(b)-1:
            count+=1
        else:
            flag = False
            for k in range(len(b)):
                c = b.copy()
                c.remove(b[k])
                
                num1 =0
                for j in range(len(c)):
                    if j!=len(c)-1:
                        if abs(c[j+1]-c[j])>3:
                            continue
                        if c[j+1]-c[j]>0:
                            num1+=1
                        if c[j+1]-c[j]<0:
                            num1-=1
                        
                if abs(num1)==len(c)-1:
                    flag = True
                    break
            if flag == True:
                count+=1
print(count)