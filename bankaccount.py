class Account():
  def __init__(self, name, account_number):
    self.name = name
    self.account_number = account_number
    self.balance = 0
  def Add_money(self, Amount):
    self.balance +=Amount
    print('Money added to your account')
  def Display_amount(self):
    print(f"Account Number: {self.account_number} \nName: {self.name} \nBalance: Nu.{self.balance}")
  def Withdraw(self, Amount):
    if Amount > self.balance:
      print('Insufficent Balanace')
    else:
      self.balance -=Amount
      print('Money withdrawn from your account')

  def transfer_money(self, transfer_amount, acc):
    if transfer_amount > self.balance:
      print("Insuffcient Balance to transfer")
    else:
      self.Withdraw(transfer_amount)
      acc.Add_money(transfer_amount)
      # self.balance -= transfer_amount
      # acc.balance += transfer_amount
      print('Money has be transferred')

