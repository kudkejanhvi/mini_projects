class Bank:
    def __init__(x):
        x.bal=700
    def dip(y):
        am=int(input("enter amount: "))
        y.bal+=am
        print("available amount",y.bal)
    def wit(y):
        am=int(input("enter amount: "))
        if y.bal>=am:
            y.bal-=am
            print("now, your amount is",y.bal)
        else:
            print("not efficient amount")
    def dis(y):
        print("available amount",y.bal)
j=Bank()

while True:
    print("1.Deposite Amount")
    print("2.Withdraw Amount")
    print("3.Display Amount")
    print("4.Exit")
    c=int(input("enter your choice: "))
    if c==1:
        j.dip()
    elif c==2:
        j.wit()
    elif c==3:
        j.dis()
    elif c==4:
        print("Thank you for Visiting")
        break
    else:
        print("plz enter corrent choice!")
