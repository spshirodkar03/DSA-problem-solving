# Day1
# math = 50
# name = "Sneha"
# pi = 3.14
# result=True
# print(type(math))
# print(type(name))
# print(type(pi))
# print(type(result))

# print(id(math))
# print(id(name))
# print(id(pi))
# print(id(result))

# math=50 #new memory
# chem=50
# phy=50
# hindi=30
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(hindi))

# print(2+2)
# print("2"+"2")
# val1=int(input("enter value of val1:"))#2
# val2=int(input("enter value of val2:"))#4
# print(val1+val2)


# print(int(3.14))
# # print(int(10.5j)) gives error 
# print(int(True)) #=1 
# print(int(False)) #=0
# # print(int("4.22")) gives error
# print(int("4"))



# float()
# print(float(3)) #3.0
# # print(float(50+2j)) gives error
# print(float(True)) #1.0
# print(float(False)) #0.0
# print(float(4.22))
# print(float("4"))

#complex() used function
# print(complex(3)) 
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex(5.6))
# print(complex(5,-3))
# # print(complex("name"))
# print(complex(True,False))



# ##bool() is used to convert
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))



# val1=int(input("enter the value of val1:")) #100
# val2=int(input("enter the value of val2:")) #200
# print("before swapping val1=",val1,"val2=",val2)
# val1=val1+val2   #temp=100
# val2=val1-val2    #val1=200
# val1=val1-val2    #val2=100




# p1=int(input("enter the marks of p1"))
# p2=int(input("enter the marks of p2"))
# p3=int(input("enter the marks of p3"))
# total=p1=p2+p3
# percentage=total/3.0
# print("total=",total)
# print("percentage=",percentage)



# p_amount=int(input("enter principal amount:")) #100000
# roi=int(input("enter rate of interest:")) #10
# time=int(input("enter duration of loan amount:")) #1
# si=p_amount*roi*time/100
# print("simple interest=",si)



# h1=float(input("enter height in feet"))
# inch=h1*12
# cm=inch*2.54
# print("height in inch:",inch)
# print("height in cm:",cm)


# num=123 #num=321
# a=num%10 #a=3
# num=num//10 #num=12
# b=num%10 #b=2
# c=num//10 #c=1
# rev=a*100+b*10+c*1  #300+20+1=321
# print(rev)



# #123456
# num=123456  #654321
# a=num%10 #a=6
# num=num//10 #12345
# b=num%10 #b=5
# num=num//10 #
# c=num%10 #c=4
# num=num//10 
# d=num%10 #d=3
# num=num//10
# e=num%10 #e=2
# num=num//10
# f=num%10
# rev=a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)


# a=10
# b=10
# print(a is b) #True
# print(a is not b) # False


# name="helpcode"
# print("z" in name) #false
# print("p" in name) #true


#WAP to accept any one no and check pos neg and zero
# no=int(input("enter any one number:")) #-4
# if no>0:
#     print("positive number")
# if no<0:
#     print("negative number")  
# if no==0:
#     print("number is zero")     




# n1=int(input("enter the valueof n1 number:"))
# n2=int(input("enter the value of n2 number:"))
# n3=int(input("enter the value of n3 number:"))
# n4=int(input("enter the value of n4 number:"))
# n5=int(input("enter the value of n5 number:"))

# if n1>n2 and n1>n3 and n1>n4 and n1>n5:
#     print("n1 is greater=",n1)
# if n2>n1 and n2>n3 and n2>n4 and n2>n5:
#     print("n2 is greater=",n2)    
# if n3>n1 and n3>n2 and n3>n4 and n3>n5:
#     print("n3 is greater=",n3)    
# if n4>n1 and n4>n3 and n4>n2 and n4>n5:
#     print("n4 is greater=",n4)    
# if n5>n1 and n5>n2 and n5>n3 and n5>n4 :
#     print("n5 is greater=",n5)  




# username=input("enter username:")
# password=input("enter password:")
# if username==password:
#     print('login successfull')
# else:
#     print("invaild credential")    





#WAP to accept phy.chem, and maths subject calculate total and percentage and if percentage is greater than eqaul to 60 and greater is equal to male so he is elligible for placement else eligible for data entry too
# phy=int(input("enter the marks:"))
# chem=int(input("enter the marks:"))
# maths=int(input("enter the marks:"))
# gender=input("enter the gender")
# total=phy+chem+maths
# percentage=total/3.0
# if(percentage>=60 and gender=="male/Female"):
#      print("eligible for placement") 
# else:
#      print("eligible for data entry")    



# A=int(input("enter A:"))
# B=int(input("enter B:"))
# C=int(input("enter C:"))

# if A>B:
#     if A>C:
#         print("print A is MAX")
# else:
          
#     if B>C:
#         print("B is greater")  
#     else:
#         print("C is greater")       


###Accept the day mon to sat and sun weekend
# day=input("enter day name:")
# if day=="Saturday" or day=="SATURDAY" or day=="sunday" or day=="SUNDAY":
#     print("Weekend")
# else:
#     print("working day") 



# ch=ord(input("enter any character"))

# if ch>=65 and ch<=91:
#     print("your entered chracyer is in upper case")
# elif ch>=97 and ch<=122:
#      print("your entered character is in lower case")  
# elif ch>=48 and ch<=57:        
#      print("your entred character is digit") 
# else:
#       print("your entered character is in special symbols") 



# Amount=int(input("please enter amount for withdraw")) 
# print("100 notes= ",Amount//100)
# print("50 notes= ",(Amount%100)//50)
# print("20 notes= ",((Amount%100)%50)//20)
# print("10 notes= ",(((Amount%100)%50)%20)//10)
# print("5 notes= ",((((Amount%100)%50)%20)%10)//5)