# n=int(input())
# if n%2==0:
#     print("even number")
# else:
#     print("odd number")


# freq
# n=input()
# emp={}
# for i in n:
#     if i not in emp:
#         emp[i]=1
#     else:
#         emp[i]+=1
# print(emp)


#vowel con count
# str=input()
# vcount=0
# ccount=0
# for i in str:
#     if i in "aeiouAEIOU":
#         vcount+=1
#     else:
        # ccount+=1
# print("vcount",vcount,"ccount",ccount)


# prime number
# n=int(input())
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print(n,"prime")



# range of prime numbers
# n=int(input())
# count=0
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"notprime")
#             break
#     else:
#         count+=1
#         print(i,"prime")
# print(count)



# max element
# l=[1,2,3,4,5,78,9,0,99]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)


# reverse without slicing
# s=input()
# e=""
# for i in s:
#     e=i+e
#     if s==e:
#         print("palindrome")
#         break
# else:
#     print("not palindrome")


# multip table
# n=int(input())
# o=int(input())
# for i in range(1,n+1):
#     for j in range(1,o+1):
#         print(f"{i}*{j}={i*j}")
#     print()



# row=int(input())
# i=row
# while i>1:
#     print("*"*i)
#     i-=1


# forward
# row=int(input())
# i=0
# while i<row:
#     print("*"*i)
#     i+=1


# spaces
rows=int(input())
space=" "
star="*"
i=0
while i<rows:
    print(space*i+star*(rows-i))
    i+=1
