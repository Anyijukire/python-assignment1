class Bank:
    def __init__(self,accountnumber,name,idnumber):
      self.accountnumber=accountnumber
      self.name=name
      self.idnumber=idnumber
    def deposit(self):
        return f'Hello my name is {self.name} and I am depositing 7000 dollars on {self.accountnumber} account number and my id number is {self.idnumber}'
    def withdraw(self):
        return f'Hello my name is {self.name} and I am withdrawing 7000 dollars on {self.accountnumber} account number and my id number is {self.idnumber}'