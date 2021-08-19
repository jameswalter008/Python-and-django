class RestaurantTable:
    menu={
        'pizza':5000,
        'cola':600,
        'orange juice':2000,
        'hamburger':1000,
        'fried potato':1500
    }
    def __init__(self):
        self.total=0
        self.orders=[]

    def addorder(self,order):
        self.orders.append(order)
        self.total+=self.menu[order]
    
    def printbill(self):
        for order in self.orders:
            print(f'{order}:{self.menu[order]}')
        print(f'Total:{self.total}')

def startprogram():
    table=RestaurantTable()

    while True:
        order=input("order: ")
        table.addorder(order)

        another=input('order again? y/n?: ')

        if another=="y":
            continue;
        if another == 'n':
            table.printbill()
            break

startprogram()