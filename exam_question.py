class bank_account:
    def __init__(self,account_number,account_holder,balance):
        self.set_account_number(account_number)
        self.set_account_holder(account_holder)
        self.set_balance(balance)

    def set_account_number(self,account_number):
        if( type(account_number) == type("sdfsf") or type(account_number) == type (12) ):
            self.__account_number=account_number
        else:
            self.__account_number=None
    
    def get_account_number(self):
        return self.__account_number
    
    def set_account_holder(self,account_holder):
        flag=True
        for char in account_holder :
            if not char.isalpha()  and char != " " and char != '.' :
                flag=False
        
        if flag:
            self.__account_holder=account_holder
        else:
            self.__account_holder=None
    
    def get_account_holder(self):
        return self.__account_holder
    
    def set_balance(self,balance):
        if balance >= 0:
            self.__balance=balance
        else:
            self.__balance=0
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if(self.get_balance()>amount):
            self.set_balance(self.get_balance()-amount)
        else:
            print("Error")
    
    def __str__(self):
        return(f"account holder:{self.get_account_holder()} account number: {self.get_account_number()} has balance of {self.get_balance()} AUD")

def main():
    bank1=bank_account("abc 999","lisa-hans",80)
    bank1.withdraw(20)
    bank2=bank_account(1232,"asdss&",80)

    print(bank1.__str__())
    print(bank2.__str__())

if __name__== "__main__":
    main()

