# r=int(input("Enter row"))
# c=int(input("Enter column"))
# print("Enter elements")
# matrix=[]
# for row in range(r):
#     row=[]
#     for col in range(c):
#         element=int(input())
#         row.append(element)
#     matrix.append(row)
# print(matrix)
# for rows in range(r):
#     for cols in range(c):
#         print(f"Matrix at {rows} {cols} : ",matrix[rows][cols])
# # trans = [[0 for _ in range(r)] for _ in range(c)]
# # for rows in range(r):
# #     for cols in range(c):
# #         trans[rows][cols]=matrix[cols][rows]
# # print(trans)
# trans=[]
# for rows in range(r):
#     row=[]
#     for cols in range(c):
#         row.append(matrix[cols][rows])
#     trans.append(row)
# print(trans)
#



# r=int(input("Enter row :"))
# c=int(input("Enter column :"))
# print("Enter values")
# matrix=[]
# for i in range (r):
#     row=[]
#     for j in range (c):
#         a=int(input())
#         row.append(a)
#     matrix.append(row)
# print(matrix)
m1=[[1,2],[3,4],[5,6]]
m2=[[1,2],[3,4]]
m3=[]
for i in range (3):
    row=[]
    for j in range(2):
        m=0
        for k in range(2):
            m+=m1[i][k]*m2[k][j]
        row.append(m)
    m3.append(row)

     print(m3)      
 

