from datetime import datetime
class Account:
      def __init__(self,name,number,password):
             self.name=name
             self.number=number
             self.password=password
             self.balance=0.0
             self.transactions=[]
      def deposit(self,deposit):
        try:
            1+deposit
        except TypeError:
            return "The amount should be in figures"
        if deposit<0:
              return "The amount has to be greater than zero"
        else:
                self.balance+=deposit
        transaction={"amount":deposit,"balance":self.balance,"time":datetime.now(),"narration":"deposit"}
        self.transactions.append(transaction)
        return "Deposited amount:{} at {}.Your new your account balance  is  {}.".format(deposit,datetime.now(),self.balance)
      def save(self,savings):
           self.savings=0.0
           return "I saved up {} yesterday,my new savings account balance is {}.".format(savings,self.savings)
      def withdrawal(self,amount):
          try:
              1+amount
          except TypeError:
              return "The amount must be in figures"
          if amount<0:
              return "The amount must be greater than zero"
          elif amount>self.balance:
              return "You have insufficient funds to complete this request"
          else:
              self.balance-=amount
              withdrawals={"amount":amount,"balance":self.balance,"time":datetime.now(),"narration":"withdrawal"}
              self.transactions.append(withdrawals)
          return "{}: {} withdrawn.New account balance is: {}.".format(datetime.now(),amount,self.balance)
      def borrow(self,loan):
          limit=15000
          amount=loan +self.balance
          if loan >limit:
              return "The loan is too high.Your loan limit is {}.Kindly borrow a lower amount".format(limit)
          elif loan<=limit and self.balance<0:
               return "You have an existing loan.Please pay up to get another one"
          elif loan<=limit and self.balance>0:
              loan_balance=loan+15/100*loan
              borrows={"amount":loan,"balance":self.balance,"time":datetime.now(),"narration":"loan"}
              self.transactions.append(borrows)
              return "{} :You have borrowed {} successfully.Your new account balance is {}.You new loan balance is :{}".format(datetime.now(),loan,amount,loan_balance)
          else:
              return "The service you need is not available now.Please try again later."
      def repay_loan(self,repay):
          if repay<0:
              return "You risk to be blacklisted.Kindly repay your loan before the due date."
          elif repay<self.loan:
                self.loan-=repay
                return "you have successfully paid {}.Your new loan balance is {}.".format(repay,self.loan)
          elif repay>self.loan:
               repay-=self.loan
               self.loan=0
               extra=repay-self.loan
               self.balance+=extra
               repayment={"amount":repay,"balance":self.balance,"time":datetime.now(),"narration":"repayment"}
               self.transactions.append(repayment)
               return "{} :You have successfully repaid your loan.Your new balance is {}.".format(datetime.now(),self.balance)
      def get_statements(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            print("{} {}: {}.New balance:{}".format(time,narration,amount,balance))
      def transfer(self,transfer,Account):
          try:
              1+transfer
          except TypeError:
              return "The amount you are sending must be in figures"
          fees=0.05*transfer
          total_transfer=transfer+ fees
          if total_transfer<0:
           return "Insufficient funds"
          elif total_transfer>self.balance:
            return "Your balance is {} and you need {} to transfer money.".format(self.balance,total_transfer)
          else:
              self.balance-=total_transfer
              return "You have transferred {} to {}.Your new balance is {}".format(transfer,Account,self.balance)
class mobileMoney(Account):
    def __init__(self,name,number,password,service_provider):
        Account.__init__(name,number,password)
        self.service_provider=service_provider
        self.limit=300000
    def buy_airtime(self,amount):
        if amount<self.balance:
            amount-=self.balance
            return "You have successfully bought {}.Your new balance is {}".format(amount,self.balance)
        else:
            return "You have insufficient funds to complete this request"





