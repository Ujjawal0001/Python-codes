mylist=list(map(int,input("enter").split(",")))
mylist1=list(map(str,input("enter").split(",")))
# my_dict = dict(zip(mylist, mylist1))
my_dict={}
# print(my_dict)
# print(mylist)
for i in range(len(mylist)):
    my_dict[mylist[i]] = mylist1[i]
print(my_dict)