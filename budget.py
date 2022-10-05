
class Category:
  def __init__(self, name):
    self.category=name         #instantiating categories
    self.ledger=[]             #ledger-a list
  
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return sum([i.get('amount') for i in self.ledger])

  def transfer(self, amount, cat):
    if self.check_funds(amount):
      self.withdraw(amount,f"Transfer to {cat.category}")
      cat.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, amount):
    return self.get_balance()>=amount
    
  def __repr__(self):
      s=f"{self.category:*^30}\n"
      for item in self.ledger:
        s+=f"{item.get('description')[:23]:23}" + f"{item.get('amount'):7.2f}" + '\n'
      s+=f"Total:{self.get_balance():7.2f}"
      return s

    
# food= Category('Food')
# entertainment = Category("Entertainment")
# food.deposit(100,"something")
# food.transfer(25, entertainment)
# food.withdraw(20, 'beans')
# print(food.ledger)
# print(str(food))
# print(entertainment.ledger)
# print(food.get_balance())
# print(entertainment.get_balance())

def create_spend_chart(categories):
  s="Percentage spent by category\n"
  
  withdrawals=[-sum([i.get('amount') for i in cat.ledger if i.get('amount')<0]) for cat in categories]
  percent_withdrawal = [round(i/sum(withdrawals)*100) for i in withdrawals]
  names=[cat.category.lower().capitalize() for cat in categories]
    
  for n in range(100,-10,-10):
    s+=str(n).rjust(3) +"| "
    for per in percent_withdrawal:
      s+="o  " if per >=n else "   "
    s+= "\n"
    
  s+=' '*4 + '-'*(2*(len(categories)+1)+2)
  max_len = len(max(names,key=len))
  names=[i.ljust(max_len) for i in names]
  for i in range(max_len):
    s+='\n     '
    for name in names:
      s+=name[i]+'  '
  return s
  
  
