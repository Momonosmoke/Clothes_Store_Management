#Clothes Store Information Management System
""" This program is a simple clothing store inventory management system.
Staff: name, age, phone number, salary, shift
Customers: name, age, phone number, order number, order date, order time, order total
Goods: quantity, price, name, size, color
Order management: order number, order date, order status
Monthly report: total sales, total profit, total orders, total customers

"""
class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    def __str__(self):
        return "Name: {}, Age: {}, Phone: {}".format(self.name, self.age, self.phone)
def Person(staff):
    def __init__(self, name, age, phone, salary, shift):
        self.name = name
        self.age = age
        self.phone = phone
        self.salary = salary
        self.shift = shift
    def __str__(self):
        return "Name: {}, Age: {}, Phone: {}, Salary: {}, Shift: {}".format(self.name, self.age, self.phone, self.salary, self.shift)
def Person(Customer):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    def __str__(self):
        return "Name: {}, Age: {}, Phone: {}".format(self.name, self.age, self.phone)
class Goods:
    def __init__(self, quantity, price, name, size, color):
        self.quantity = quantity
        self.price = price
        self.name = name
        self.size = size
        self.color = color
    def __str__(self):
        return "Quantity: {}, Price: {}, Name: {}, Size: {}, Color: {}".format(self.quantity, self.price, self.name, self.size, self.color)
def Order():
    def __init__(self, order_number, order_date, order_status):
        self.order_number = order_number
        self.order_date = order_date
        self.order_status = order_status
    def __str__(self):
        return "Order number: {}, Order date: {}, Order status: {}".format(self.order_number, self.order_date, self.order_status)
def Monthly_report():
    def __init__(self, total_sales, total_profit, total_orders, total_customers):
        self.total_sales = total_sales
        self.total_profit = total_profit
        self.total_orders = total_orders
        self.total_customers = total_customers
    def __str__(self):
        return "Total sales: {}, Total profit: {}, Total orders: {}, Total customers: {}".format(self.total_sales, self.total_profit, self.total_orders, self.total_customers)
#if customer wanna refund, the order status will be refunded and customer will be lost 10% money for each order
