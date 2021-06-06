class ObserverBase(object):
    def update(self, date):
        raise NotImplementedError()

class Observer(ObserverBase):
    def __init__(self, user):
        self.user = user

    def update(self, data):
        print ('%s: %s' % (self.user, data))


class Subject(object):
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        if not isinstance(observer,ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)   

class Administrator(Subject):
    def __init__(self,orders):
        self.count = 0
        self.orders = orders
        self._data = None
        self._observers = set()

    def enter(self):
        print("\nLogin: ")
        login = input()
        print("\nPassword: ")
        password = input()
        self.data = login + " " + password
        self.set_data("Left")
        return self

    def exit(self):
        self = None

    def OrderDetails(self):
        print("\nOrder id: ")
        id = int(input())
        print("\nProduct name: ")
        name = input()
        print("\nPrice: ")
        price = float(input())
        print("\nAmount: ")
        amount = float(input())
        print("\nOrdered ")
        print(name)
        print(" ")
        fprice = price*amount
        print(str(fprice))
        msg = "Ordered " + str(amount) + " " + name 
        self.orders[id].AddPrice(fprice)
        self.orders[id].AddChangeLog(msg)
        self.orders[id].CountPrice(id)
        self.set_data(msg)

    def AddWorkerToOrder(self):
        print("\nOrder id: ")
        id = int(input())
        print("\nWorker full name: ")
        name = input()
        msg = str(name) + " has been added to order #" + str(id)
        print("\n" + msg)
        self.orders[id].AddChangeLog(msg + "\n")
        self.set_data(msg)

class Order():
    def __init__ (self):
        self.price = 0
        self.changeList = ""

    def CountPrice(self,id):
        print("\nOrder #" + str(id))
        print(self.changeList)
        print("\nPrice: "+ str(self.price))

    def AddPrice(self, price_):
        self.price += price_

    def AddChangeLog(self, log):
        self.changeList += log

def main():
    orders = [Order()]
    admin = Administrator(orders).enter()
    admin.attach(Observer('Admin #0001'))
    admin.AddWorkerToOrder()
    admin.OrderDetails()
    admin.exit()

if __name__ == "__main__":
    main()