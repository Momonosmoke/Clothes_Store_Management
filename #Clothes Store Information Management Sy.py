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
staff_list = []
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
Goods_list = []
class Goods:
    def __init__(self, quantity, price, name, size, color):
        self.quantity = quantity
        self.price = price
        self.name = name
        self.size = size
        self.color = color
    def __str__(self):
        return "Quantity: {}, Price: {}, Name: {}, Size: {}, Color: {}".format(self.quantity, self.price, self.name, self.size, self.color)
orders_list = []
def Order():
    def __init__(self, order_number, order_date, order_status):
        self.order_number = order_number
        self.order_date = order_date
        self.order_status = order_status
    def __str__(self):
        return "Order number: {}, Order date: {}, Order status: {}".format(self.order_number, self.order_date, self.order_status)
#total profit = total sales - total cost - total living cost - total salary
def profit():
    total_sales = 0
    total_cost = 0
    total_living_cost = 0
    total_salary = 0
    for i in range(len(orders_list)):
        total_sales += orders_list[i].order_total
    for i in range(len(staff_list)):
        total_salary += staff_list[i].salary
    for i in range(len(Goods_list)):
        total_cost += Goods_list[i].quantity * Goods_list[i].price
    for i in range(len(staff_list)):
        if staff_list[i].shift == "Day":
            total_living_cost += staff_list[i].salary * 0.1
        elif staff_list[i].shift == "Night":
            total_living_cost += staff_list[i].salary * 0.2
    total_profit = total_sales - total_cost - total_living_cost - total_salary
    return total_profit