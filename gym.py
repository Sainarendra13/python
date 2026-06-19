print("****welcome to hulk fitness****")
print(" 1.strength\n 2.cardio\n 3.personaltraining\n 4.zumba")
fee=100
while True:
    n=int(input("choose the option you want"))
    if n==1:
        fee+=1000
        print(fee,"you have successfully paid for strength training")
        break
    elif n==2:
        fee+=1500
        print(fee,"you have successfully paid for cardio")
        break
    elif n==3:
        fee+=5000
        print(fee,"you have successfully paid for personal training")
        break
    elif n==4:
        fee+=2500
        print(fee,"you have successfully paid for zumba")
        break
    else:
        print("please check valid option")
        break
    
print("****thank you for visiting hulk fitness****")   
