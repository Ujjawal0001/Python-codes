m1=[[1,2],[1,2]]
m2=[[1,2],[1,2]]

m3=[]
for i in range(2):#(r1)
    row=[]
    for j in range(2):#(c2)
        m=0
        for k in range(2):#(r2)
            m+=m1[i][k]*m2[k][j]
        row.append(m)
    m3.append(row)
print(m3)