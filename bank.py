class Account:
  def __init__(self,accountnumber,name,phone,loan_limit):
    self.accountnumber=accountnumber
    self.name=name
    self.balance=0
    self.phone=phone
    self.loan=0
    self.loan_limit=loan_limit
  def deposit(self,amount):
    if amount<=0:
      return f"The amount you must be greater than zero"
    else:  
      self.balance+=amount
    return f"Dear {self.name} You have deposited {amount} your new balance is {self.balance}"
  def show_balance(self):
    return self.balance
  def withdraw(self,amount):
    if amount<0:
      return f"Dear {self.name} You cannot withdraw a negative amount" 
    elif self.balance<=amount:
      return f"Dear {self.name} you have insificient credit"    
    else:
      self.balance-=amount
      return f"Dear {self.name} You have successfully withdrawn {amount} your new balance is {self.balance}"
  def borrow(self,amount):
    if amount>=self.loan_limit:
      return f"Dear {self.name}, the amount you are trying to borrow is above your loan limit, please deposit more to increase your loan limit"    
    elif self.loan>0:
      return f"Dear {self.name}, You still have an uncleared loan, please clear your outstanding debts to borrow more thank you."
    elif amount<=0:
      return f"Dear {self.name}, You cannot borrow a negative amount"  
    else:
      self.loan=1
      self.balance+=amount
      return f"Dear {self.name}, You have successfully borrowed {amount}. Your new balance is {self.balance}"  
    