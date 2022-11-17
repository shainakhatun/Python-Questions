# 1.Find all element's length inforant of each elements....

# a=["ankita","shaina","anjali","roopa"]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     count=0
#     while j<len(a[i]):
#         count=count+1
#         j=j+1
#     print(a[i],count)
#     i=i+1


# 2.According to the user input make a list....

# a=int(input("entre the no:"))
# i=0
# b=[]
# while i<a:
#     n=int(input("entre the elements:"))
#     b.append(n)
#     i=i+1
# print(b)


# 3.Find all the int value present in this list....

# a=["23","ankita","shaina",14,20]
# b=[]
# i=0
# while i<len(a):
#     if type (a[i])==int:
#         b.append(a[i])
#     i=i+1
# print(b)


# 4.Indexing....
# (Output:5)

# a=[[1,2,3,[4,5],6],7]
# b=a[0][3][1]
# print(b)

# (Output:[[1,2,3,[4,5],6]])

# a=[[1,2,3,[4,5],6],7]
# a.pop()
# print(a)


# 5.Do sum of all elements present in this nested list....
# a=[2,5,2,4,[1,2,3,[4,5],6]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])!=list:
#         sum=sum+a[i]
#     else:
#         j=0
#         while j<len(a[i]):
#             if type (a[i][j])!=list:
#                 sum=sum+a[i][j]
#             else:
#                 s=0
#                 while s<len(a[i][j]):
#                     sum=sum+a[i][j][s]
#                     s=s+1
#             j=j+1
#     i=i+1
# print(sum)



# 6.Interview Practice Questions....

# (i) Remove all the zeros....
# a=[3,0,7,4,0,7,0,9,8,0,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     i=i+1
# print(b)


# (ii) Add all the zeros at the last of the list....

# a=[3,0,7,4,0,7,0,9,8,0,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b+c)


# (iii) Remove all the duplicates elements....

# a=[3,0,7,4,3,7,4,0,7,0,9,8,0,0]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in  b:
#         b.append(a[i])
#     i=i+1
# print(b)


# (iv) Do Sum of all elements present in this list ....
# a=[3,7,3,4,2]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)



# (v) Remove all duplicates and do sum....
# a=[2,4,3,5,3,5,2,6,7,8]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         sum=sum+a[i]
#     i=i+1
# print(sum)

  
# (vi) Find all the elements which are more then one....
a=[3,0,7,4,3,7,4,0,7,0,9]
i=0
b=[           ]
list=[]
while i<len(a):
    c= a.count(a[i])
    if c>1:
        b.append(a[i])
    j=0
    while j<len(b):
        if b[j] not in list:
            list.append(b[j])
        j+=1
    i+=1
print(list)



# a=[3,0,7,4,3,7,4,0,7,0,9,8,0,0,1,1,2]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(c)