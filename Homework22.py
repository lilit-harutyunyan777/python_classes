
import requests
import socket


class WebStore:
    _counter = dict()

    def __init__(self):
        self.hostname = None
        self.IPAddr = None
        self.response = None
        self.requests = None
        self.search_key = None
        self.search_address = None

    def address(self):
        self.search_key = input("What to order?\n")
        address = "https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search="
        self.search_address = address + self.search_key
        print(self.search_address)
        return self.search_key

    def order(self):
        self.search_address = ""
        WebStore.address(self)
        try:
            self.response = requests.get(f"{self.search_address}")
            return self.response
        except Exception as err:
            raise Exception("something wrong has happened {}".format(err))

    def hostname(self):
        self.hostname = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.hostname)

    def id_counts(self):
        WebStore.hostname(self)
        if self.IPAddr in WebStore._counter:
            WebStore._counter[self.IPAddr] += 1
        else:
            WebStore._counter[self.IPAddr] = 1
        the_best_costumer = max(WebStore._counter, key=WebStore._counter.get)
        sorted_dict = {}
        sorted_keys = sorted(WebStore._counter, key=WebStore._counter.get)
        for i in sorted_keys:
            sorted_dict[i] = WebStore._counter[i]

        print(f"The_best_costumer is {the_best_costumer}")
        print(f"Top of the best customers with their orders: {sorted_dict})")

    def ord_process(self):
        WebStore.order(self)
        WebStore.id_counts(self)


order_N = WebStore()
order_N.ord_process()


def generate_order(order):
    while True:
        yield order_N.ord_process()


my_orders = generate_order(order_N.ord_process())
for i in range(0, 1000):
    (next(my_orders))

