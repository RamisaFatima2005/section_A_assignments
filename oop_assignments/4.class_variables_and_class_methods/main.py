# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "National Bank" 

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_details(self):
        print(f"Customer Name: {self.customer_name}, Bank Name: {self.bank_name}")
        
customer1 = Bank("Ramisa")
customer2 = Bank("Ghayas")

customer1.show_details()
customer2.show_details()

Bank.change_bank_name("Habib Bank")

customer1.show_details()    
customer2.show_details()
