from datetime import datetime
now=datetime.now()
class Account:
  def __init__(self,accountnumber,name,phone,loan_limit):
    self.accountnumber=accountnumber
    self.name=name
    self.balance=0
    self.phone=phone
    self.loan=0
    self.loan_limit=loan_limit
    self.transactions=[]
    self.withdrawals=[]
    self.loans=[]
    self.loanpays=[]
  def deposit(self,amount):
    if amount<=0:
      return f"The amount you must be greater than zero"
    else:  
      self.balance+=amount
      transaction={"amount": amount, "balance": self.balance, "Time":  now.strftime("%D"), "Naration": "deposit"}
      self.transactions.append(transaction)
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
      withdrawal={"amount": amount, "balance": self.balance, "Time":  now.strftime("%D"), "Naration": "withdraw"}
      self.withdrawals.append(withdrawal)
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
      loan={"amount": amount, "balance": self.balance, "Time":  now.strftime("%D"), "Naration": "loan"}
      self.loans.append(loan)
      return f"Dear {self.name}, You have successfully borrowed {amount}. Your new balance is {self.balance}"  
#ability  to show transactions
  def loan_repayment(self,amount):
      if amount<=0:
        return f"please put a positive amount"
      elif amount<self.loan:
        self.loan-=amount
        return f"Dear {self.name} You have paid {amount} on your loan"
      else:
        difference=amount-self.loan
        self.balance+=difference 
        loanpay={"amount": amount, "balance": self.balance, "Time":  now.strftime("%D"), "Naration": "loan payment"}
        self.loanpays.append(loanpay)
        return f"Dear {self.name} you have fully paid your loan, your account balance is {self.balance}" 
  def get_statement(self):
    for transaction in self.transactions:
      narration = transaction["Naration"]
      amount =transaction["amount"]
      balance = transaction["balance"]
      time = transaction["Time"]
      print(f"Dear {self.name}, You made a {narration} of {amount} on {time}, your balance is {balance} thank you.")
    for withdrawal in self.withdrawals:
      narration = withdrawal["Naration"]
      amount =withdrawal["amount"]
      balance = withdrawal["balance"]
      time = withdrawal["Time"]
      print(f"Dear {self.name}, You made a {narration} of {amount} on {time}, your balance is {balance} thank you.")
    for loan in self.loans:
      narration = loan["Naration"]
      amount =loan["amount"]
      balance = loan["balance"]
      time = loan["Time"]
      print(f"Dear {self.name}, You acquired a {narration} of {amount} on {time}, your balance is {balance} thank you.")
    for loanpay in self.loanpays:
      narration = loanpay["Naration"]
      amount =loanpay["amount"]
      balance = loanpay["balance"]
      time = loanpay["Time"]
      print(f"Dear {self.name}, You made a {narration} of {amount} on {time}, your balance is {balance} thank you.")
        
