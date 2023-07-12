class error(Exception):
    pass
class error1(Exception):
    pass
class bank:
    def _init_(self,a):
        self.a=a
    def deposite(self,amount):
        b=self.a+amount
        print(b)
    def withdraw(self, amount):
        b = self.a - amount
        print(b)
a=int(input("enter 1 for deposite  or enter 2 for withdraw or enter 3 for check balance"))
if (a==1):
    b=int(input("enter the amount to deposite  "))
    if(b==0):
        try:
            if(b<=0):
                raise error1
        except error1:
            print("invalidamountexception")
    else:
        s=bank(a)
        s.deposite(b)
elif(a==2):
    c=int(input("enter the amount to with draw  "))
    if(c>a or c<=0):
        try:
            if(c>a):
                raise error
            elif(c<=0):
                raise error1
        except error:
            print("insufficientfundexception")
        except error1:
            print("invalidamountexception")
    else:
        s=bank(a1)
        s.withdraw(c)

elif(a==3):
    s=bank()
else:
    print("thank you")