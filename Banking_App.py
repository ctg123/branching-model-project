#!/usr/bin/python
'''
Created on 10-Sep-2020

@author: ctgraves
'''
"""
 Description:
  Python program to demonstrate classes and multiple inheritance with Banking domain.
  (a.k.a. Multiple Inheritance)

  In my example, I have the customer named John Doe open up a primary checking and savings account at a Chase bank branch.
"""

# Parent class 1 - Bank
class Bank(object):
    def __init__(self, ifsc_code, bankname, branchname, loc): 
        self.ifsc_code = ifsc_code 
        self.bankname = bankname
        self.branchname = branchname
        self.loc = loc 

    def getBankInfo(self):
      print("IFSC_Code: " , self.ifsc_code)
      print("Bank name: " + self.bankname)
      print("Branch name: " + self.branchname) 
      print("Location: " + str(self.loc))
      print("\n")

# Parent class 2 - Customer
class Customer:
    # initializing the variables
    customer_id = 0
    name = ""
    address = ""
    contact_info = ""

    # defining constructor
    def __init__(self, customer_id, custname, address, contactdetails):
        self.customerID = customer_id
        self.name = custname
        self.address = address
        self.contact_info = contactdetails

    # defining class methods
    def show_name(self):
        print(self.name)

    def show_address(self):
        print(self.address)


# definition of subclass for Bank Account starts here:
class Bank_Account(Customer):

    # initializing the variables
    AccountId = ""
    balance = 0

    def __init__(self, account_id, customerID, custname, address, contactdetails):
        super().__init__(customerID, custname, address, contactdetails)
        self.AccountId = account_id

    def get_id(self):
        print("You've been assigned with the Account ID: " , self.AccountId)

    def getAccountInfo(self):
        print("Customer_ID: ", self.customerID)
        print("Customer name: ", self.name)
        print("Customer Address: " + self.address) 
        print("Contact Information: " + str(self.contact_info))
        print("\n")

    
    # The deposit function will prompt the user to enter their moneny as a floating integer.
    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance = self.balance + amount
        print("You deposited $" + str(amount) + " into your account.")

    def withdraw (self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You withdrew $" + str(amount) + " from your account.")
        else:
        #self.balance = self.balance - amount
            print(" You have an insufficient balance.")

    def getBalance(self):
        print("\n You have a total balance of $", self.balance)

# end of subclass definition for Bank Account

class Savings_Account(Bank_Account):

    # initializing the variables. Setting hard requirement for $5000 to open a Savings account.
    SMinBalance = float(5000)

    def __init__(self, account_id, customerID, custname, address, contactdetails):
        super().__init__(account_id, customerID, custname, address, contactdetails)

    def getSavingsAccountInfo(self):
        self.SMinBalance = self.SMinBalance
        print(" Customer_ID: ", self.customerID)
        print(" Customer name: ", self.name)
        print(" Customer Address: " + self.address) 
        print(" Contact Information: " + str(self.contact_info))
        print("\n You setup your Savings account with the amount of $", self.SMinBalance)
        print("\n")

    def savings_deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.SMinBalance = self.SMinBalance + amount
        print("You deposited $" + str(amount) + " into your Savings account.")
        print("You're total amount is now: $", self.SMinBalance)

    def savings_withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.SMinBalance - amount >= 5000:
            self.SMinBalance -= amount
            print("You withdrew $" + str(amount) + " from your account.")
        else:
        #self.balance = self.balance - amount
            print(" You withdrew more than the minimum ammount required for your savings account.")

    def getSavingsBalance(self):
        print("\n You have a total balance of $", self.SMinBalance)

