# name="sai narendra"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.casefold())
# print(name.swapcase())
# print(name.title())

# string input
# str=input()
# print(str)


# l=["a,b,c,d,e"]
# for i in l:
#     print(i.upper())


# L = ['A', 'B', 'C', 'D', 'E']
# i =len(L)
# for x in L:
#     print(i,x)
#     i = i-1
# for i in range (14,21,1):
#     print(i)

# l = ["a","b","c","d","e"]
# for i in range(len(l)-1,-1,-1):
#     print(i, l[i].upper())


l=["mani","PANITHA","nanDINI","rAM"]
for i in range(len(l)):
    if i%2==0:
        print(l[i].lower())
    else:
        print(l[i].upper())
