#Question:1
lst1=[1,2,2,3,4,5,6,6,7,7,8]
empty_lst=[]
for e in lst1:
    if e not in empty_lst:
        empty_lst.append(e)
lst1.clear
print(empty_lst)

#Question: 2
Matrix1=[[1,2,3],[4,5,6]]
Matrix2=[[3,2,1],[6,5,4]]
Result=[[0,0,0],[0,0,0]]
for i in range(len(Matrix1)):
    for j in range(len(Matrix1[0])):
        Result[i][j]=Matrix1[i][j] + Matrix2[i][j]
print(Result)