# Day 2
# name="prashantjha"
# #indexing=01234567890
# print(name[0])
# print(name[1])
# print(name[-1])
# # print(name[15]) gives error
# print(name[0:9])
# print(name[1:7])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])



# s="python is a high level progamming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())



# print("subject marks:")
# phy=50
# chem=60
# maths=70
# print("physics={} chemsitry={} math={}".format(phy,chem,maths))
# print("physics={0} chemsitry={1} math={2}".format(phy,chem,maths))
# print("physics={x} chemsitry={y} math={z}".format(x=phy,y=chem,z=maths))
# total=phy+chem+maths
# print("total marks",f"{total}")
# print("Roll No=","7".zfill(4))



#for(initialization; condition; inc/dec)
# for i in range(5): #01234
#     print(i)


# for i in range(1,5): #01234
#     print(i)

# for i in range(5): #01234
#     print(i)



# for i in range(1,11):
#     print(i*2)


# for i in range(1,11):
#     print(i*2,"",i*3,"",i*4,"",i*5)

# print()

# for i in range(1,11):
#     print(i*11,"",i*12,"",i*13,"",i*14)




# name="racear"
#     #0123456
# for i in name: 
#     print(i)



#WAP to remove the duplicates
# name="snehashirodkar"
# result=""
# for i in name:
#     if i not in result:
#         result += i
# print(result)



# for i in range(5,0,-1):
#     print(i)


# for i in range(10,0,-2):
#     print(i)



#WAP to reverse the string using for loop
# name="Mumbai"
#      #012345
# newname=""     
# n=len(name)
# for i in range(n-1,-1,-1): #i=5
#     newname+=name[i]  #name[5]
# print(newname)    
    



# #WAP to check if a given string is a palindrome
# name="racecar"
# print(name)
# print(name[::-1])

# if name == name[::-1]:
#     print("panlindrome string:")
# else:
#     print("not palindrome string")    



# mylist=["sneha","mitali","nutan","siddhi","gayatri",77,"sejal",60.52,"sneha"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[4])
# print(mylist[-1])
# print(mylist[1:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

#how to chnage the index value
# mylist[2]="Akshay"
# print(mylist)


# if "siddhi" in mylist:
#     print("yes siddhi is available")
# else:
#     print("not available")    

 ##append the value
# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)


# mylist.insert(1,"sanket")
# print(mylist)


# mylist.remove("siddhi")
# print(mylist)


# newlist=mylist.copy()
# print(newlist)


# mylist=[['sneha','shirodkar'],['85.56'],[440022,"yyy"]]
# print("example of multidimentional list:")
# print(mylist)
# # print(mylist[row][col]) #gives error
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])


# list1=["sneha","shirodkar"]
# print(list1*2)

# list2=[50,25,50]
# print(list1+list2)


# list2=[50,25,50,'sneha']
# del list2[2]
# # del list2
# print(list2)


# list2=[50,25,50,'sneha']
# list2.clear()
# print(list2)


# name="sneha"
# print(name)
# myname=list(name)
# print(myname)


# mylist=[40,30,20,10]
# mylist.reverse()
# print(mylist)


#sorting elements
# mylist=[44,22,77,0,9,88]
# mylist.sort()
# print(mylist)
#default sorting order for number is acsending order
# default sorting order for string is alphabetical order



# mylist=[44,22,77,0,9,88]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))
# mylist[0]="sneha"
# print(mylist)
# print(newlist)


# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())


# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")   



# #Tuple

# mytuple=("prashant","Ashish","rahul","sandip","komal","ankush","rajesh",23,3,15,77,"sandip")
# print(mytuple)
# print(type(tuple))

# mytuple[2]="sunil"
# print(mytuple)


# init_tuple=()
# print(init_tuple.__len__())

# init_tuple_a='a','b'
# init_tuple_b=('a','b')
# print(init_tuple_a==init_tuple_b)


# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a+init_tuple_b)


# init_tuple=('python')*3
# print(type(init_tuple))

# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)

# init_tuple=((1,2),)*7
# print(len(init_tuple[3:8]))

# names=[4,2,5,6,8,2]
# for i in names:
#     print(i)


# A=[4,0,2,5,0,1]
# for i in A:
#     if i==0:
#         A.remove(i)
#         A.append(i)
# print(A)        


# B=[1,2,2,3,4,4,5]
# result=[]
# for i in B:
#     if i not in result:
#        result.append(i)
# print(result)       


# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)


# n = int(input("Enter size: "))
# arr = []
# for i in range(n):
#     val = int(input("Enter value: "))
#     arr.append(val)
# total = 0
# print("Array:", arr)
# for i in range(n - 1):   # stop at second last index
#     value = abs(arr[i] - arr[i + 1])
#     total += value
# print("Sum:", total)


# for i in range(1,5):
#     if i==3:
#         break
#     print(i)


#zip() inside we can take multiple function
# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)
 

# A=prashant*is*a*good*programmer
# a = "prashant*is*a*good*programmer"
# b = ""
# c = ""
# for i in a:
#     if i == "*":
#         b += i
#     else:
#         c += i   
# print(b+c)           


#BODMAS
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)


# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)


# a="listen"
# b="silent"

# if sorted(a) == sorted(b):
#     print("anagram")


# WAP to count the number of words in a string

# a="this is a sentence"
# count=1
# for i in a:
#     if i==" ":
#         count+=1
# print(count)        



