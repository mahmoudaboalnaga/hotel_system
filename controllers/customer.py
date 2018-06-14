"""
customer.py
This is the customer class file
"""

class Customer(object):
    customer_list=[]
    """docstring for Customer."""
    def __init__(self,customer_name, mobile_number):
        self.customer_name = customer_name
        self.mobile_number = mobile_number
        Customer.customer_list.append([self.customer_name , self.mobile_number])
