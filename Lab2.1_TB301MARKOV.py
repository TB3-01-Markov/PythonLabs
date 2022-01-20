# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Product():
    def __init__(self, productId, productName, productPrice, productSize, productSpecification):
        self.id    = productId
        self.name  = productName
        self.price = productPrice
        self.size  = productSize
        self.specification = productSpecification

class Customer():
    def __init__(self,   customerId, customerSurname, customerName, customerPatronymic, customerPhone ,customerEmail, customerCreditcard):
        self.id = customerId
        self.surname = customerSurname
        self.name  = customerName
        self.patronymic = customerPatronymic
        self.phone = customerPhone
        self.email = customerEmail
        self.creditcard = customerCreditcard


class Order():
    def __init__(self, orderId, orderCustomerid, orderProductid, orderAmount, orderDatetime):
        self.id= orderId
        self.customerid = orderCustomerid
        self.productid = check_null(orderProductid)
        self.amount = orderAmount
        self.datetime = orderDatetime
        #self.totalprice = Product.price * self.amount

    def check_null(value):
        if(value<=0.0): print("given value ", value," is not allowed value")
        else: return value

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'HELLO! {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('TB301 MARKOV')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
