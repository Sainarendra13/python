# programs on if

# Write a program to check if a number is greater than 10
# n=int(input())
# if n>10:
#     print("number is greater than 10 ")

# Write a program to check if a person is eligible to vote (age 18 or above).
# age=int(input())
# if age>=18:
#     print("you are eligible to vote")

# Write a program to check if a number is positive.
# num=int(input())
# if num>0:
#     print("positive")

# Write a program to check if a number is negative.
# num=int(input())
# if num<0:
#     print("negative")


# programs on if else 
# Write a program to check if a number is even or odd.
# num=int(input())
# if num%2==0:
#     print("even")
# else:
#     print("odd")



# Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40).
# marks=int(input())
# if marks>40:
#     print("passed")
# else:
#     print("failed")


# programs on if elif else
# Write a program to classify a number as positive, negative, or zero.
# num=int(input())
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# liters_used=int(input())
# if liters_used<100:
#     print("less used")
# elif liters_used >=100 and liters_used<=500:
#     print("moderate usage")
# else:
#     print("high usage")



# nested if
# A student needs at least 35 marks to pass. If they score above 90, they get a scholarship.
# marks=int(input())
# if marks>35:
#     print("passed")
# if marks>90:
#     print("eligible for scholarship")

# Write a program that asks for a person's age and checks if tickets are available.
# age = int(input("Enter age:"))
# if age >= 18:
#     seats = input("Are seats available? (yes/no): ")  
#     if seats.lower() == "yes":
#         print("Booking Confirmed")
#     else:
#         print("Tickets Sold Out")
# else:
#     print("Not eligible for this movie")

#  condi completed
# x=["a","b","c","d","e","f"]
# for i in range(len(x)):
#     if i%2==0:
#         print(x[i].upper())


# x=["a","b","c","d","e","f"]
# i=0
# while i<len(x):
#     if i%2==0:
#         print(x[i].upper())
#     i+=1

# x = ["a","b","c","d","e","f"]
# y = []
# for i in x[::-1]:
#     if i not in y:
#         y.append(i)
# print(y)


# for i in range(100,200):
#     if i%2!=0:
#         continue
#     print(i)

# i = 0
# while i<=3:
#     j = 0
#     while j<=3:
#         print(j)
#         j+= 1
#     i +=1



# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# n=4
# i=1
# while i<=n:
#     print("*"*2)
#     i+=1



# n=int(input())
# for i in range(n,-1,-1):
#     for j in range(n):
#         print(n-j,end=" ")
#     print()

# str=input()
# vcount=0
# ccount=0
# for i in range(len(str)):
#     if str[i] in "aeiou,AEIOU":
#         vcount+=1
#     else:
#         ccount+=1
# print(vcount)
# print(ccount)
# str="beautiful"
# length=0
# for i in str:
#     length+=1
# print(length)


# n=int(input())
# for i in range(2,n):
#     if n%i!=0:
#         print("prime")
#         break
# else:
#     print("not prime")


# str="beautiful"
# count=1
# em={}
# for i in str:
#     if i not in em:
#         em[i]=1
#     else:
#         em[i]+=1
# print(em)




# n=int(input())
# for i in range(2,n):
#     if n%i==0:
    





# n=int(input())
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"not prime")
#             break
#     else:
#         print(i,'prime')

# # 
# n=int(input())
# count=0
# s=0
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         s+=i
#         count+=1
# print(count)
# print(s)



# fibanocii
# n=int(input())
# a=0
# b=1
# for i in range(n):
#     # print(a)
#     c=a+b
#     print(c)
#     a=b
#     b=c


# l=[1,2,3,4,5,78,9,0,99]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)



