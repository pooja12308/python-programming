class bankacc:
    def __init__(self):
        self.__balance=0
    def depositamt(self,amt):
        self.__balance+=amt
    def withdrawamt(self,amt):
        self.__balance-=amt
    def getbalance(self):
        return self.__balance

obj=bankacc()
obj.depositamt(5000)
obj.withdrawamt(2000)
print(f"Final balance : {obj.getbalance()}")
